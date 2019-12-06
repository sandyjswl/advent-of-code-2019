# A simple Python program for traversal of a linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.orbiters = []

    def add_orbiters(self, other):
        self.orbiters.append(Node(other))
        return self

    def is_data_in_orbiters(self, data):
        for each_orbit in self.orbiters:
            if data == each_orbit.data:
                return True
        return False

    def find_index(self, data):
        for i in range(len(self.orbiters)):
            if data == self.orbiters[i]:
                return i
    # Linked List class contains a Node object


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            print(temp.orbiters)
            temp = temp.next


# Code execution starts here
def is_present_inside_orbiters(data, child, linked):
    temp = linked.head
    while temp:
        if temp.is_data_in_orbiters(data):
            index = temp.find_index(data)

            next_node = Node(child)
            parent_node = temp.orbiters[index]
            parent_node.next = next_node

            # temp.orbiters.append(child)
        temp = temp.next



def list_append(linked_list, parent_data, child_data):
    temp = linked_list.head
    while temp:
        if temp.data == parent_data and temp.next is None:
            next_node = Node(child_data)
            temp.next = next_node
        else:
            is_present_inside_orbiters(parent_data, child_data, linked_list)

            # temp.orbiters.append(child)
        temp = temp.next

    return linked_list


if __name__ == '__main__':
    # Start with the empty list
    with open('day_5.txt', 'r') as f:
        content = f.readlines()
    # print(content)
    result = []
    for line in content:
        result.append(line.strip())

    first = 0
    llist = LinkedList()
    print(result)
    for orbit in result:
        parent = orbit.split(")")[0]
        child = orbit.split(")")[1]
        if first == 0:
            first = 1
            llist.head = Node(parent)
            child_node = Node(child)
            llist.head.next = child_node
        else:
            llist = list_append(llist, parent, child)
    # Link second node with the third node

    llist.printList()
