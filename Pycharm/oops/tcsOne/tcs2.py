def data_oper(string1, string2):
    '''
    Split the string string1 with whitespace as delimiter
    Remove the words that contain characters that are not alphabets
    Remove the words whose length is less than 3
    Convert first letter of each word in to Upper case
    Store it in variable list1
    Type of list1 - List
    '''
    s1 = string1.split(' ')
    list1 = []
    for i in s1:
        if i.isalpha() and len(i)>=3:
            list1.append(i)

    list1 = [word.capitalize() for word in list1]
    '''
    Split the string string2 with whitespace as delimiter
    Remove the words that contain characters that are not alphabets
    Remove the words whose length is less than 3
    Convert first letter of each word in to Upper case
    Store it in variable list2
    Type of list2 - List
    '''

    s2 = string2.split(' ')
    list2 =[]
    for j in s2:
        if j.isalpha() and len(j)>=3:
            list2.append(j)

    list2 = [word.capitalize() for word in list2]

    '''
    Concatinate the lists list1,list2 and store it in variable list3
    Type of list3 - List
    '''

    list3 = list1+list2

    '''
    Find the count of each word in the list list3 and store it in variable count_dictionary
    Type of count_dictionary - Dictionary
    Keys have to be words
    Dictionary must be ordered based on Keys
    '''

    count_dictionary = {}.fromkeys(sorted(list3),0)
    for k in list3:
        count_dictionary[k] +=1

    '''
    Find the unique words from words of list3 and store it in variable list3_uni
    Type of list3_uni - list
    list3_uni must be sorted in ascending order
    '''

    list3_uni = sorted(list({}.fromkeys(list3)))

    '''
    Find the common words in list1,list2 and store it in variable common_tuple
    Type of common_tuple - tuple
    Words have to unique and sorted in ascending order
    If there are no common words in list1,list2 store an empty tuple
    '''
    tup = sorted(set(list1).intersection(set(list2)))
    common_tuple = tuple(tup)

    '''
    Find the words of list3 that ends with 's' and store it in variable ends_with
    Type of ends_with - tuple
    Words have to be unique and sorted in ascending order
    If there are no words in list3 that ends with 's', store an empty tuple
    '''

    lst = sorted([i for i in set(list3) if i.endswith('s')])
    ends_with = tuple(lst)

    print(list3)
    print(count_dictionary)
    print(list3_uni)
    print(common_tuple)
    print(ends_with)


if __name__ == '__main__':
    string1 = input()
    string2 = input()
    data_oper(string1, string2)