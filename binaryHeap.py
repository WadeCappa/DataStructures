class binaryHeap():

    def __init__(self):
        self.index = 0
        self.value = []
 
    def push(self, num):
        self.value.append(num)
        self.sortNew()

    def sortNew(self):
        tempIndex = self.index
        if tempIndex == 0:
            self.index += 1
            return( "complete" )
        else:
            while self.value[tempIndex] < self.value[ int(( tempIndex - 1 ) / 2) ]:
                temp = self.value[ int(( tempIndex - 1 ) / 2) ]
                self.value[ int(( tempIndex - 1 ) / 2) ] = self.value[tempIndex]
                self.value[tempIndex] = temp
                tempIndex = int(( tempIndex - 1 ) / 2) 
            self.index += 1

    def pullNum(self, num):
        i = 0
        while i < self.index:
            if self.value[i] == num:
                self.index -= 1
                temp = self.value[self.index]
                self.value[self.index] = self.value[i]
                self.value[i] = temp
                self.value.pop()
                self.trickleDown(i)
            i += 1



    def pullTop(self):
        self.index -= 1
        tempIndex = self.index
        temp = self.value[self.index]
        self.value[self.index] = self.value[0]
        self.value[0] = temp
        self.value.pop()
        self.trickleDown(0)


    def trickleDown(self, index):
        tempIndex = index
        while int(( tempIndex + 1 ) * 2) < self.index:
            if self.value[ int(( tempIndex + 1 ) * 2) ] < self.value[ int((( tempIndex + 1 ) * 2) - 1) ]:
                if self.value[tempIndex] > self.value[ int(( tempIndex + 1 ) * 2) ]:
                    specialVal = 0
                else:
                    return(0)
            else:
                if self.value[tempIndex] > self.value[ int((( tempIndex + 1 ) * 2) - 1) ]:
                    specialVal = 1
                else:
                    return(0)
            temp = self.value[ int((( tempIndex + 1 ) * 2) - specialVal) ]
            self.value[ int((( tempIndex + 1 ) * 2) - specialVal) ] = self.value[tempIndex]
            self.value[tempIndex] = temp
            tempIndex = int((( tempIndex + 1 ) * 2) - specialVal) 




    def displayHeap(self):
        print("Index Value: ", self.index)
        for x in self.value:
            print(x)

            
                




newHeap = binaryHeap()
newHeap.push(12)
newHeap.push(4)
newHeap.push(1)
newHeap.push(11)
newHeap.push(6)
newHeap.push(14)
newHeap.push(0)
newHeap.push(8)
newHeap.push(2)
newHeap.push(3)

newHeap.displayHeap()

print("------- REMOVE TOP --------")

newHeap.pullTop()
newHeap.displayHeap()

