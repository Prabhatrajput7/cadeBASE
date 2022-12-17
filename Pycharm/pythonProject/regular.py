import re

string = 'harry potter and the deathly and hollows part1/2'
string2 = 'praa_@hackerrank.com'
#patter = re.compile('and')
patter = re.compile(r"([a-zA-Z]).([a])")#. means anything
patter2 = re.compile(r"^[a-z]{1,6}0?_?0?[0-9]{0,4}@hackerrank\.com$")
#a = patter.search(string)
#a = re.search('and',string)
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())
# print(patter.findall(string))
# print(patter.fullmatch(string)) #both string should be same
# print(patter.match(string)) #matches both sring from starting and doesn't matter what come afterward when match completes

if re.fullmatch(patter2,string2):
    print('yes')
else:
    print("no")