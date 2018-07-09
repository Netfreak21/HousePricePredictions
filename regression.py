import csv
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import LassoCV
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score
from sklearn import metrics
#performing a train test split 
l=0
with open('all_data.csv','rb') as csvfile:
    rowread=csv.reader(csvfile)
    for row in rowread:
    	if l==0:
	    	with open('test_data.csv','a') as fil:
	            writ=csv.writer(fil)
	            writ.writerow(row)
	        with open('train_data.csv','a') as fil2:
	            writer=csv.writer(fil2)
	            writer.writerow(row)
        elif row[11]=="NaN":
            with open('test_data.csv','a') as file1:
                writer=csv.writer(file1)
                writer.writerow(row)
        else:
            with open('train_data.csv','a') as file2:
                writer=csv.writer(file2)
                writer.writerow(row)
        l=l+1
#converting hexadecimal house ids to integer
#filling up NaN values using interpolation
train_data=pd.read_csv('train_data.csv',converters={"id1":lambda x:int (x,16)})
train_data.interpolate(method='akima',inplace=True)
train_data.sort_values(by="id1",inplace=True)
#filling the still not filled values with the average value of the coloumn
train_data['bathroom'][0]=2
train_data.drop(['id1','garden','renovation'],axis=1,inplace=True)
train_features=train_data.drop(['price'],axis=1)
train_features.describe()
train_labels=train_data['price']
test_data=pd.read_csv('test_data.csv',converters={"id1":lambda x:int (x,16)})
test_data=test_data.drop(['price'],axis=1)
test_data.interpolate(method='akima',inplace=True)
test_data=test_data.sort_values(by='id1')
test_data.drop(['id1','garden','renovation'],axis=1,inplace=True)
test_data.info()
test_features=test_data
print "still some missing values"
test_data['location'][0]=1
#LASSOCV REGRESSION
reg=LassoCV(max_iter=1500,precompute=True,alphas=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10],selection='random',normalize=True)
reg.fit(train_features,train_labels)
pred=reg.predict(test_features)
#predicting the r2 score
print "lassocv regression score-------------",reg.score(train_features,train_labels)
#LINEAR REGRESSION
reg=LinearRegression(normalize=False)
scores=cross_val_score(reg,train_features,train_labels,cv=5,scoring='r2')
print "Linear Regression score--------------",scores.mean()
#RIDGE REGRESSION
test_labels=[]
l=0
with open("/home/aryan/Desktop/Logical Rhythm/solution.csv",'rU') as csvfile:
    rowreader=csv.reader(csvfile)
    for row in rowreader:
        if l!=0:
            test_labels.append(int(row[1]))
        l=l+1
reg=Ridge(alpha=0.5,max_iter=100,tol=0.00001,random_state=42)
reg.fit(train_features,train_labels)
print "Ridge Regression score---------------",reg.score(test_features,test_labels)
#XGBOOST TECHNIQUE
train_data=pd.read_csv('train_data.csv',converters={"id1":lambda x:int (x,16)})
#train_data.interpolate(method='akima',inplace=True)
train_data.sort_values(by="id1",inplace=True)
#filling the still not filled values with the average value of the coloumn
train_data['bathroom'][0]=2
train_data.drop(['id1','garden','renovation'],axis=1,inplace=True)
train_features=train_data.drop(['price'],axis=1)
train_features.describe()
train_labels=train_data['price']
test_data=pd.read_csv('test_data.csv',converters={"id1":lambda x:int (x,16)})
test_data=test_data.drop(['price'],axis=1)
#test_data.interpolate(method='akima',inplace=True)
test_data=test_data.sort_values(by='id1')
test_data.drop(['id1','garden','renovation'],axis=1,inplace=True)
test_data.info()
test_features=test_data
print "still some missing values"
test_data['location'][0]=1
eval_set=[(test_features,test_labels)]
model=XGBRegressor(max_depth=3,n_estimators=350,learning_rate=0.1)
model.fit(train_features, train_labels, eval_metric="error", eval_set=eval_set, verbose=True)
pred=model.predict(test_features)
from sklearn.metrics import r2_score
print "XGBoost Regression score-------------",model.score(train_features,train_labels)
#calculating cross validation score to check for overfitting
from sklearn.model_selection import cross_val_score 
score=cross_val_score(model,test_features,test_labels,cv=10,scoring='r2')
import xgboost
import matplotlib
xgboost.plot_importance(model)
matplotlib.pyplot.show()
print " score acheived",score

    
