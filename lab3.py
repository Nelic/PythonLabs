import os

def FileList():
    dirname = 'C:/Users/Nelik/Desktop/4course/2sem/prog/Py'
    files = os.listdir(dirname)
    for i in files:
        if i.__contains__(".txt"):
            print(i)

def Write(fn):
    with open(fn, 'a+') as fi:
        name = input("Name and average Mark \n")
        fi.write(name + "\n")

def Read(fn):
    with open(fn, 'r') as fi:
        di = dict()
        for line in fi.readlines():
            line = line.strip().split(" ")
            di.update({ line[0] : int(line[1])})
        return di

def Display(di):
    for i in di:
        print(i + " " + str(di[i]))

def Find(fn, student):
    with open(fn, 'r') as fi:
        for line in fi.readlines():
            if line.__contains__(student):
                return line

def Sort(fn, di):
    with open(fn, 'w') as fi:
        listValues = list(di.values())
        listValues.sort()
        for j in listValues:
            for i in di:
                if di[i] == j:
                    fi.write(i + " " + str(j) + "\n")


filename = "414cs.txt"
Write(filename)