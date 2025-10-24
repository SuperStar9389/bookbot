def get_word_count(text):
	return len(text.split())
def count_letters(text):
	result = {}
	for i in text:
		try:
			result[i.lower()] += 1
		except:
			result[i.lower()] = 1
	return result
def sort_by_num(data):
	return data["num"]
def organize_dict(data):
	result = []
	for i in data.keys():
		if i == " ": continue
		result.append({"char": i, "num": data[i]})
	result.sort(reverse=True, key=sort_by_num)
	return result


