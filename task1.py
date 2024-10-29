
# list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# add element into list
def append_to_list(head, value):
    new_node = Node(value)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


# print list
def print_list(head):
    current = head
    while current:
        print(current.value, end=" >> ")
        current = current.next
    print("None")


# reverse list
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


# merge sort
def merge_sort(head):
    if head is None or head.next is None:
        return head
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None
    left = merge_sort(head)
    right = merge_sort(next_to_middle)
    sorted_list = sorted_merge(left, right)
    return sorted_list


# get middle of list
def get_middle(head):
    if head is None:
        return head    
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


# merge lists
def sorted_merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    if left.value <= right.value:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)
    return result


# merge sorted lists
def merge_two_sorted_lists(list1, list2):
    dummy = Node(0)  
    tail = dummy
    while list1 and list2:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    return dummy.next


# Main
if __name__ == '__main__':
    try:
        # list
        head = None
        for value in [3, 1, 4, 2]:
            head = append_to_list(head, value)
        print("Original list:")
        print_list(head)
        reversed_head = reverse_list(head)
        print("Reverse_list:")
        print_list(reversed_head)
        sorted_head = merge_sort(reversed_head)
        print("Sorted lists:")
        print_list(sorted_head)
        # union
        list1 = None
        list2 = None
        for value in [1, 3, 5]:
            list1 = append_to_list(list1, value)
        for value in [2, 4, 6]:
            list2 = append_to_list(list2, value)
        print("List 1")
        print_list(list1)
        print("List 2")
        print_list(list2)
        merged_head = merge_two_sorted_lists(list1, list2)
        print("Union sorted lists (List1, List2)")
        print_list(merged_head)
    except (ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)
