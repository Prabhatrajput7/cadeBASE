# with open('file.txt', 'r') as f:
#     f.seek(4)
#     print(f.read())
#     print(f.seekable())

# f = open("file101.txt", "a")
# f.write("Now the file has one more line!")
# f.flush()
# f.write("...and another one!")
# f.write("anotherone")
# f.close()

# f = open("demofile2.txt", "a")
# f.truncate(20)
# f.close()
#
# #open and read the file after the truncate:
# f = open("demofile2.txt", "r")
# print(f.read())
#
f = open("demofile3.txt", "a")
f.writelines(["See you soon!\n", "Over and out."])
f.close()
#
# #open and read the file after the appending:
# f = open("demofile3.txt", "r")
# print(f.read())
