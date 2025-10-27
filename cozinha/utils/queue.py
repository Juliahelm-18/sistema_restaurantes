class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None  # Referência para o início da fila
        self.tail = None  # Referência para o final da fila
        self.length = 0  # Contador para o tamanho da fila

    def __str__(self) -> str:
        valores = []
        current = self.head
        while current:
            valores.append(str(current.value))
            current = current.next
        return " -> ".join(valores)

    def enqueue(self, value) -> None:
        novo_no = Node(value)  # Cria um novo nó
        if self.is_empty():
            self.head = self.tail = (
                novo_no  # Se estiver vazia, o nó é tanto a cabeça quanto a cauda
            )
        else:
            self.tail.next = novo_no  # O nó atual da cauda aponta para o novo nó
            self.tail = novo_no  # O novo nó se torna a cauda
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value  # Armazena o value do nó que está na cabeça
        self.head = self.head.next  # Atualiza a cabeça para o próximo nó
        if (
                self.head is None
        ):  # Se a cabeça for None, a fila está vazia e a cauda também deve ser None
            self.tail = None
        self.length -= 1
        return value

    def is_empty(self) -> bool:
        return self.head is None

    def first_value(self):
        if self.is_empty():
            print("A fila está vazia.")
            return None
        return self.head.value

    def queue_length(self) -> int:
        return self.length

    # def queue_length(self):
    #     contador = 0
    #     current = self.head
    #     while current:
    #         contador += 1
    #         current = current.next
    #     return contador
