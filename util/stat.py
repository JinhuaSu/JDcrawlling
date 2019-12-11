from fuzzywuzzy import fuzz

def count_freq(l):
	fre_dict = {}
	for x in l:
		fre_dict[x] = fre_dict[x] + 1 if x in fre_dict.keys() else 1	
	return fre_dict

def auto_select_major_class(fre_dict,threshold_ratio=0.8):
	sum_ = sum(fre_dict.values())
	queue = sorted(list(fre_dict.items()),key=lambda x:x[1],reverse =True)
	threshold = sum_ * threshold_ratio
	count = 0
	major_list = []
	while count < threshold:
		pop = queue.pop(0)
		major_list.append(pop[0])
		count += pop[1]
	minor_list = [x[0] for x in queue]
	return major_list,minor_list
		
def fuzzy_map(major_list,minor_list,method = 'all'):
	map_dict = dict(zip(major_list,major_list))
	for one in minor_list:
		max_score = 0
		mapping = None
		for compare in major_list:
			score = fuzz.ratio(one,compare) if method == 'all' else fuzz.partial_ratio(one,compare)
			if score > max_score:
				max_score,mapping = score,compare
		map_dict[one] = mapping
	return map_dict
			
