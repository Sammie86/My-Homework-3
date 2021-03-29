print('Iyai Bassey 1937369') #This is my name and PSID
words = input().split()
for word in words:
    count = 0
    for w in words:
        if w == word:
            count += 1
    print(word, count)