import sys
def main():
    lines = []
    for line in sys.stdin:
        if line == '\n':
            break
        lines.append(line.rstrip('\n'))

    line1_name = [lines[0][:3]]
    line2_name = [lines[1][:3]]

    line1_number = [lines[0][4:]]
    line2_number = [lines[1][4:]]

    line1_number_separated = [[], [], []]
    line2_number_separated = [[], [], []]

    i = 0
    for line in line1_number:
        for ele in line:
            if ele == ' ':
                i += 1
                continue
            line1_number_separated[i].append(ele)

    i = 0
    for line in line2_number:
        for ele in line:
            if ele == ' ':
                i += 1
                continue
            line2_number_separated[i].append(ele)

    multiplier1 = line1_number_separated[0]
    if len(multiplier1) == 2:
        multiplier1 = multiplier1[0] + multiplier1[1]
    else:
        multiplier1 = multiplier1[0]
    failure1 = line1_number_separated[1]
    if len(failure1) == 2:
        failure1 = failure1[0] + failure1[1]
    else:
        failure1 = failure1[0]
    repair1 = line1_number_separated[2]
    if len(repair1) == 2:
        repair1 = repair1[0] + repair1[1]
    else:
        repair1 = repair1[0]

    multiplier2 = line2_number_separated[0]
    if len(multiplier2) == 2:
        multiplier2 = multiplier2[0] + multiplier2[1]
    else:
        multiplier2 = multiplier2[0]
    failure2 = line2_number_separated[1]
    if len(failure2) == 2:
        failure2 = failure2[0] + failure2[1]
    else:
        failure2 = failure2[0]
    repair2 = line2_number_separated[2]
    if len(repair2) == 2:
        repair2 = repair2[0] + repair2[1]
    else:
        repair2 = repair2[0]

    if int(multiplier1) > 20 or int(failure1) > 20 or int(repair1) > 20 or int(multiplier2) > 20 or int(failure2) > 20 or int(repair2) > 20:
        print("nombre supérieur a 20")
        return 84
    hour1 = int(multiplier1) * (int(failure1) + int(repair1))
    hour2 = int(multiplier2) * (int(failure2) + int(repair2))

    if hour1 < hour2:
        print(line1_name)
    else:
        print(line2_name)

if __name__ == "__main__":
    main()