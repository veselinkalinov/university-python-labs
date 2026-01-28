n = int(input("Enter a number:"))
with open("data.txt", "r") as f:
    arg = f.read(n)
    print(arg)
