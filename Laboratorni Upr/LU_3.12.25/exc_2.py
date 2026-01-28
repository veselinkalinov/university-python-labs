num_lines = 0
num_words = 0
num_charts = 0

with open("hello.txt", "r") as f:
    for line in f:
        num_lines += 1
        words = line.split()
        num_words += len(words)
        num_charts += len(line)

print(
    f"Number of lines: {num_lines}\nNumber of words: {num_words}\nNumber of charts: {num_charts}")
