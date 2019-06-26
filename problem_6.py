class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        node = self.tail
        node.next = Node(value)
        self.tail = node.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def turn_string_to_list(self, data):
        for x in data:
            self.append(x)

    def search(self, value):
        if self.head is None:
            return False
        else:
            node = self.head
            while node.next:
                if node.value == value:
                    return True
                else:
                    node = node.next
            return False

    def remove_duplicates(self):
        # I know this can be easily done by set, but I thought I should do linked list with nodes?
        node = self.head
        reference = LinkedList()
        while node:
            if reference is None:
                reference.head.value = node.value
            else:
                if reference.search(node.value):
                    node = node.next
                else:
                    reference.append(node.value)
                    node = node.next
        return reference


def union(llist_1, llist_2):
    # Your Solution Here
    node1 = llist_1.head
    node2 = llist_2.head
    append_this = LinkedList()
    while node1:
        append_this.append(node1.value)
        node1 = node1.next
    while node2:
        append_this.append(node2.value)
        node2 = node2.next
    append_this = append_this.remove_duplicates()
    return append_this

def intersection(llist_1, llist_2):
    # Your Solution Here
    llist_1 = llist_1.remove_duplicates()
    llist_2 = llist_2.remove_duplicates()
    if llist_1.head is None or llist_2.head is None:
        return 'Nothing intersects'
    node1 = llist_1.head
    node2 = llist_2.head
    intersect = LinkedList()
    while node1:
        while node2:
            if node1.value != node2.value:
                if node2.next is None:
                    if node1.next is None:
                        if intersect.head is None:
                            intersect.append('Nothing intersects')
                            return intersect
                        else:
                            return intersect
                    else:
                        node1 = node1.next
                        node2 = llist_2.head
                else:
                    node2 = node2.next
            else:
                intersect.append(node1.value)
                node2 = llist_2.head  # reset to beginning
                if node1.next is None:
                    return intersect
                else:
                    node1 = node1.next
                continue
    return intersect

#Test Case 1:
#Union -> Hi cat!dog?
#Intersection -> Hi
string1 = 'Hi cat!'
string2 = 'Hi dog?'
s1 = LinkedList()
s2 = LinkedList()
sum = LinkedList()
s1.turn_string_to_list(string1)
s2.turn_string_to_list(string2)
print(str(union(s1, s2)))
print(str(intersection(s1,s2)))

#Test case 2
#Union -> 3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11
#Intersection -> 4, 6, 21
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

#Test case 3
#Union -> 3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21
#Intersection -> Nothing!

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

#Test case 4
#Union -> Was itcroIsw?H
#Intersection -> 'as itc'
string1 = 'Was it a car or a cat I saw?'
string2 = 'Hi it is a cat'
s1 = LinkedList()
s2 = LinkedList()
sum = LinkedList()
s1.turn_string_to_list(string1)
s2.turn_string_to_list(string2)
print(str(union(s1, s2)))
print(str(intersection(s1,s2)))

#Test case 5
#Union -> abcde
#Intersection -> Nothing intersects
string1 = 'abcde'
string2 = ''
s1 = LinkedList()
s2 = LinkedList()
sum = LinkedList()
s1.turn_string_to_list(string1)
s2.turn_string_to_list(string2)
print(str(union(s1, s2)))
print(str(intersection(s1,s2)))

