text="Ideas2IT Technology Services Private Limited"

def text_count(text):
    text_count={}
    for char in text:
        if char in text_count:
            text_count[char]+=1
        else:
            text_count[char]= 1

    print(dict(sorted(text_count.items(),key=lambda x: x[1],reverse=True)))

text_count(text)

def reverse_word(text):
    i = 0
    n = len(text)
    reverse_text = ""

    while i < n:
        if text[i] == ' ':
            reverse_text += ' '
            i += 1
            continue
        start = i
        while i < n and text[i] != ' ':
            i += 1
        for j in range(i - 1, start - 1, -1):
            reverse_text += text[j]

    print(reverse_text)

reverse_word(text)