#implement linked list with the following functions:
#display
#insert at the beginning
#insert at the end
#insert at a given position
#delete at the beginning
#delete at the end
#delete at a given position
#delete a given node
#search
#reverse
#forward and backword traversal

#start
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while pos-2:
            temp = temp.next
            pos -= 1
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_at_position(self, pos):
        if pos == 1:
            self.delete_at_beginning()
            return
        temp = self.head
        while pos-2:
            temp = temp.next
            pos -= 1
        temp.next = temp.next.next

    def delete_node(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next

    def search(self, data):
        if self.head is None:
            return
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev

    def forward_traversal(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def backward_traversal(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data)
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
#menu driven
def main():
    llist = LinkedList()
    while True:
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert at position")
        print("4. Delete at beginning")
        print("5. Delete at end")
        print("6. Delete at position")
        print("7. Delete a node")
        print("8. Search")
        print("9. Reverse")
        print("10. Forward traversal")
        print("11. Backward traversal")
        print("12. Display")
        print("13. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter the data: "))
            llist.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter the data: "))
            llist.insert_at_end(data)
        elif choice == 3:
            data = int(input("Enter the data: "))
            pos = int(input("Enter the position: "))
            llist.insert_at_position(data, pos)
        elif choice == 4:
            llist.delete_at_beginning()
        elif choice == 5:
            llist.delete_at_end()
        elif choice == 6:
            pos = int(input("Enter the position: "))
            llist.delete_at_position(pos)
        elif choice == 7:
            data = int(input("Enter the data: "))
            llist.delete_node(data)
        elif choice == 8:
            data = int(input("Enter the data: "))
            if llist.search(data):
                print("Found")
            else:
                print("Not found")
        elif choice == 9:
            llist.reverse()
        elif choice == 10:
            llist.forward_traversal()
        elif choice == 11:
            llist.backward_traversal()
        elif choice == 12:
            llist.display()
        elif choice == 13:
            break
        else:
            print("Invalid choice")
            

main()
    











            

