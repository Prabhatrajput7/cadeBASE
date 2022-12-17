# while True:
#     try:
#         age = int(input('enter age '))
#         10/age
#         raise ValueError('cut it out')
#     except ValueError:
#         print('Plz enter a number')
#     except ZeroDivisionError:
#         print('Other than Zero plz')
#     else:
#         print("thankx")
#         break
#     finally:
#         print('done')
#     print('can u hear me?')


# except block only runs one
#except(e1,e2):

"""
    raise ValueError('cut it out')
    # except ValueError:
    #     print('Plz enter a number')
    
    raise point out the below value error so to use raise remove it
"""
n= 1

# try:
#     age = int(input('enter age '))
#     10/age
#     # raise ValueError('cut it out')
# # except ValueError:
# #     print('Plz enter a number')
# except ZeroDivisionError:
#     print('Other than Zero plz')
# else:
#     print("thankx")
# finally:
#     print('done')
# print('can u hear me?')


try:
    print('try')
    # if(4/0):
    #     print('zero')
except:
    print('expect')
else:
    print('else')
print('yo')