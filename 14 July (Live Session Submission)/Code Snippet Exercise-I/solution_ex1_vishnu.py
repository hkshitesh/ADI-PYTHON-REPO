
ADI_list = [10, 20, 30, 40]
# print all the method of ADI_LIST
print(dir(ADI_list))

ADIiter = iter(ADI_list)
# print all the methods of ADIiter
print(dir(ADIiter))

try:
    while True:
	    print(next(ADIiter))
except StopIteration:
    print('Stop!')
