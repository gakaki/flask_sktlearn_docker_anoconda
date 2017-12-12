# Nvidia Docker 镜像 https://hub.docker.com/r/nvidia/cuda/
FROM nvidia/cuda:9.0-cudnn7-runtime
LABEL maintainer "Go-Capture gakaki <gakaki@qq.com>"

# 前置步骤
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH
WORKDIR /root/

# 替换为aliyun 的源头
COPY apt_sources.list /etc/apt/sources.list

# 使用镜像 安装anoconda https://github.com/ContinuumIO/docker-images/blob/master/anaconda3/Dockerfile
# 清华大学 anoconda 镜像地址 https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

# 这里其实最好还是吧anaconda给下载下来copy之后在安装不然体积太大实在是很容易安装失败
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.0.1-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh


## 注意下面的在ubuntu 17.10系统里其实用不上这是给16的ubuntu设计的东西
RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

## 如果你觉得镜像过大 可以使用airpline和miniconda3组合 然而airpline并没有gpu的nvida的docker
## 所以使用内网千兆+镜像docker仓库是提高开发效率的必要步骤
## mini conda https://hub.docker.com/r/continuumio/miniconda3/

# 设置conda镜像为中国清华大学源 https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/
RUN conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ && \
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ && \
conda config --set show_channel_urls yes

# 继续使用清华大学的py镜像源加速pip
#COPY pip.conf ~/.pip/pip.conf
RUN mkdir -p  ~/.pip/ &&  echo "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple" > ~/.pip/pip.conf

#COPY requirements.txt /root/requirements.txt
# 安装本地requirments的包 juputer pandas之类
# 醉了 跑 RUN conda update anaconda 会死机 奇怪
#RUN conda install --yes --file /root/requirements.txt
RUN conda install --yes boto3 flask scikit-learn keras \
numpy requests ujson jupyter pandas

# 安装pytorch 不知道requirments怎么装
#RUN conda install pytorch=0.1.12 cuda80 -c soumith

# copy 本地文件去镜像里
COPY tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whl /root/tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whl

# 安装 tensorflow同时支持 gpu加速 和 cpu sse 加速的版本
# https://github.com/mind/wheels/releases 复杂死了 还有针对aws这种的版本 我这里是本机笔记本还是generic 的cuda9吧
RUN pip install /root/tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whl

#COPY . /root/
# 暴露flask端口
EXPOSE 9999
# 运行flask
#ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "python","flask_data_sales_num.py" ]

# docker build -t="gc/python:latest" .
# docker run -it gc/python:latest /bin/bash
# docker run gc/python:latest