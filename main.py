import os

class Style:
  def __init__(self, name, startLine, endLine):
    self.name = name
    self.startLine = startLine
    self.endLine = endLine

directories = next(os.walk('.'))[1]

'''os.walk(directories[0])'''

count=1
startFlag = 0
endFlag = 0
cStyleName=''
cStyleStartLine=0
cStyleEndLine=0

restart = True
quitd = True
''' for dirname in directories:
    if os.path.isdir(dirname): '''
while restart:
    ''' print dirname '''
    ''' f=open(dirname + "/styles.js", 'r') '''
    f=open("./styles.js", 'r')
    fl=f.readlines()
    
    quitd = True
    count=1
    startFlag = 0 
    endFlag = 0
    cStyleName=''
    cStyleStartLine=0
    cStyleEndLine=0
    for x in fl:
        array=x.split(': {', 1)
        print array
        if len(array) == 2 and startFlag == 0:
            array[0]=array[0].strip()
            #print array[0]
            cStyleName=array[0]
            cStyleStartLine=count
            startFlag=1
        if len(array) == 1 and startFlag == 1:
            array[0]=array[0].strip()
            if array[0] == '},':
                #print 'end ' + array[0]
                cStyleEndLine=count
                endFlag=1
        if startFlag == 1 and endFlag == 1:
            item = Style(cStyleName, cStyleStartLine, cStyleEndLine)
            startFlag = 0
            endFlag = 0
            with open('./index.js') as a:
                if not 'styles.' + item.name in a.read():
                    s=1
                    with open("./styles.js", "r") as f:
                        lines = f.readlines()
                    with open("./styles.js", "w") as f:
                        for line in lines:
                            if not (s == int(item.startLine) or (s > int(item.startLine) and s < int(item.endLine)) or s == int(item.endLine)):
                                f.write(line)
                            s=s+1
                    quitd = False
                    a.close()
                    f.close()
                    print item.name + ' in ' + './styles.js' + ' is removed'
                    break
            f.close()
            a.close()
            del item
        count=count+1
    if quitd == True:
        restart = False
f.close()
f.close()

