#Create the following dataset in python Convert the categorical data into numeric format.
# Apply the apriori algorithm on the above dataset to generate the frequent itemsets and association rules
# .Repeat the process with different min_sup values

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
dataset=[["Bread","Milk"],["Bread","Diaper","Beer","Eggs"],["Milk","Diaper","Beer","Coke"],
         ["Bread","Milk","Diaper","Beer",],["Bread","Milk","Diaper","Coke"]]

te=TransactionEncoder()
te_array=te.fit(dataset).transform(dataset)
df=pd.DataFrame(te_array,columns=te.columns_)
print("Result after preprocessing")
print(df)
freq_items_ap=apriori(df,min_support=0.01,use_colnames=True)
print("\nResult after apriori algorithm")
print(freq_items_ap)
rules_ap=association_rules(freq_items_ap,metric='confidence',min_threshold=0.8)
freq_items_ap['length']=freq_items_ap['itemsets'].apply(lambda x:len(x))
print("\nFrequent 2 Item Sets")
print(freq_items_ap[freq_items_ap['length']>=2])
print("\nFrequent 3 Item Sets")
print(freq_items_ap[freq_items_ap['length']>=3])