class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_begining(self, data) -> None:
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data) -> None:
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_values(self, dataList) -> None:
        self.head = None
        for data in dataList:
            self.insert_at_end(data)
    
    def get_length(self) -> int:
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            return Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

if __name__ == '__main__': 
    ll = LinkedList()
    ll.insert_values(["Aniket", "Remo", "Nikhil", "Gends"])
    # ll.insert_at_begineeing(3)
    # ll.insert_at_begineeing(2)
    # ll.insert_at_begineeing(9)
    # ll.insert_at_begineeing(1)
    # ll.insert_at_begineeing(0)
    # ll.insert_at_end(2)
    # ll.insert_at_end(4)
    # ll.insert_at_end(7)
    # ll.insert_at_end(1)
    # ll.insert_at_end(3)
    ll.print()
    print(ll.get_length())
    ll.remove_at(1)
    ll.insert_at("Ambhi", 1)
    ll.print()



