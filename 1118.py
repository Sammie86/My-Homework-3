print('Iyai Bassey 1937369')  # This is my name and PSID
prompt = " "
line = input(prompt).split()
positive = []
for i in line:
    if int(i) > 0:
        positive.append(int(i))

sortedlist = sorted(positive)
for i in sortedlist:
    print(i,end=" ")