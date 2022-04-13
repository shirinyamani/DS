class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addnode(self,value):
        if self.next == None:
            self.next = LinkedList(value)

        else: 
            self.next.add(value)

    def __str__(self):
        return f"{self.value}" + str(self.next)


