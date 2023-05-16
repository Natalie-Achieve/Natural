import json

def split():
    left = []
    right = []
    lines = []
    with open("original.txt", "r", encoding="utf8") as f:
        lines = f.read().split('\n')
    for line in lines:
        line = line.strip()
        if len(line) <= 0:
            left.append([""])
            right.append([""])
            continue
        slash_index = line.find('/')
        if slash_index == -1:
            left.append([line])
            right.append([""])
            continue
        splited_lines = line.split("<br>")
        inter_left = []
        inter_right = []
        for splited_line in splited_lines:
            splited_slash = splited_line.split("/")
            if len(splited_slash) > 2:
                print(f"unexpected {line}")
            inter_left.append(splited_slash[0])
            if len(splited_slash) == 2:
                inter_right.append(splited_slash[1])
            else:
                inter_right.append("")
        left.append(inter_left)
        right.append(inter_right)
    
    with open("splited_left.txt", "w", encoding="utf8") as f:
        f.write(json.dumps(left, indent=2, ensure_ascii=False))

    with open("splited_right.txt", "w", encoding="utf8") as f:
        f.write(json.dumps(right, indent=2, ensure_ascii=False))

def combine():
    left = []
    right = []
    result = ""
    with open("splited_left.txt", "r", encoding="utf8") as f:
        left = json.loads(f.read())

    with open("splited_right.txt", "r", encoding="utf8") as f:
        right = json.loads(f.read())

    if len(left) != len(right):
        raise IndexError()

    for y in range(len(left)):
        if len(left[y]) != len(right[y]):
            print(len(left[y]), len(right[y]), left[y], right[y])
            raise IndexError()
        for x in range(len(left[y])):
            
            if len(right[y][x]) == 0:
                result += left[y][x]
            else:
                result += f"{left[y][x]}/{right[y][x]}"
            result += "<br>"
        result = result[:-4]
        result += "\n"
    with open("combined.txt", "w", encoding="utf8") as f:
        f.write(result)


#split()
combine()