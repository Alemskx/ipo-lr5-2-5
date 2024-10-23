str = input("Введи строку:")
count = 0
str1=str.lower()
for i in str1:
    if i =="и":
        count +=1
print("Количество букв и:",count)
