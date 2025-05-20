class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, char):
        char = char.lower()
        new_node = Node(char)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += current.data
            current = current.next
        return result

    def is_custom_palindrome(self):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        seen = set()

        fwd = ""
        current = self.head
        while current:
            ch = current.data
            if ch not in vowels and ch not in seen and ch.isalpha():
                fwd = fwd + ch
                seen.add(ch)
            current = current.next

        bwd = ""
        seen.clear()
        current = self.tail
        while current:
            ch = current.data
            if ch not in vowels and ch not in seen and ch.isalpha():
                bwd = bwd + ch
                seen.add(ch)
            current = current.prev

        return fwd == bwd

if __name__ == "__main__":
    input_str = input("Enter a string: ")

    dll = DoublyLinkedList()
    for char in input_str:
        if char.isalpha():
            dll.insert(char)

    print("Linked List:", dll)
    if dll.is_custom_palindrome():
        print("True")
    else:
        print("False")
