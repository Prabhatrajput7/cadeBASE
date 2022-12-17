# def encode(message):
#     encoded_message = ""
#     i = 0
#
#     while (i <= len(message) - 1):
#         count = 1
#         ch = message[i]
#         j = i
#         while (j < len(message) - 1):
#             if (message[j] == message[j + 1]):
#                 count = count + 1
#                 j = j + 1
#             else:
#                 break
#         encoded_message = encoded_message + ch + str(count)
#         i = j + 1
#     return encoded_message

s = 'AABBCCDD'
i = 0
news = ''
while(i<len(s)-1):
    ch = s[i]
    c = 1
    j = i
    while(j<len(s)-1):
        if s[j] == s[j+1]:
            c+=1
            j+=1
        else:
            break
    news += ch + str(c)
    i = j + 1
print(news)
# from basicss import asum
#
# print(asum(2,3))

# Provide different values for message and test your program
# encoded_message = encode("AABBCC")
# print(encoded_message)

# def cuber(n):
#     # cu =  f'{8},{12*(n-2)},{6*(n-2)**2},{(n-2)**3}'
#     l1 = [8,12*(n-2),6*(n-2)**2,(n-2)**3]
#     return l1
# n = 6
# cube = cuber(n)
# print(cube)

from collections import OrderedDict
# def runLengthEncoding(input):
#     dict = {}.fromkeys(input, 0)
#     for ch in input:
#         dict[ch] += 1
#         print(dict)
#     output = ''
#     for key, value in dict.items():
#         output = output + key + str(value)
#     return output
# # Driver function
# if __name__ == "__main__":
#     input = "ABBBBCCCCCCCCAB"
#     print(runLengthEncoding(input))

# from collections import defaultdict
#
#
# a = defaultdict(lambda :0)
# a['a'] = 10
# print(a['b'])

from collections import Counter

# s = "ABBBBCCCCCCCCAB"
# d = {}.fromkeys(s,0)
# for i in s:
#     if i in d:
#         d[i]+=1
# print(d)
# st =""
# for i in d:
#     st = st + i + str(d[i])
#     print(st)
# print(st)


# from collections import Counter
# s = "AAAABCCCCCCCCAB"
# print(sorted(Counter(s).items(), key=lambda x:x[1]))


# import os
# fol = 'vig'
# curr = os.getcwd()
# os.makedirs(fol)





