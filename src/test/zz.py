import pandas as pd 
import pprint
from nn import dist

data = pd.read_csv('in.csv')

var = data.tail(96)

# print(var)
# pt = list(var.iloc[:,0])
lat = list(var.iloc[:,5])
lon = list(var.iloc[:,6])
num = len(lat)

ans = [[0 for _ in range(num)] for __ in range(num)]
# print(len(ans), len(ans[0]))

for i in range(num):
	for j in range(num):
		ans[i][j] = dist(lat[i], lat[j], lon[i], lon[j])

for matrix in ans:
	print(matrix, end=',\n')

