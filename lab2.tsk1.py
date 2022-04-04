lists = [1, 46, 93, 19, 102, 81, 3, 9, -41, 0, 19, -100, -100]

# def Quick_sort(numbers, low, high):
# 	if low < high:
# 		pivot = Prepare(numbers, low, high)
# 		Quick_sort(numbers, low, pivot - 1)
# 		Quick_sort(numbers, pivot + 1, high)
#
# def Prepare(numbers, low, high):
# 	pivot = numbers[high]
# 	item = low - 1
# 	for i in range(low, high):
# 		if numbers[i] <= pivot:
# 			item = item + 1
# 			(numbers[item], numbers[i]) = (numbers[i], numbers[item])
# 	(numbers[item + 1], numbers[high]) = (numbers[high], numbers[item + 1])
# 	return item + 1
#
# Quick_sort(lists,0,len(lists)-1)
# for i in lists:
#     print(i)

# def FindByValue (list, value):
# 	for i in list:
# 		return True

# def Sequence (list, x = 0, y = 0, i = 0):
# 	for i in range(len(list)-1):
# 		if list[i] > list[i+1]:
# 			y = i+1
# 		if (x != y) and (x != y-1):
# 			print(list[x:y])
# 		x = y
# Sequence(lists)

# def FirstFiveMin (mass):
# 	li = sorted(mass)
# 	li = li[0:5]
# 	return li
#
# def FirstFiveMax (mass):
# 	li = sorted(mass)
# 	li = li[len(li)-5:len(li)]
# 	return li
#
# a = FirstFiveMin(lists)
# for i in a:
# 	print(i)

# def Avg (li):
# 	sum = 0
# 	for i in li:
# 		sum += i
# 	return sum / len(li)

# def ToList(li):
# 	print(list(set(li)))
# ToList(lists)


