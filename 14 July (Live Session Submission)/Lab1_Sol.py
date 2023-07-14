import pandas as pd
df= pd.read_excel("Iterator-Lab.xlsx", sheet_name=0)
list_device = list(df['Device'])
list_current = list(df['Current'])
list_power = list(df['Power'])
sort_list_power= sorted(list_power, reverse=True)
index_1= list_power.index(sort_list_power[0])
index_2= list_power.index(sort_list_power[1])
print(index_1)
print(index_2)
print("Top Two power rating Devices are ", list_device[index_1], ' ',list_device[index_2])
print("Top Two power rated Current readings are ", list_current[index_1], ' ',list_current[index_2])
print("Top Two power readings are ", list_power[index_1], ' ',list_power[index_2])


