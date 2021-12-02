increaseCount, decreaseCount, nochangeCount = 0,0,0
bufferSize = 4
windowSize = bufferSize-1
buffer=[]
A,B = 0,0
for i in range(0, bufferSize):
    buffer.append(-1)
with open("data.dat") as file:
    for line in file:
        line = int(line.strip())
        i = 0
        while bufferSize-i > 0:
            buffer[(bufferSize-i)-1] = buffer[(bufferSize-i)-2]
            i+=1
        buffer[0] = line
        if buffer[windowSize] > -1:
            A,B = 0,0
            aRange,bRange = range(1,bufferSize), range(0,windowSize)
            for j in aRange:
                A = A + buffer[j]
            for j in bRange:
                B = B + buffer[j]
            if (A) < (B):
                increaseCount+=1
            else:
                if (A) > (B):
                    decreaseCount+=1
                else:
                    nochangeCount+=1
print("Increased: " + str(increaseCount))
print("Decreased: " + str(decreaseCount))
print("No change: " + str(nochangeCount))
