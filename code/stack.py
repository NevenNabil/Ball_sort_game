class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def get_top(self):
        if self.isEmpty():
            return False
        else:
            pop = self.pop()
            self.push(pop)
            return pop

    def get_for_print(self):
        removed_lis = []
        out_lis = []
        index = 0
        while not self.isEmpty():
            out_lis.append(str(self.get_top()) + " ")
            removed_lis.append(self.pop())
            index += 1

        out_lis.reverse()
        if index < 4:
            for i in range(4 - index):
                out_lis.append(str("-") + " ")
        removed_lis.reverse()
        for item in removed_lis:
            self.push(item)
        return out_lis

    def get_values(self):
        out = []
        while not self.isEmpty():
            out.append(self.pop())

        out.reverse()
        for item in out:
            self.push(item)
        return out

    # Get the current size of the stack
    def getSize(self):
        return self.size

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
