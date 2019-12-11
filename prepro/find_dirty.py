import sys
sys.path.append("../")
from util.stat import *
import pickle

with open('../result/debug.pk','rb') as f:
	partial_data = pickle.load(f)
target = '4800万像素'
for row in partial_data.values():
	if target in row.keys():
		print(row)

