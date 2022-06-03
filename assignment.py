Data Analytics
Q.1] Download the Market basket dataset.
Write a python program to read the dataset and display its information.
Preprocess the data (drop null values etc.)
Convert the categorical values into numeric format.
Apply the apriori algorithm on the above dataset to generate the frequent itemsets and
association rules.
Solution :

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
store_data=pd.read_csv('marketbasket.csv',header=None)
store_data.head()
records = []
for i in range(0,300):
records.append([str(store_data.values[i,j]) for j in range(0,20)])
association_rules=apriori(records,min_support=0.0045,min_confidence=0.2,min_
lift=3,min_length=2)
association_results=list(association_rules)
print(len(association_results))
print(association_results[0])
for item in association_results:
pair = item[0]
items = [x for x in pair]
print("Rule:"+items[0]+"->"+items[1])
print("Support:"+str(item[1]))
print("Confidence:"+str(item[2][0][2]))
print("Lift:"+str(item[2][0][3]))
print("========================================")
Q.2] Download the groceries dataset.
Write a python program to read the dataset and display its information.
Preprocess the data (drop null values etc.)
Convert the categorical values into numeric format.
Apply the apriori algorithm on the above dataset to generate the frequent itemsets and
association rules.
Solution :

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
store_data=pd.read_csv('groceries.csv',header=None)
store_data.head()
records = []
for i in range(0,300):
records.append([str(store_data.values[i,j]) for j in range(0,20)])
association_rules=apriori(records,min_support=0.0045,min_confidence=0.2,min_
lift=3,min_length=2)
association_results=list(association_rules)
print(len(association_results))
print(association_results[0])
for item in association_results:
pair = item[0]
items = [x for x in pair]
print("Rule:"+items[0]+"->"+items[1])
print("Support:"+str(item[1]))
print("Confidence:"+str(item[2][0][2]))
print("Lift:"+str(item[2][0][3]))
print("========================================")
Q.3] Write a python code to implement the apriori algorithm. Test the code
on any standard dataset.
Solution :

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
store_data=pd.read_csv('Medical_Data.csv',header=None)
store_data.head()
records = []
for i in range(0,300):
records.append([str(store_data.values[i,j]) for j in range(0,20)])
association_rules=apriori(records,min_support=0.0045,min_confidence=0.2,min_
lift=3,min_length=2)
association_results=list(association_rules)
print(len(association_results))
print(association_results[0])
for item in association_results:
pair = item[0]
items = [x for x in pair]
print("Rule:"+items[0]+"->"+items[1])
print("Support:"+str(item[1]))
print("Confidence:"+str(item[2][0][2]))
print("Lift:"+str(item[2][0][3]))
print("========================================")