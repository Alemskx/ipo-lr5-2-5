str = input("Введи строку:")
kolvo = 0
str1=str.lower()
for i in str1:
    if i =="и":
        kolvo +=1
print("Количество букв и:",kolvo)