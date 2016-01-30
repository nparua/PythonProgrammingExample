def insertion_sort(input_array):
	for k in range(1, len(input_array)):
		cur = input_array[k]
		j = k
		while j>0 and input_array[j-1] > cur:
			input_array[j] = input_array[j-1]
			j-=1
		input_array[j] = cur
	return input_array

def merge_sort(m):
	from heapq import merge
	if len(m) <= 1:
		return m

	middle = len(m)//2
	left = m[:middle]
	right = m[middle:]

	left = merge_sort(left)
	right = merge_sort(right)

	return list(merge(left, right))
