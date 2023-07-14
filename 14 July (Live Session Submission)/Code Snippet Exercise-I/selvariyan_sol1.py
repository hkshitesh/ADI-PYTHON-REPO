ADI_list = [10, 20, 30, 40]
print(dir(ADI_list))

ADIiter = iter(ADI_list)
print(dir(ADIiter))

try:
    while True:
        val = next(ADIiter)
        print(val)
except StopIteration:
    print('Stop!')
