#The largest element
#Statement
#Given a list of numbers.
#Determine the element in the list with the largest value.
#Print the value of the largest element and then the index number.
#If the highest element is not unique, print the index of the first instance.

#Задача «Наибольший элемент»
#Условие
#Дан список чисел. Выведите значение наибольшего элемента в списке,
#а затем индекс этого элемента в списке.
#Если наибольших элементов несколько, выведите индекс первого из них.

a = [int(i) for i in input().split()]
largest_pos = 0
for i in range(1, len(a)):
    if a[i] > a[largest_pos]:
        largest_pos = i
print(a[largest_pos], largest_pos)
