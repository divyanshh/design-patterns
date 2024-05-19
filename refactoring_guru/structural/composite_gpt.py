"""
+-------------------------+
|         Component       |
+-------------------------+
| + operation()           |
| + add(component)        |
| + remove(component)     |
| + get_child(index)      |
+-------------------------+
       /           \
      /             \
 +-------+        +-----------+
 |  Leaf |        |  Composite |
 +-------+        +-----------+
 |         operation()         |
 +-----------------------------+
 | + add(component)            |
 | + remove(component)         |
 | + get_child(index)          |
 +-----------------------------+

"""


# Component interface
class FileSystemComponent:
    def __init__(self, name):
        self.name = name

    def operation(self):
        pass

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def get_child(self, index):
        pass


# Leaf: File
class File(FileSystemComponent):
    def operation(self):
        print(f"File: {self.name}")


# Composite: Directory
class Directory(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def operation(self):
        print(f"Directory: {self.name}")

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_child(self, index):
        return self.children[index]


if __name__ == "__main__":
    # Create files
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    # Create directories
    dir1 = Directory("Documents")
    dir2 = Directory("Pictures")

    # Add files to directory 1
    dir1.add(file1)
    dir1.add(file2)

    # Add files to directory 2
    dir2.add(file3)

    # Add directory 2 to directory 1
    dir1.add(dir2)

    # Print the structure
    dir1.operation()
    for child in dir1.get_child(0):
        child.operation()
