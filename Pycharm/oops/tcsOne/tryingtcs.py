import ast
# def list_oper(list1,list2):
#     sq = [i*i for i in list1]
#     cube = [i**3 for i in list2]
#     if (set(sq).intersection(set(list2))) and (set(cube).intersection(set(list2))):
#         return f'True'
#
#
# if __name__=='__main__':
#     list1 = ast.literal_eval(input())
#     list2 = ast.literal_eval(input())
#     print(list_oper(list1,list2))

# def amstrong(num1,num2):
#     lst =[]
#     for i in range(num1,num2):
#         if sum(int(i)**3 for i in str(i)) == i and i>100:
#             lst.append(i)
#     print(lst)
#
# amstrong(0,200)

#
# def string_reverse(string2):
#     s1 = string2.split(' ')
#     s1 = [i[::-1] for i in s1]
#     return ' '.join(s1)
#
# string2 = input()
# print(string_reverse(string2))


# def string_oper(string1):
#     s1,s2 = string1.split(),[]
#     [s2.append(i) for i in s1 for j in i if i.count(j)>1]
#     [s1.remove(i) for i in s1 if i in s2]
#     return ' '.join(s1)
#
#
#
# string1 = input()
# print(string_oper(string1))


# s = '2'
# p = '5'
# print(int(s)+int(p))

students = ast.literal_eval(input())
staff = ast.literal_eval(input())
print(students,staff)
# t = []
# s = []
# for i in staff:
#     t.append(Staff(i[0], i[1], i[2]))
# for i in students:
#     s.append(Student(i[0], i[1], i[2], i[3], i[4]))
# for i in t:
#     print(i.GetStaff())
#     print(Staff.count)
# for i in s:
#     print(i.GetStudent())
#     print(Student.count)