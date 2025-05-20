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
        seen_left = set()
        seen_right = set()

        left = self.head
        right = self.tail

        while left and right:
            while left and (left.data in vowels or left.data in seen_left):
                seen_left.add(left.data)
                left = left.next
            
            while right and (right.data in vowels or right.data in seen_right):
                seen_right.add(right.data)
                right = right.prev

            if not left or not right:
                break

            left_char = left.data
            right_char = right.data

            if left_char != right_char:
                return False

            seen_left.add(left_char)
            seen_right.add(right_char)

            left = left.next
            right = right.prev

        return True


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
