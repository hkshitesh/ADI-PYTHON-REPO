ADI_list = [10, 20, 30, 40]

ADIiter = iter(ADI_list)

try:
    while True:
	    print(next(ADIiter))
except StopIteration:
    print('Stop!')
