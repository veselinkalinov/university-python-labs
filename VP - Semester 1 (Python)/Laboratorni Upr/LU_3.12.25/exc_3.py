text = str(input("Enter text: "))

with open("log.txt", "a") as f:
    f.write(text+"\n")
    print("You added text")
