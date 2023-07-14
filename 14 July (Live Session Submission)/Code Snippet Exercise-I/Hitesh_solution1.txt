ADI_list = [10, 20, 30, 40]
ADIiter = iter(ADI_list)
try:
    while True:
        val = next(ADIiter)
        print(val)
except StopIteration:
    print('Stop!')
