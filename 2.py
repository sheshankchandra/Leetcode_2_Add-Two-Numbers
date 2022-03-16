# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

		ans = ListNode()

		itr1 = l1
		itr2 = l2
		itr = ans

		c = 0

		while itr1 and itr2:
			temp = itr1.val + itr2.val + c
			if temp > 9:

				newNode = ListNode(temp % 10)
				c = 1
			else:
				newNode = ListNode(temp)
				c = 0
			itr.next = newNode

			itr1 = itr1.next
			itr2 = itr2.next
			itr = itr.next

		if itr1:
			while itr1:
				temp = itr1.val + c
				if temp > 9:
					newNode = ListNode(temp % 10)
					c = 1
				else:
					newNode = ListNode(temp)
					c = 0
				itr.next = newNode
				itr = itr.next
				itr1 = itr1.next

		if itr2:
			while itr2:
				temp = itr2.val + c
				if temp > 9:
					newNode = ListNode(temp % 10)
					c = 1
				else:
					newNode = ListNode(temp)
					c = 0
				itr.next = newNode
				itr = itr.next
				itr2 = itr2.next

		if c != 0:
			newNode = ListNode(1)
			itr.next = newNode

		return ans.next