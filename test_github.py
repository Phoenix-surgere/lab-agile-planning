import torch

print(torch.__version__)
def add(x,y):
	z = x+y
	return z if z>0 else -z

def rem(x,y):
	return x-y 


def addAdv(x,y,z):
	return x+y+z
print(f"This is {add(-4,3)}!")

	