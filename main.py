my_dict = {"Алексей" : 1996 , "Павел" : 1991, "Вова" : 1993}
print("Все переменные словаря: ", my_dict)
print("Вывести значение из словаря: ", my_dict["Алексей"])
print("Не существующее значение: ", my_dict.get("Алена"))
my_dict.update({"Саша" : 1997 ,
                "Лера" : 2002 ,
                "Вика" : 2000})
print("Обновленный словарь: ", my_dict)
del my_dict["Павел"], my_dict[ "Алексей"]
print("Удаление из словаря: ", my_dict)

my_set = [20 , 20, 25, 30 , "Город" , "Город", "Страна", True]
my_set = set(my_set)
print("Множество: ", my_set)
my_set.add(489)
my_set.add((1,2,3))
my_set.discard(1)
print("Обновленное множество: ", my_set)

