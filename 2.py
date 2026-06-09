# Step 1: Create the input file
with open("input4.2.txt","w") as f:
    f.write("Hello World\nPython Programming\nEEE Department")

# Step 2: Read the file and reverse each line
with open("input4.2.txt","r") as f:
    for line in f:
        print(line.strip()[::-1])