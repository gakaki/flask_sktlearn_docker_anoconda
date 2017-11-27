# Nvidia Docker 镜像 https://hub.docker.com/r/nvidia/cuda/
FROM nvidia/cuda:9.0-cudnn7-runtime
LABEL maintainer "Go-Capture gakaki <gakaki@qq.com>"

# 前置步骤
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH
WORKDIR /root/


# 使用镜像 安装anoconda https://github.com/ContinuumIO/docker-images/blob/master/anaconda3/Dockerfile
# 清华大学 anoconda 镜像地址 https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

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

ENTRYPOINT [ "/usr/bin/tini", "--" ]

## 如果你觉得镜像过大 可以使用airpline和miniconda3组合 然而airpline并没有gpu的nvida的docker
## 所以使用内网千兆+镜像docker仓库是提高开发效率的必要步骤
## mini conda https://hub.docker.com/r/continuumio/miniconda3/

# 设置conda镜像为中国清华大学源 https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/
RUN conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ && \
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ && \
conda config --set show_channel_urls yes

# copy 本地文件去镜像里
COPY . /root/

# 安装本地requirments的包
RUN conda install --yes --file requirements.txt

# 安装 juputer


# 安装 tensorflow同时支持 gpu加速 和 cpu sse 加速的版本

# 暴露flask端口
EXPOSE 5000
# 运行flask
CMD [ "python","flask_data_sales_num.py" ]
