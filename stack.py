class Stack:
    
    def __init__(self):
        self.stack = []
        self.size = 0
        
    def push(self, e):
        self.stack.append(e)
        self.size += 1
        
    def pop(self):
        if not self.empty():
            self.stack.pop()
            self.size -= 1
    
    def empty(self):
        if self.size == 0:
            return True
        return False
    
    def length(self):
        return self.size

    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None

    def show(self):
        print(self.stack)
    
