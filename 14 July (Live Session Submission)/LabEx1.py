import pandas as pd
df= pd.read_excel("Iterator-Lab.xlsx", sheet_name=0)
list_power = list(df['Power'])
list_Device = list(df['Device'])
list_Current = list(df['Current'])
sort_list_power = sorted(list_power, reverse=True)
top1= sort_list_power[0]
top2= sort_list_power[1]
index1= list_power.index(top1)
index2= list_power.index(top2)
print("The Device names for top two power rating are: ",list_Device[index1],' ',list_Device[index2])
print("The Current Rating for top two power rating are: ", list_Current[index1], ' ', list_Current[index2])
print("The Power Rating for top two power rating are: ", list_power[index1], ' ', list_power[index2])

