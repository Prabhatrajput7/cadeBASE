import pickle
import pytest
from faker import  Faker
ff =Faker()
def storeData():
    lst =[ff.name() for i in range(100)]
    with open('custom.pickle', 'ab') as p:
        pickle.dump(lst, p)

def loadData():
    with open('custom.pickle', 'rb') as p:
        db = pickle.load(p)
        print(db)

if __name__ == '__main__':
    # storeData()
    loadData()