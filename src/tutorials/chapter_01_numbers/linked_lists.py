class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# LC206. Reverse Linked List, top100
def reverseList(self, head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr is not None:
        curr.next, prev, curr = prev, curr, curr.next
    return prev


# LC92. Reverse Linked List II
def reverseBetween(self, head, m, n):
    dummy = start = ListNode(0, head)
    for _ in range(m-1): start = start.next # move the  position before m
    pre, curr = None, start.next # point to pre, right before cur
    for _ in range(n-m+1): # reverse the defined part
        curr.next, pre, curr = pre, curr, curr.next
    start.next.next = curr # point old start to tail: curr = n+1
    start.next = pre # point start to new head
    return dummy.next


# LC2. Add Two Numbers, top100
def addTwoNumbers(self, l1, l2):
    result = result_tail = ListNode(0)
    carry = 0
    while l1 or l2 or carry:  # pattern
        val1 = (l1.val if l1 else 0)  # pattern
        val2 = (l2.val if l2 else 0)  # pattern
        carry, out = divmod(val1+val2 + carry, 10)  # pattern
        result_tail.next = ListNode(out)
        result_tail = result_tail.next
        l1 = l1.next if l1 else None  # pattern
        l2 = l2.next if l2 else None  # pattern
    return result.next


# LC445. Add Two Numbers II
def addTwoNumbers(self, l1, l2):
    def reverse_list(lst):
        prev, curr = None, lst
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
    rl1, rl2 = reverse_list(l1), reverse_list(l2)
    res = curr = ListNode(0)
    carry = 0
    while rl1 or rl2 or carry:
        v1 = rl1.val if rl1 else 0
        v2 = rl2.val if rl2 else 0
        carry, digit = divmod(v1 + v2 + carry, 10)
        curr.next = ListNode(digit)
        curr = curr.next
        rl1 = rl1.next if rl1 else None
        rl2 = rl2.next if rl2 else None
    return reverse_list(res.next)


# LC160. Intersection of Two Linked Lists
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    pA = headA
    pB = headB
    while pA != pB:
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next
    return pA


# LC141. Linked List Cycle
def hasCycle(self, head: ListNode) -> bool:
    hare = turtle = head
    while hare and hare.next:
        turtle, hare = turtle.next, hare.next.next
        if hare == turtle: return True
    return False


# LC143. Reorder List
def reorderList(self, head: ListNode) -> None:
    if not head: return
    slow = fast = head # in 1->2->3->4->5->6 find 4
    while fast and fast.next: # slow is the middle node
        slow, fast = slow.next, fast.next.next
    prev, curr = None, slow # reverse the second half, prev is new head
    while curr: # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        curr.next, prev, curr = prev, curr, curr.next
    first, second = head, prev # merge two sorted linked lists
    while second.next: # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first.next, first = second, first.next
        second.next, second = first, second.next