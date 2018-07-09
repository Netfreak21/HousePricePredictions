import pandas as pd 
all_data=pd.read_csv("all_data.csv",converters={"id1": lambda x: int(x,16)})
all_data.sort_values(by="id1",inplace=True)
print all_data.info()
print "Data sorted in order of house id's for easy interpretation..."
print "Analysing data for data analysis.."
import seaborn as sns
import matplotlib.pyplot as plt
print "plotting the scatterplot of capital distance feature"
for i in range(0,len(all_data)/10):
	plt.scatter(all_data['capital'][i],all_data['price'][i])
plt.show()
print "here we see a strong relation between capital distance and price.."
print "now trying for knight distance"
for i in range(0,len(all_data)/10):
	plt.scatter(all_data['knighthouse'][i],all_data['price'][i])
plt.show()
print "seems very similar to capital distance"
print "lets try for blessings"
for i in range(0,len(all_data)/10):
	plt.scatter(all_data['blessings'][i],all_data['price'][i])
plt.show()
print "ALL THE 3 FEATURES ARE VERY IMPORTANT FOR REGRESSION"
print "but we should check if they all are correlated or not"
print "lets print the correlation matrix"
sns.set(style='ticks',color_codes=True)
plt.figure(figsize=(40,40))
sns.heatmap(all_data.corr(),linewidths=0.1,square=True,linecolor='white',annot=True)
plt.show()
print "seems like they all are almost same"
print "lets try for other features"
g=sns.FacetGrid(all_data,col='dining')
g.map(plt.hist,'price',bins=50)
all_data.plot(kind='scatter',x='garden',y='kingvisit')
print "king visit only those houses which have gardens with them"

