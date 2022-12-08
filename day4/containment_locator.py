def main():
    filename = "assignment.txt"
    print(find_containment_total(filename))
    print(find_overlap_total(filename))

def find_containment_total(contents):
    guide = open(contents, "r")
    file_lines = guide.readlines()
    total = 0
    for line in file_lines:
        assignments = find_assignments(line)
        as1 = convert_to_arr(assignments[0])
        as2 = convert_to_arr(assignments[1])
        if contains(as1, as2):
            total = total + 1
    return total

def find_overlap_total(contents):
    guide = open(contents, "r")
    file_lines = guide.readlines()
    total = 0
    for line in file_lines:
        assignments = find_assignments(line)
        as1 = convert_to_arr(assignments[0])
        as2 = convert_to_arr(assignments[1])
        if overlaps(as1, as2):
            total = total + 1
    return total

def overlaps(as1, as2):
    for x in as1:
        if x in as2:
            return True

    for x in as2:
        if x in as1:
            return True

    return False

def find_assignments(line):
    return line.split(',')

def convert_to_arr(assignment):
    range_arr = assignment.split('-')
    start = int(range_arr[0])
    end = int(range_arr[1])
    arr = []
    for i in range(start, end+1):
        arr.append(i)
    return set(arr)

def contains(as1, as2):
    if as1.issubset(as2) or as2.issubset(as1):
        return True

if __name__ == "__main__":
    main()