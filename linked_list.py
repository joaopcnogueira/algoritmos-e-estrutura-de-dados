class Node:

	def __init__(self, label):
		self._label = label
		self._next = None

	@property
	def label(self):
		return self._label

	@label.setter
	def label(self, label):
		self._label = label

	@property
	def next(self):
		return self._next
	
	@next.setter
	def next(self, ref):
		self._next = ref

class LinkedList:

	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0

	def empty(self):
		if self.size == 0:
			return True
		return False

	def length(self):
		return self.size

	def show(self):
		curr_node = self.first

		while curr_node != None:
			print(curr_node.label, end=' ')
			curr_node = curr_node.next
		print('')

	def push(self, label, index):

		if index >= 0:

			# create a new node
			node = Node(label)

			# is the linked list empty?
			if self.empty():
				self.first = node
				self.last = node
				self.size += 1

			else:
				if index == 0:
					# insertion at the beginning
					node.next = self.first
					self.first = node
					self.size += 1
				elif index >= self.size:
					# insertion at the end
					self.last.next = node
					self.last = node
					self.size += 1
				else:
					# insertion in any place between the beginning and
					# the end of the linked list
					prev_node = self.first
					curr_node = self.first.next
					curr_index = 1

					while curr_node != None:

						if curr_index == index:
							# curr_node is the next of the node
							node.next = curr_node
							prev_node.next = node
							self.size += 1
							break
						prev_node = curr_node
						curr_node = curr_node.next
						curr_index += 1
	def pop(self, index):

		if not self.empty() and (0 <= index < self.size):

			flag_remove = False

			if self.first.next == None:
				# only 1 element in the linked list
				self.first = None
				self.last = None
				flag_remove = True
			elif index == 0:
				# remove from the beginning, but the linked list
				# has more than 1 element
				self.first = self.first.next
				flag_remove = True
			else:
				prev_node = self.first
				curr_node = self.first.next
				curr_index = 1

				while curr_node != None:
					 if index == curr_index:
					 	prev_node.next = curr_node.next
					 	curr_node.next = None
					 	flag_remove = True
					 	break

					 prev_node = curr_node
					 curr_node = curr_node.next
					 curr_index += 1

			if flag_remove:
				self.size -= 1


