def ADI_Fun(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
ADI_Fun (2.0, 3.0)
ADI_Fun (3.0, 3.0)
