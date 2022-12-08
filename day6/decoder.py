def main():
    filename = "communication.txt"
    print(find_message_start(filename))
    print(find_message_marker(filename))

def find_message_start(contents):
    guide = open(contents, "r")
    communications = guide.read()
    return find_buffer(communications) + 4

def find_message_marker(contents):
    guide = open(contents, "r")
    communications = guide.read()
    return message_marker(communications) + 14

def message_marker(letters):
    count = 0
    for letter in letters:
        arr = []
        for i in range(14):
            arr.append(letters[count+i])

        if(len(set(arr)) == len(arr)):
            return count
        else:
            count = count + 1
    return -1

def find_buffer(letters):
    count = 0
    for letter in letters:
        arr = [letter, letters[count+1], letters[count+2], letters[count+3]]
        if(len(set(arr)) == len(arr)):
            return count
        else:
            count = count + 1
    return -1

if __name__ == "__main__":
    main()