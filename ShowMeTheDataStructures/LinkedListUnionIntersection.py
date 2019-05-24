class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def __eq__(self, other):
        if self.size() != other.size():
            return False

        cur_head_self = self.head
        cur_head_other = self.head
        while cur_head_self:
            if cur_head_self.value != cur_head_other.value:
                return False

            cur_head_self = cur_head_self.next
            cur_head_other = cur_head_other.next

        return True

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = Node(value)
        node.next = self.head
        self.head = node
        
        self.num_elements += 1

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

        self.num_elements += 1

    def size(self):
        return self.num_elements

def union(llist_1, llist_2):
    # Your Solution Here
    found_elements = set()
    union_list = LinkedList()
    union_lists(llist_1, union_list, found_elements)
    union_lists(llist_2, union_list, found_elements)

    return union_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    found_elements = set()
    intersect_list = LinkedList()
    build_intersect_set(llist_1, found_elements)
    intersect_lists(llist_2, intersect_list, found_elements)

    return intersect_list

def union_lists(input_list, output_list, found_elements):
    head = input_list.head
    while head:
        if head.value not in found_elements:
            output_list.prepend(head.value)
        found_elements.add(head.value)
        head = head.next

def build_intersect_set(input_list, found_elements):
    head = input_list.head
    while head:
        found_elements.add(head.value)
        head = head.next

def intersect_lists(input_list, output_list, found_elements):
    already_inserted_elements = set()
    head = input_list.head
    while head:
        if head.value in found_elements and head.value not in already_inserted_elements:
            output_list.prepend(head.value)
            already_inserted_elements.add(head.value)
        head = head.next


print('*** Test LinkedList Union/Intersection ***')

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
union_list = LinkedList()
intersection_list = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
expected_union = [11,1,9,32,21,65,6,35,4,2,3]
expected_intersection = [21,6,4]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

for i in expected_union:
    union_list.append(i)

for i in expected_intersection:
    intersection_list.append(i)

print (union(linked_list_1,linked_list_2))
assert union(linked_list_1,linked_list_2) == union_list, 'Union result not as expected'
print (intersection(linked_list_1,linked_list_2))
assert intersection(linked_list_1,linked_list_2) == intersection_list, 'Intersection result not as expected'

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
union_list = LinkedList()
intersection_list = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]
expected_union = [23,3,4,6,65,35,21,21,11,9,8,7,1]
expected_intersection = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

for i in expected_union:
    union_list.append(i)

for i in expected_intersection:
    intersection_list.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

print (union(linked_list_3,linked_list_4))
assert union(linked_list_3,linked_list_4) == union_list, 'Union result not as expected'
print (intersection(linked_list_3,linked_list_4))
assert intersection(linked_list_3,linked_list_4) == intersection_list, 'Intersection result not empty as expected'

# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
expected_union = LinkedList()
expected_intersection = LinkedList()

print (union(linked_list_5,linked_list_6))
assert union(linked_list_5,linked_list_6) == expected_union, 'Union result not empty as expected'

print (intersection(linked_list_5,linked_list_6))
assert intersection(linked_list_5,linked_list_6) == expected_union, 'Intersection result not empty as expected'

print('*** Success ***')
