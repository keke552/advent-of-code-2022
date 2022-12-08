class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.dirs = []

    def add_file(self, f):
        self.files.append(f)

    def add_dir(self, d):
        self.dirs.append(d)

    def get_size(self):
        size = 0
        for d in self.dirs:
            size = size + d.get_size()
        for f in self.files:
            size = size + f.get_size()
        return size

class File:
    def __init__(self, name, size):
        self.name = name
        self.files = []
        self.size = size

    def get_size(self):
        return self.size

def main():
    filename = "sample_commands.txt"
    create_filesystem(filename)

def create_filesystem(contents):
    guide = open(contents, "r")
    communications = guide.read()
    f = File("hello", 12)
    d = Directory("Dir")
    d.add_file(f)
    print(d.get_size())

if __name__ == "__main__":
    main()