class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def prepend(self,data):
        if self.__head is None:
            new_node  = Node(data)
            new_node.prev = None
            self.__head = new_node
        else:
            new_node = Node(data)
            self.__head.prev = new_node
            new_node.next = self.__head
            self.__head = new_node
            new_node.prev = None

    def append(self,data):
        if self.__head is None:
            new_node = Node(data)
            new_node.prev = None
            self.__head = new_node
        else:
            new_node = Node(data)
            tmp = self.__head
            while tmp.next:
                tmp= tmp.next
            tmp.next = new_node
            new_node.prev = tmp
            new_node.next = None

    def display(self):
        tmp = self.__head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    def insert_after(self, target_data, data):
        tmp = self.__head
        while tmp:
            if tmp.next is None and tmp.data == target_data:
                self.append(data)
                return
            elif tmp.data == target_data:
                new_node = Node(data)
                nxt = tmp.next
                tmp.next = new_node
                new_node.next = nxt
                new_node.prev = tmp
                nxt.prev=new_node
            tmp = tmp.next

    def insert_before(self, target_data, data):
        tmp = self.__head
        while tmp:
            if tmp.prev is None and tmp.data == target_data:
                self.prepend(data)
                return
            elif tmp.data == target_data:
                new_node = Node(data)
                previous = tmp.prev
                previous.next = new_node
                tmp.prev = new_node
                new_node.next = tmp
                new_node.prev = previous
            tmp = tmp.next

    def delete_node(self, target_data):
        tmp = self.__head
        while tmp:
            if tmp.data == target_data and tmp == self.__head:
                if not tmp.next:
                    tmp = None
                    self.__head = None
                    return
                else:
                    nxt = tmp.next
                    tmp.next = None
                    tmp.prev = None
                    tmp = None
                    self.__head = nxt
                    return
            elif tmp.data == target_data:
                if tmp.next:
                    nxt = tmp.next
                    previous = tmp.prev
                    previous.next = nxt
                    nxt.prev = previous
                    tmp.next = None
                    tmp.prev = None
                    tmp = nxt
                    return
                else:
                    previous = tmp.prev
                    previous.next = None
                    tmp.prev = None
                    tmp = previous  # Update tmp here
                    return
            tmp = tmp.next

linked_list = LinkedList()
#linked_list.prepend(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
#linked_list.insert_after(2, 11)
#linked_list.insert_before(2,32)
linked_list.delete_node(2)

linked_list.display()


