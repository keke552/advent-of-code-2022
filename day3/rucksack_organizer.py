def main():
    filename = "contents.txt"
    print(find_rucksack_total(filename))
    print(find_badge_total(filename))

def find_error_value(line1, line2):
    error = ''
    for letter in line1:
        if line2.find(letter) >= 0:
            error = letter
            break
    return char_value(error)

def find_badge_value(line1, line2, line3):
    badge = ''
    for letter in line1:
        if line2.find(letter) >= 0 and line3.find(letter) >=0:
            badge = letter
            break
    return char_value(badge)

def char_value(error):
    value = 0
    ascii_value = ord(error)
    if ascii_value <= 90:
        value = ascii_value - 38
    else:
        value = ascii_value - 96
    return value

def find_rucksack_total(contents):
    guide = open(contents, "r")
    file_lines = guide.readlines()
    total = 0
    
    for line in file_lines:
        line.replace('\n', '')
        comp_size = len(line)/2
        line1 = line[:int(comp_size)]
        line2 = line[int(comp_size):]
        
        total = total + find_error_value(line1, line2)
    return total

def find_badge_total(contents):
    guide = open(contents, "r")
    file_lines = guide.readlines()
    total = 0
    count = 0
    for i in range(int(len(file_lines)/3)):               
        total = total + find_badge_value(file_lines[count], file_lines[count+1], file_lines[count+2])
        count = count + 3 
    return total

if __name__ == "__main__":
    main()