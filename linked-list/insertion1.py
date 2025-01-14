#inserting at the begining of the list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        
