import sys
sys.path.append("../")
from util.stat import *
import pickle

with open('../result/debug.pk','rb') as f:
	partial_data = pickle.load(f)

num = len(partial_data)
total_list = []
for x in partial_data.values():
    total_list += list(x.keys())

freq1 = count_freq(total_list)
major_l, minor_l = auto_select_major_class(freq1)

