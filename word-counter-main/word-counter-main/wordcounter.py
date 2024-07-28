sentence = input("enter the sentense")

sentence = sentence.replace(',', '').lower().split()
wc = {}

for word in sentence:
    if word in wc.keys():
        wc[word] += 1
    else:
        wc[word] = 1

print(wc)