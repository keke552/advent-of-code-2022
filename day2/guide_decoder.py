def main():
    guide = open("guide.txt", "r")
    file_lines = guide.readlines()
    total = 0

    for line in file_lines:
        print(line)
        if line[2] == 'X':
            round_sum = 0
            if line[0] == 'A':
                round_sum += 3
            elif line[0] == 'B':
                round_sum += 1
            else:
                round_sum += 2
        elif line[2] == 'Y':
            round_sum = 3
            if line[0] == 'A':
                round_sum += 1
            elif line[0] == 'B':
                round_sum += 2
            else:
                round_sum += 3
        else:
            round_sum = 6
            if line[0] == 'A':
                round_sum += 2
            elif line[0] == 'B':
                round_sum += 3
            else:
                round_sum += 1

        total += round_sum
        print(round_sum)

    print(total)

if __name__ == "__main__":
    main()