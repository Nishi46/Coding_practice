# Python3 program to find decimal value
# of binary linked list

# Node Class
class Node:
	

	def __init__(self, data):
		
		# Assign data
		self.data = data
		

		self.next = None

class LinkedList:


	def __init__(self):
		
		self.head = None


	def decimalValue(self, head):
		

		res = 0
		while head:

			res = (res << 1) + head.data

			# Move Next
			head = head.next
			
		return res


if __name__ == '__main__':


	llist = LinkedList()

	llist.head = Node(1)
	llist.head.next = Node(0)
	llist.head.next.next = Node(1)
	llist.head.next.next.next = Node(1)
	
	print("Decimal Value is {}".format(
		llist.decimalValue(llist.head)))



