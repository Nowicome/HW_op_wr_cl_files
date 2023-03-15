def reader(name):
    with open(name, encoding="utf-8") as file:
        k = []
        count = 0
        for line in file:
            count += 1
            k.append(line.strip())
        k.append(count)
    return k


if __name__ == "__main__":
    hoarder = {}

    hoarder["1.txt"] = reader("HW_folder/1.txt")
    hoarder["2.txt"] = reader("HW_folder/2.txt")
    hoarder["3.txt"] = reader("HW_folder/3.txt")

    file = open("HW_folder/4.txt", "a", encoding="utf-8")
    for key, val in sorted(hoarder.items(), key=lambda val: val[-1], reverse=True):
        file.write(key + "\n")
        file.write(str(val[-1]) + "\n")
        for i in range(len(val)-1):
            file.write(val[i] + "\n")
    file.close()
