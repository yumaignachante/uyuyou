"""day 2"""
def main():
    """Atbash Cipher"""
    xxx = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    zzz = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    qqq = xxx.lower()
    ooo = zzz.lower()
    ccc = ""
    yyy = input()
    for i in yyy:
        if i.isupper():
            aaa = xxx.find(i)
            ccc += zzz[aaa]
        elif i.islower():
            bbb = qqq.find(i)
            ccc += ooo[bbb]
        else:
            ccc += i
    print(ccc)
main()
