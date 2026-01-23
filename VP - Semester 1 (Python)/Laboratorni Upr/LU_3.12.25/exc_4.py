py = []

with open("data.txt", "r") as f:
    for line in f:
        if "Python" in line:
            print(line.strip())
