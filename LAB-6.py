# cor1=(93,54)
# cor2=('Zhetisay','Astana')
# cor3=cor1+cor2
# cor4=1,2,3,4,5,6,7
# print(cor1[0])
# print("cor3:",cor3)
# print(cor4[3:7])
# y_set={93,3}
# y_set.add(62)
# y_set.update({2,45,3})
# print(y_set)


# import random
# def fill_tuple(size, min_num, max_num):
#  return tuple(random.randint(min_num, max_num) for a in 
# range(size))
# tuple1 = fill_tuple(10,0, 5)
# tuple2 = fill_tuple(10, -5, 0)
# tuple3 = tuple1 + tuple2
# zeros_count = tuple3.count(0)
# print("1k:", tuple1)
# print("2k:", tuple2)
# print("3k:", tuple3)
# print("0 sany:", zeros_count)


# nested_tuple = (9, (3.14, (2+3j, ("Zhetisay", ()))))
# print("san : ", nested_tuple[0])
# print(“ ұзартылған", nested_tuple[1][0])
# print("күрделі сан:", nested_tuple[1][1][0])
# print("(string): ", nested_tuple[1][1][1][0])
# print("bos кортеж: ", nested_tuple[1][1][1][1])



# expenses = {}
# week_days = ['Понедельник', 'Вторник', ' Среда', 
# 'Четверг','Четверг', ' Суббота', 'Воскресенье']
# # Просим пользователя ввести расходы за каждый день недели
# for day in week_days:
#  expenses[day] = {}
#  print(f'{day} кунделикти pасходы:')
#  expenses[day]['транспортные '] = float(input('транспорт: '))
#  expenses[day]['еда'] = float(input('еда: '))
#  expenses[day]['остальное'] = float(input('остальное: '))
# # Вычисляем общую сумму за неделю
# total_expenses = 0
# for day in expenses:
#  total_expenses += sum(expenses[day].values())
#  print('\nЗа неделю:')
# for day in expenses:
#  print(f'{day}: {sum(expenses[day].values())} тг.')
# print("\n")
# print(f' расходы: {total_expenses} тг.')



students_str = input("Имена студентов: ")
students_tuple = tuple(students_str.split())

va_names = [name for name in students_tuple if "ва" and "ов" in name]
print("Фамилии с 'ва':", " ".join(va_names))

