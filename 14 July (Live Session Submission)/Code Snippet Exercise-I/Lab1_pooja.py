import pandas as pd

df = pd.read_excel("Iterator-Lab.xlsx", sheet_name= 0,index_col = 0)
print(df)

list_Device = list(df["Device"])
list_Current = list(df["Current"])
list_Power = list(df["Power"])
print(list_Device)
print(list_Current)
print(list_Power)

sorted_list_Power = sorted(list_Power, reverse = True)
print(sorted_list_Power[0], sorted_list_Power[1])

index_1 = list_Power.index(sorted_list_Power[0])
index_2 = list_Power.index(sorted_list_Power[1])
print(index_1, index_2)

print("Top two power rating Devices are ", list_Device[index_1], ' ', list_Device[index_2])
print("Top two power rated Current readings are ", list_Current[index_1], ' ', list_Current[index_2])
print("Top two Power ratings are ", list_Power[index_1], ' ', list_Power[index_2])

iterator_list_Power = iter(list_Power)

print("\n Iterarte Power \n")
while True:
    try:
        print(next(iterator_list_Power))
    except StopIteration:
        break
print("\n Iterarte Current \n")
iterator_list_Current = iter(list_Current)
for cur in iterator_list_Current:
    print(iterator_list_Current.__next__())
