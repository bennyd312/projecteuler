def readinput(name):
    file = open(f"{name}.txt","r")
    for line in file:
        print(line.rstrip())

    file.close()

def saveinput(name):
    text = []
    file = open(f"{name}.txt","r")

    for line in file:
        text.append(line.strip())
    
    file.close()
    return text