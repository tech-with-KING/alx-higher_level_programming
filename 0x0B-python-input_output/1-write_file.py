#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, encoding='utf-8') as f:
        f.write(text)
        print(f, end=' ')

write_file('text.txt','this is the ultimate attempt to change the world')
