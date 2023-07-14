# 1
ADI_List = [10,20,30,40]
ADIIter = iter(ADI_List)
try:
  while True:
    next(ADIIter)
except StopIteration:
  print('Stop!')
  
