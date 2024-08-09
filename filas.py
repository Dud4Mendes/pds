from typing import Deque, Any, Iterator
from collections import deque

class Queue:
    """Uma clase representando uma fila"""

    def __init__(self, maxlen=None) -> None:
        self.__itens: Deque[Any] = deque(maxlen=maxlen)    

    def enqueue(self, *itens: Any) -> None:
        """Enqueue (enfileirar) é o mesmo que append"""
        for item in itens:
            self.__itens.append(item)    

    def dequeue(self) -> Any:
        """Dequeue (desenileirar) é o mesmo que popleft"""
        if not self:
            raise IndexError('pop rom empty queue')    
        
        return self.__items.popleft()
    
    def __repr__(self) -> str:
        return str(self.__itens)
    
    def __bool__(self) -> bool:
        return bool(self.__itens)

    def __len__(self) -> int:
        return len(self.__itens)
    
    def __iter__(self) -> Iterator:
        return self.__itens.__iter__()
    
    def __getitem__(self, index: int) -> any:
        return self.__itens[index]
    
if __name__ == "__main__":
    fila = Queue()

fila.enqueue('A', 'B', 'C', 'D')

print(fila.__repr__())
print(fila.__getitem__(2))
print(fila.__bool__())
print(fila.__iter__())

fila.enqueue('d', 'e', 'f', 'g')

print(fila)
print('Item com inice 1:', fila[1], end='\n\n')

for item in fila:
    print('Iteração:', item)


