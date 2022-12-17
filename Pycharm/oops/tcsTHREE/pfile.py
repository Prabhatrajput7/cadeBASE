import pickle
import pprint

def storeData():
    Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak',
             'age': 21, 'pay': 40000}
    Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak',
               'age': 50, 'pay': 50000}
    db = {}
    db['Omkar'] = Omkar
    db['Jagdish'] = Jagdish
    print(db)
    with open('examplePickle.pickle', 'ab') as p:
        pickle.dump(db, p)

def loadData():
    with open('examplePickle.pickle', 'rb') as p:
        db = pickle.load(p)
    for keys in db:
        print(keys, '=>', db[keys])

if __name__ == '__main__':
    storeData()
    loadData()