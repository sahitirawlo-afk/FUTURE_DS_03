
with open("input4.1.txt","w") as f:
    f.write("Banana Apple Mango Grapes apple")

with open("input4.1.txt","r") as f:
    words=f.read().split()

words=[w.lower() for w in words]
words.sort()

with open("output4.1.txt","w") as f:
    for w in words:
        f.write(w+"\n")

print(open("output4.1.txt").read())

