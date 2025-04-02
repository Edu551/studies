class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Recursive_Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        hash_set = {}
        self.traverse_linked_list(headA, hash_set)
        intersection_node = self.compare_dict(headB, hash_set)
        return intersection_node

    def traverse_linked_list(self, head: ListNode, hash_set: dict):
        if head is None:
            return
        if head not in hash_set:
            hash_set[head] = head
        self.traverse_linked_list(head.next, hash_set)

    def compare_dict(self, head: ListNode, hash_set: dict) -> ListNode | None:
        if head is None:
            return None
        if head in hash_set:
            return head
        return self.compare_dict(head.next, hash_set)
    
class Iterative_Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        hash_set = {}
        self.traverse_linked_list(headA, hash_set)
        intersection_node = self.compare_dict(headB, hash_set)
        return intersection_node
    
    def traverse_linked_list(self, head: ListNode, hash_set: dict):
        while head:
            if head not in hash_set:
                hash_set[head] = head
            head = head.next
    
    def compare_dict(self, head: ListNode, hash_set: dict) -> ListNode | None:
        while head:
            if head in hash_set:
                return head
            head = head.next
        return None
    
class Two_Pointers_Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        pointerA, pointerB = headA, headB

        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        return pointerA

