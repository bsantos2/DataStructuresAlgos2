import os

def find_files(root = ".", extension = ".c"):
    #Default extension is blank, it follows instruction of ".c" per project
    #Root default is "." in case user forgets input
    subdirectories = list()
    c_files = list()
    y = extension.find(".")
    if y == -1:
        extension = "." + extension
    filtered_files = recursive_os_walk(root, subdirectories, c_files, extension)
    print(filtered_files)

def recursive_os_walk(root, subdirectories, c_files, extension):
    if os.path.exists(root):
        fileList = os.listdir(root)
        for x in fileList:
            x = root + "/" + x
            if os.path.isdir(x):
                subdirectories.append(x)
                recursive_os_walk(x, subdirectories, c_files, extension)
            elif x.endswith(extension):
                c_files.append(x)
        return c_files
    else:
        return "Directory does not exist"

#Test Case 1
print("Test Case #1")
x = (find_files("."))
print(x)
#This prints the c files, as specified from the example folder from the project write up
#Expected output = { ./testdir/subdir1/a.c,
#                    ./testdir/subdir3/subsubdir1/b.c,
#                    ./testdir/subdir5/a.c,
#                    ./testdir/t1.c

#Test Case 2
print("Test Case #2")
x = (find_files(".."))
print(x)
#The solution is same as above, except it is from perspective of the parent of this directory

#Test Case 3
print("Test Case #3")
x = (find_files("../junk"))
print(x)
#Since the path does not exist, It returns "Directory does not exist"

#Test Case 4
print("Test Case #4")
x = (find_files())
print(x)
#Since the path does not exist, It returns "Directory does not exist"
#Should be same as test case # 1