
def listInput():
    lst = []
    x = int(input("Enter the number of Element: "))

    for i in range (x):
        element = input()
        lst.append(element)
    return lst


listFile = listInput()
print('Given List: ',listFile)

listFile.sort()
print('Sorted List: ', listFile)