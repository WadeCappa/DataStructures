class hashTable():
    def __init__(self):
        self.index = []
        self.value = []
        self.size = 7
        self.filled = 0

        self.initTable(self.index)
        self.initTable(self.value)


    def initTable(self, table):
        i = 0
        while i < len(table):
            table[i] = None
            i += 1

        while i < self.size:
            table.append(None)
            i += 1

    def resizeTable(self):
        self.filled = 0
        tempIndex = []
        tempValue = []
        self.initTable(tempIndex)
        self.initTable(tempValue)
        
        i = 0

        while i < self.size:
            tempIndex[i] = self.index[i]
            tempValue[i] = self.value[i]
            i += 1

        self.size *= 2
        self.size = self.findPrime(self.size)

        self.initTable(self.index)
        self.initTable(self.value)

        j = 0
        while j < i:
            self.insertElement(tempIndex[j], tempValue[j])
            j += 1


    def findPrime(self, number):
        correct = 1
        for x in range(2, number - 1):
            if number % x == 0:
                correct = 0
        if correct == 0:
            number = self.findPrime(number + 1)
        else:
            return(number)
        return(number)


    def insertElement(self, name, wage):

        if name == None or name == '---':
            return

        self.filled += 1
        if float(self.filled / self.size) >= 0.4:
            self.resizeTable()

        hash = self.hashElement(name)
        if self.index[hash] != None and self.index[hash] != '---':
            hash = self.probingSequence(2, name)
           
        if hash == None:
            return(None)
        else:
            self.index[hash] = name
            self.value[hash] = wage

    def probingSequence(self, offset, name):
        hash = 0
        if offset > self.size * 3:
            print("Cannot complete Operation")
            return(None)
        for x in name:
            hash += ord(x)
        hash = int(offset * hash)
        hash = int(hash % self.size)
        if self.index[hash] != None and self.index[hash] != '---':
            if self.index[hash] == name:
                return(hash)
            else:
                self.probingSequence(offset + 1, name)
        else:
            return(hash)

   
    def hashElement(self, name):
        hash = 0
        for x in name:
            hash += ord(x)
        return(hash % self.size)

    def findElement(self, name):
        hash = self.hashElement(name)
        if self.index[hash] == name:
            print("{} was found at index {} and has a value of {}".format(name, hash, self.value[hash]))
            return
        hash = self.probingSequence(2, name)

        if self.index[hash] != name:
            print("Could not be found")
            return
        else:
            print("{} was found at index {} and has a value of {}".format(name, hash, self.value[hash]))


    def removeElement(self, name):
        hash = self.hashElement(name)
        if self.index[hash] == name:
            self.index[hash] = "---"
            self.value[hash] = None
            return        
        hash = self.probingSequence(2, name)

        if self.index[hash] != name:
            print("Could not be found")
            return
        else:
            self.index[hash] = "---"
            self.value[hash] = None
            print("Removed")


    def printTable(self):
        i = 0
        while i < self.size:
            print("index {} for value {}".format(self.index[i], self.value[i]))
            i += 1
        print("")


r = hashTable()

r.insertElement("WADE CAPPA", 42)
r.insertElement("CAPPA WADE", 84)
r.insertElement("BENJAMIN FRANKLIN", 12378)
r.insertElement("MARKIUS CERLIIUS", 13215)
r.insertElement("EEEEEEEEEEEEEEEE", 13218)
r.insertElement("D E A T H", 7886)
r.insertElement("V O I D", 21387)

r.printTable()

r.findElement("V O I D")
r.findElement("rrr")
r.findElement("WADE CAPPA")

print("")

r.removeElement("V O I D")
r.removeElement("CAPPA WADE")

r.printTable()