#making list of all important features which can help us extracting features from strings
keywords=["Built","Priced","garden","Dock","Capital","Royal","Guarding","River","dining","bedrooms","bathrooms","pay","Sorcerer","blessings","farm","Location","Holy","Knight's","ID","renovation","sorcerer","Visited"]
#list of all files from which data needs to be extracted where file name represents the name of the builder
files=["Bob.txt","Bright_Brothers.txt","Masters_of_Stones.txt","Not_Known.txt","The_Greens.txt","The_Kings.txt","The_Lannisters.txt","The_Ollivers.txt","The_Overlords.txt","The_Starks.txt","Wood_Priests.txt"]
import re
import datetime
import csv
#all_data.csv will contain our whole data with features as well as the actual prices
#missing values filled with NaN
with open('all_data.csv','wb') as csvfile :
    writer=csv.writer(csvfile)
    writer.writerow(["Dining","Bathrooms","Kings visit","Guarding","FarmSize","knightsdistance","builder","bedrooms","royal","holy tree","priced year","Dock","blessings","built year","sorcerer curse","capital","renovation","River","house id",])
#searching every file for features
for index in range(0,len(files)):
	file1=open("/home/aryan/Housing Prices/"+files[index])
	a=[]
	a=file1.readlines()
	l=0
#setting the target map default value which will give the values of the corresponding features
	target_map={'price':"NaN",'location':"NaN",'builder':"NaN",'build':"NaN",'priced':"NaN",'sorcerer_curse':"NaN",'kingspay':"NaN",'blessings':"NaN",'id':"NaN",'farm':"NaN",'garden': "NaN",'Dock': "NaN",'Capital':"NaN",'Royal':"NaN",'Guarding':"NaN",'River':"NaN",'dining':"NaN",'bedrooms':"NaN",'holytree':"NaN",'renovation':"NaN",'bathrooms':"NaN",'knight':"NaN"}
	while l<len(a):
	    x=0
	    for i in a[l].split():
	        for j in range(0,len(keywords)):
#searching for any keyword match
	            if i==keywords[j]:
	                x=1
	                if j==2:
	                    for k in a[l].split():
	                        if k=="no":
	                            target_map['garden']=0
	                        elif k=="beautiful":
	                            target_map['garden']=1
	                elif j==3:
	                    y=re.findall("\d+\.\d+", a[l])
	                    target_map['Dock']=y[0]
	                elif j==4:
	                    y=re.findall("\d+\.\d+", a[l])
	                    target_map['Capital']=y[0]
	                elif j==5:
	                    y=re.findall("\d+\.\d+", a[l])
	                    target_map['Royal']=y[0]
	                elif j==6:
	                    y=re.findall("\d+\.\d+", a[l])
	                    target_map['Guarding']=y[0]
	                elif j==7:
	                    y=re.findall("\d+\.\d+", a[l])
	                    target_map['River']=y[0]
	                elif j==8:
	                    y=re.findall("\d+", a[l])
	                    target_map['dining']=y[0]
	                elif j==9:
	                    y=re.findall("\d", a[l])
	                    target_map['bedrooms']=y[0]
	                elif j==10:
	                    y=re.findall("\d+", a[l])
	                    target_map['bathrooms']=y[0]
	                elif j==17:
	                    y=re.findall("\d+\.\d+", a[l])
	                    target_map['knight']=y[0]
	                elif j==19:
	                    for k in a[l].split():
	                        if k=="not":
	                            target_map['renovation']=0
	                    if target_map['renovation']=="NaN":
	                        target_map['renovation']=1
	                elif j==16:
	                    for k in a[l].split():
	                        if k=="stands":
	                            target_map['holytree']=1
	                    if target_map['holytree']=="NaN":
	                        target_map['holytree']=0
	                elif j==14:
	                    for k in a[l].split():
	                        if k=="small":
	                            target_map['farm']=0
	                        elif k=="huge":
	                            target_map['farm']=1
	                        elif k=="no":
	                            target_map['farm']=2;
	                elif j==18:
	                    m=a[l].split();
	                    target_map['id']=m[len(m)-1]
	                elif j==13:
	                    y=re.findall("\d+", a[l])
	                    target_map['blessings']=y[0]
	                elif j==11:
	                    target_map['kingspay']=0
	                elif j==21:
	                    target_map['kingspay']=1
	                elif j==12:
	                    target_map['sorcerer_curse']=0
	                elif j==20:
	                    target_map['sorcerer_curse']=1
	                elif j==0 :
	                    match1=re.findall(r'\d{2}/\d{2}/\d{4}',a[l][0:30])
	                    if len(match1) !=0:
	                        target_map['build']=match1[j][6:]
	                    else:
	                        match2=re.findall('\d{1}/\d{2}/\d{4}',a[l][0:30])
	                        if len(match2)!=0:
	                            target_map['build']=match2[j][5:]
	                        else:
	                            match3=re.findall('\d{1}/\d{1}/\d{4}',a[l][0:30])
	                            target_map['build']=match3[j][4:]
	                elif j==1:
	                    match1=re.findall(r'\d{2}/\d{2}/\d{4}',a[l][31:])
	                    if len(match1) !=0:
	                        target_map['priced']=match1[0][6:]
	                    else:
	                        match2=re.findall('\d{1}/\d{2}/\d{4}',a[l][31:])
	                        if len(match2)!=0:
	                            target_map['priced']=match2[0][5:]
	                        else:
	                            match3=re.findall('\d{1}/\d{1}/\d{4}',a[l][31:])
	                            target_map['priced']=match3[0][4:]
	                elif j==15:
	                    if "King's Landing" in a[l]:
	                        target_map['location']=0
	                    elif "The Mountains" in a[l]:
	                        target_map['location']=1
	                    elif "Cursed Land" in a[l]:
	                        target_map['location']=2
	                    elif "Servant's Premises" in a[l]:
	                        target_map['location']=3
	                #if no match of features then it is an empty line
	                #at this point we take all the features of map and insert it in a form of row in all_data.csv
	    if x==0:
	    	if (files[index]=="Not_Known.txt"):
	    		target_map['builder']="NaN"
	    	else:
	        	target_map['builder']=index
	        with open('/home/aryan/Housing Prices/house_prices.csv') as csvf:
	            reader=csv.DictReader(csvf)
	            for row in reader:
	                if row['House ID']==target_map['id']:
	                    target_map['price']=row['Golden Grains']
	                    break
	        l=l+1
	        with open('all_data.csv','a') as csvfile :
	            writer=csv.writer(csvfile)
	            writer.writerow(target_map.values())
	            #resetting the map
	        target_map={'price':"NaN",'location':"NaN",'builder':"NaN",'build':"NaN",'priced':"NaN",'sorcerer_curse':"NaN",'kingspay':"NaN",'blessings':"NaN",'id':"NaN",'farm':"NaN",'garden': "NaN",'Dock': "NaN",'Capital':"NaN",'Royal':"NaN",'Guarding':"NaN",'River':"NaN",'dining':"NaN",'bedrooms':"NaN",'holytree':"NaN",'renovation':"NaN",'bathrooms':"NaN",'knight':"NaN"}
	    l=l+1
	print index,"st file extraction complete"
	print "================================================================================================"
