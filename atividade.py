class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
pilha = Stack()

pilha.push('é assim que acaba')
pilha.push('é assim que começa')
pilha.push('é assim que acaba, livro de colorir')
print(pilha.items)
print(pilha.peek())
print(pilha.items)
pilha.pop()
print(pilha.items)