class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(3)
    ll.insert_at_end(6)
    ll.print()



