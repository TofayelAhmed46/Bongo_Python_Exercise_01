
def listInput():
    lst = []
    x = int(input("Enter the number of Element: "))

    for i in range (x):
        element = int(input())
        lst.append(element)
    return lst


listFile = listInput()
print(listFile)

index = int(input("Enter the value want to search: "))
if index in listFile:
    print (f'The index of {index} is : ',listFile.index(index))
else:
    print('The value is not in list.')