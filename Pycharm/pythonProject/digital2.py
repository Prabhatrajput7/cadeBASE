def bar_code(bar):
    s = 0
    for i in bar:
        if i.isdigit():
            s+=int(i)
        else:
            ch = int(max(str(ord(i))))
            s += ch
    return s
if __name__ == '__main__':
    bar = input()
    print(bar_code(bar))
