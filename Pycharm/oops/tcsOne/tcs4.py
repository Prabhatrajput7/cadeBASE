import ast

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Create class Person
Initialize the class with first_name,last_name
Create a member function "Name" that returns the Full name of the person
Type of first_name - str
Type of last_name - str
'''


class Person:

    def __init__(self,fist_name,last_name):
        self.fist_name = fist_name
        self.last_name = last_name

    def Name(self):
        return f'{self.fist_name} {self.last_name}'

'''
Create another class Student that inherits the proporties of class Person
Initialize the class variable "count" with value 0
Initialize the class with fist_name,last_name,rollno,mark1,mark2
class variable count should have the number of students
Create a member function "GetStudent" that returns the fullname,rollno,total marks seperated by commas
Type of first_name - str
Type of last_name -str
Type of rollno - int
Type of mark1 - int
Type of mark2 - int
'''


class Student(Person):

    count = 0

    def __init__(self, fist_name, last_name,rollno, mark1, mark2):
        super().__init__(fist_name, last_name)
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2
        Student.count +=1

    def GetStudent(self):
        return f'{Person.Name(self)},{self.rollno},{int(self.mark1)+int(self.mark2)}'


'''
Create another class Staff that inherits the proporties of class Person
Initialize the class variable "count" with value 0
Initialize the class with fist_name,last_name,staffnum
class variable count should have the number of staffs
Create a member function "GetStaff" that returns the fullname and staffnumber seperated by comma
Type of first_name - str
Type of last_name -str
Type of staffnum - int
'''


class Staff(Person):
    count = 0

    def __init__(self, fist_name, last_name, staffnum):
        super().__init__(fist_name, last_name)
        self.staffnum = staffnum
        Staff.count +=1

    def GetStaff(self):
        return f'{Person.Name(self)},{int(self.staffnum)}'




if __name__ == '__main__':
    students = ast.literal_eval(input())
    staff = ast.literal_eval(input())
    t = []
    s = []
    for i in staff:
        t.append(Staff(i[0], i[1], i[2]))
    for i in students:
        s.append(Student(i[0], i[1], i[2], i[3], i[4]))


    for i in t:
        print(i)
        print(i.GetStaff())
    print(Staff.count)

    for i in s:
        print(i.GetStudent())
    print(Student.count)

"""
[["Joseph", "Paul",1, 100,30],["Mathew","John",2,100,0]]
[["Abin", "Joy", 1832],["Liza","Clare",1003]]

Abin Joy,1832
Liza Clare,1003
2
Joseph Paul,1,130
Mathew John,2,100
2
"""