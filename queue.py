class Queue:

	def __init__(self):
		self.queue = []
		self.size = 0

	def push(self, e):
		self.queue.append(e)
		self.size += 1

	def pop(self):
		if not self.empty():
			self.queue.pop(0)	
			self.size -= 1

	def empty(self):
		if self.size == 0:
			return True
		return False

	def length(self):
	    return self.size

	def front(self):
		if not self.empty():
			return self.queue[0]
		return None

	def show(self):
		print(self.queue)