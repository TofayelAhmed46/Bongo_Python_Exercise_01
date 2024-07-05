
def isLandscape(width, height):
    if width>height:
        return 'Landscape'
    else:
        return 'Portrait'
    
width  = int(input("Enter Width: "))
Height = int(input("Enter Height: "))

print(isLandscape(width, Height))