ADI_list = [10, 20, 30, 40]
ADIiter = iter(ADI_list)
try:
    while True:
        item = next(ADIiter)
        print(item)
except StopIteration:
    print('Stop!')
