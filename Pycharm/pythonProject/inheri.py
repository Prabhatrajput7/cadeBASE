# class Ubi:
#     def sign(self):
#         print('login')
# class Siege(Ubi):
#     def __init__(self,username,passw):
#         self.username = username
#         self.passw = passw
#     def displayy(self):
#         print(f'Your username and password: {self.username} & {self.passw}')
#
# s1 = Siege('l1','**')
# print(s1.sign())
# print(isinstance(s1,Ubi))

# class PPT:
#     pass
#
# p = PPT()
# p_info = {'first': 'MS2007','sec':'MS2010'}
# for i,j in p_info.items():
#     setattr(p,i,j)
# for i in p_info.keys():
#     print(getattr(p,i))


# class Employee:
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay, extra):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#         self.extra = extra
#         print('*')
#
#     def fullname(self):
#         return '{} {} {}'.format(self.first, self.last, self.extra)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
#
#
# class Developer(Employee):
#     raise_amt = 1.10
#
#     def __init__(self, first, last, pay, extra, prog_lang):
#         super().__init__(first, last, pay, extra)
#         self.prog_lang = prog_lang
#
#
# class Manager(Employee):
#     def __init__(self, first, last, pay, extra, employees=None):
#         super().__init__(first, last, pay, extra)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#
#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#
#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())


#dev_1 = Developer('Corey', 'Schafer', 50000, 'ex' , 'Python')
# dev_2 = Developer('Test', 'Employee', 60000, 'Java')

#mgr_1 = Manager('Sue', 'Smith', 90000,'exx', [dev_1])
# mgr_2 = Manager('Sue', 'Smith', 90000, [dev_2])
# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_2)

#mgr_1.print_emps()

# mgr_2.print_emps()

# class Pets:
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals
#     def walk(self):
#         for animal in self.animals:
#             print(animal.breedy())
# class Cat:
#     is_lazy = True
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def wlk(self):
#         return f'{self.name} is just walking around'
#
# class Catty:
#     def __init__(self,breed):
#         self.breed = breed
#     def breedy(self):
#         return f'{self.breed} is your breed'
# animal_1 = Cat(name="Simon", age=14)
# animal_2 = Cat(name="Sally", age=15)
# animal_3 = Cat(name="Micheal", age=11)
# my_cats = [animal_1, animal_2, animal_3]
# my_cat = Catty('kali')
# my_cat2 = Catty('safed')
# my_cat3 = [my_cat,my_cat2]
# my_pets = Pets(my_cat3)
# my_pets.walk()


# class Pets:
#   animalss = []
#
#   def __init__(self, animals):
#     self.animals = animals
#
#   def walk(self):
#     for i in self.animals:
#       print(i.walk())
#
# class Cat:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def walk(self):
#     return f'{self.name} is just walking around'
#
# class Simon(Cat):
#   def sing(self, sounds):
#     return f'{sounds}'
#
# animal_1 = Simon(name="test", age=14)
# my_cats = [animal_1]
# my_pets = Pets(my_cats)
# my_pets.walk()
