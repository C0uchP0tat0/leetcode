from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node_to_front(self, node):
        node.next = self.head
        self.head = node

    def add_node_to_end(self, node):
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curent_head1 = list1
        curent_head2 = list2
        dummy = ListNode(0)
        result_tail = dummy

        while curent_head1 is not None and curent_head2 is not None:
            curent_val1 = curent_head1.val
            curent_val2 = curent_head2.val
            if curent_val1 < curent_val2:
                node = ListNode(curent_val1)
                result_tail.next = node
                result_tail = node
                curent_head1 = curent_head1.next
            elif curent_val1 > curent_val2:
                node = ListNode(curent_val2)
                result_tail.next = node
                result_tail = node
                curent_head2 = curent_head2.next
            else:
                node = ListNode(curent_val1)
                result_tail.next = node
                result_tail = node
                node = ListNode(curent_val2)
                result_tail.next = node
                result_tail = node
                curent_head1 = curent_head1.next
                curent_head2 = curent_head2.next

        while curent_head1 is not None:
            node = ListNode(curent_head1.val)
            result_tail.next = node
            result_tail = node
            curent_head1 = curent_head1.next

        while curent_head2 is not None:
            node = ListNode(curent_head2.val)
            result_tail.next = node
            result_tail = node
            curent_head2 = curent_head2.next

        return dummy.next
        

if __name__ == "__main__":
    res = Solution()
    # Input: list1 = [1,2,4], list2 = [1,3,4]
    # Output: [1,1,2,3,4,4]
    # Example 2:

    # Input: list1 = [], list2 = []
    # Output: []
    # Example 3:

    # Input: list1 = [], list2 = [0]
    # Output: [0]
    list1 = [1,2,4]
    list2 = [1,3,4]

    linked_list1 = LinkedList()
    linked_list2 = LinkedList()

    for i in list1[::-1]:
        node = ListNode(i)
        linked_list1.add_node_to_front(node)

    for i in list2[::-1]:
        node = ListNode(i)
        linked_list2.add_node_to_front(node)

    res_list = res.mergeTwoLists(linked_list1.head, linked_list2.head)
    curent_head = res_list
    while curent_head is not None:
        print(curent_head.val)
        curent_head = curent_head.next
    