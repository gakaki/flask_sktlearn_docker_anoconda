
# coding: utf-8

# In[8]:


import numpy as np
#import matplotlib as mpl
#import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import argparse
import uuid
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV, ElasticNetCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model.coordinate_descent import ConvergenceWarning
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from math import ceil
from pandas import Series,DataFrame


# In[9]:


#mpl.rcParams['font.sans-serif']=[u'simHei']
#mpl.rcParams['axes.unicode_minus']=False
###########3.具体方法选择##########
####3.1决策树回归####
from sklearn import tree
model_DecisionTreeRegressor = tree.DecisionTreeRegressor()
####3.2线性回归####
from sklearn import linear_model
model_LinearRegression = linear_model.LinearRegression()
####3.3SVM回归####
from sklearn import svm
model_SVR = svm.SVR()
####3.4KNN回归####
from sklearn import neighbors
model_KNeighborsRegressor = neighbors.KNeighborsRegressor()
####3.5随机森林回归####
from sklearn import ensemble
model_RandomForestRegressor = ensemble.RandomForestRegressor(n_estimators=20)#这里使用20个决策树
####3.6Adaboost回归####
from sklearn import ensemble
model_AdaBoostRegressor = ensemble.AdaBoostRegressor(n_estimators=50)#这里使用50个决策树
####3.7GBRT回归####
from sklearn import ensemble
model_GradientBoostingRegressor = ensemble.GradientBoostingRegressor(n_estimators=100)#这里使用100个决策树
####3.8Bagging回归####
from sklearn.ensemble import BaggingRegressor
model_BaggingRegressor = BaggingRegressor()
####3.9ExtraTree极端随机树回归####
from sklearn.tree import ExtraTreeRegressor
model_ExtraTreeRegressor = ExtraTreeRegressor()


# In[48]:


def getHeadFromFile():
    #paths=path[0:path.index(".")]
    #names=paths.split("-")
    #names=['date', 'sales_num']
    return names

def getDataFromFile(jsonstring):
    #df = pd.read_csv(path, sep='\t', low_memory=False)
    #new_df = df.replace('?', np.nan)
    #datas = new_df.dropna(how = 'any')
    #jsondata = json.loads(jsonstring)
    # print("具体的jsonstring 到底是 " + jsonstring)
    df=DataFrame(eval(jsonstring))
    # df     = DataFrame(jsonstring)
    new_df = df.replace('?', np.nan)
    datas = new_df.dropna(how = 'any')
    return datas


# In[49]:


def try_different_method(X_train,X_test,Y_train,Y_test,X,model):
    model.fit(X_train,Y_train)
    #joblib.dump(model, strname) 
    #result = model.predict(X_test)
    score = model.score(X_test, Y_test)
    return  float('%.02f'%score),model.predict(X)
    #plt.figure()
    #plt.plot(np.arange(len(result)), Y_test,'go-',label='true value')
    #plt.plot(np.arange(len(result)),result,'ro-',label='predict value')
    #plt.title('score: %f'%score)
    #plt.legend()
    #plt.show()
def process(jsonstring,date):
    datas=getDataFromFile(jsonstring)
    length=datas.iloc[0].size
    X = datas.iloc[:,0:length-1]
    Y = datas.iloc[:,length-1]
    X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
    X = date.split(",")
    X = [ float( x ) for x in X if x ]
    X=[X]
    dic={}
    #uid=str(uuid.uuid1())
    ####3.1决策树回归####
    modelname="model_DecisionTreeRegressor"
    #score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_DecisionTreeRegressor,mpath+modelname)
    score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_DecisionTreeRegressor)
    #mtest = joblib.load("model_DecisionTreeRegressor") 
    #ypredit=mtest.predict(X)
    dic[modelname]=[int(ceil(ypredit[0])),score]
    ####3.2线性回归####
    modelname="model_LinearRegression"
    #score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_LinearRegression,mpath+modelname)
    score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_LinearRegression)
    #mtest = joblib.load("model_LinearRegression")  
    #ypredit=mtest.predict(X)
    dic[modelname]=[int(ceil(ypredit[0])),score]
    ####3.5随机森林回归####
    modelname="model_RandomForestRegressor"
    #score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_RandomForestRegressor,mpath+modelname)
    score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_RandomForestRegressor)
    #mtest = joblib.load("model_RandomForestRegressor")  
    #ypredit=mtest.predict(X)
    dic[modelname]=[int(ceil(ypredit[0])),score]
    
    ####3.6Adaboost回归####
    modelname="model_AdaBoostRegressor"
    #score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_AdaBoostRegressor,mpath+modelname)
    score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_AdaBoostRegressor)
    #mtest = joblib.load("model_AdaBoostRegressor")  
    #ypredit=mtest.predict(X)
    dic[modelname]=[int(ceil(ypredit[0])),score]
    
    ####3.7GBRT回归####
    modelname="model_GradientBoostingRegressor"
    #score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_GradientBoostingRegressor,mpath+modelname)
    score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_GradientBoostingRegressor)
    #mtest = joblib.load("model_GradientBoostingRegressor")  
    #ypredit=mtest.predict(X)
    dic[modelname]=[int(ceil(ypredit[0])),score]
    
    ####3.8Bagging回归####
    modelname="model_BaggingRegressor"
    #score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_BaggingRegressor,mpath+modelname)
    score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_BaggingRegressor)
    #mtest = joblib.load("model_BaggingRegressor")  
    #ypredit=mtest.predict(X)
    dic[modelname]=[int(ceil(ypredit[0])),score]
    
    ####3.9ExtraTree极端随机树回归####
    modelname="model_ExtraTreeRegressor"
    #score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_ExtraTreeRegressor,mpath+modelname)
    score,ypredit=try_different_method(X_train,X_test,Y_train,Y_test,X,model_ExtraTreeRegressor)
    #mtest = joblib.load("model_ExtraTreeRegressor")  
    #ypredit=mtest.predict(X)
    dic[modelname]=[int(ceil(ypredit[0])),score]
    
    return dic


# In[50]:


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=' ')
    parser.add_argument('--jsonstring') 
    parser.add_argument('--date')
    #parser.add_argument('--mpath')
    args = vars(parser.parse_args())
    print(process(**args))
    #jsonstring='[[2017,2,0,346],[2017,3,0,347],[2017,4,0,348],[2017,5,1,349],[2017,6,2,350]]'
    #mpath='C:/Users/zhuwei/ml/datas/models/'
    #print(getDataFromFile(jsonstring,getHeadFromFile()))
    #print(process('date-sales_num.csv','2018-01'))
    #print(jsonstring)
    #print(process(jsonstring,'2018,1,2',mpath))


# In[ ]: