with open(r"Phases VI\data.txt", "r") as files:
    content = files.read()
    print(content)

with open(r"Phases VI\data.txt", "r") as file:
    line = file.readline()
    print(line)

with open(r"Phases VI\data.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    print(len(lines))
    print(lines[0])
    