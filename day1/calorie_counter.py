def main():
    calorie_file = open("calories.txt", "r")
    file_lines = calorie_file.readlines()
    cal_sum = 0
    max_sum = 0
    max2 = 0
    max3 = 0
    for line in file_lines:
        if line != '' and line != '\n':
            cal_sum += int(line)
        else:
            if cal_sum >= max_sum:
                max3 = max2
                max2 = max_sum
                max_sum = cal_sum
            elif cal_sum >= max2:
                max3 = max2
                max2 = cal_sum
            elif cal_sum >= max3:
                max3 = cal_sum
            cal_sum = 0
    if cal_sum >= max_sum:
        max3 = max2
        max2 = max_sum
        max_sum = cal_sum
    elif cal_sum >= max2:
        max3 = max2
        max2 = cal_sum
    elif cal_sum >= max3:
        max3 = cal_sum
    print("Highest: ", max_sum)
    print("Second highest: ", max2)
    print("Third highest: ", max3)
    total = max_sum + max2 + max3
    print("Total: ", total)

if __name__ == "__main__":
    main()