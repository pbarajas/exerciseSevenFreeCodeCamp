try:
    fileName = input('Enter a file name: ')
    fileName = open(fileName)
except:
    print('Unkown File.')
    quit()
for line in fileName:
    line = line.rstrip()
    print(line.upper())
