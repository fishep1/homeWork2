#Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать!
# Реализовать свой метод
import random
Mylist = [0,1,2,3,4,5,6,7,8,9]
print ("список до перемешивания: " + str(Mylist))
for i in range(len(Mylist)-1, 0, -1):
    j = random.randint(0, i + 1)
    Mylist[i], Mylist[j] = Mylist[j], Mylist[i]
print ("список после перемешивания: " +  str(Mylist))
