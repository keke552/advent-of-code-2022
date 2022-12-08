def main():
    filename = "assignment.txt"
    print(find_containment_total(filename))

def find_containment_total(contents):
    guide = open(contents, "r")
    file_lines = guide.readlines()
    total = 0
    for line in file_lines:
        
    return total

if __name__ == "__main__":
    main()