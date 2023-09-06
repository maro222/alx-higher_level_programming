#!/usr/bin/python3
def text_indentation(text):
    temp = ""
    for ch in text:
        temp += ch
        if ch in ['.', '?', ':']:
            print(f"{temp.strip()}\n")
            temp = ""
    print(temp.strip(), end='')
