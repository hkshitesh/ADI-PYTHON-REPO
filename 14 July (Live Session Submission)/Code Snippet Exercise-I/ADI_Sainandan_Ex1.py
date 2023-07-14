ADI_list = [10, 20, 30, 40]

# check if the list is iterable or not
# use  dir() function. dir() will list all the function that the object has

# Iterables will implement __iter__() function
# But Iterators will implement both __iter__() and __next__() function
# So all iterators are iterables but not all iterables are iterators
print(dir(ADI_list))

ADIiter = iter(ADI_list)

try:
    while True:
        item = next(ADIiter)
        print(item)
except StopIteration:
    print('Stop!')
