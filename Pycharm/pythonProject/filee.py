with open("myfile.txt", "r") as file:
    with open('write.txt', 'a') as file2:
        data = file.readlines()
        for line in data:
            file2.writelines('line')
        file2.write('\n')


f = open("trunk.txt", "a")
f.truncate(20)
f.close()

