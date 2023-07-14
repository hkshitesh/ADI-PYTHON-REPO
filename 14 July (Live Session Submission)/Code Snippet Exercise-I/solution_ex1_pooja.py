ADI_list = [10,20,30,40]
ADIiter = iter(ADI_list)
try:
	while True:
		next_val = next(ADIiter)
    print(val, end=' ')
except StopIteration:
	print('Stop!')
