#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        for text in f:
            print(text, end='')


read_file(filename)
