class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "堆疊是空的"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "堆疊是空的"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("堆疊內容：", self.stack)

# 使用示例
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()

    print("堆疊頂部元素：", stack.peek())
    print("出堆疊元素：", stack.pop())
    stack.display()
    print("堆疊頂部元素：", stack.peek())