ADI_list = [10, 20, 30, 40]
ADIiter = iter(ADI_list)
print(type(ADIiter))
try:
    while True:
        val = next(ADIiter)
        print(val, end=' ')
except StopIteration:
    print('Stop!')
