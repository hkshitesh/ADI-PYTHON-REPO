ADIlist = [10, 20, 30, 40]

ADIiter = iter(ADIlist)

try:
	while True:
		print(next(ADIiter))
except StopIteration:
	print("stop!")