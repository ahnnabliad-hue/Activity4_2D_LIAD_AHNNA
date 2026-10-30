from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue

def main():
print("=== STACKS AND QUEUES LAB ===")
print("1. Work with a data structure")
print("2. Check balanced parentheses")
print("3. Simulate a print queue")
print("0. Exit")

choice = input("Choose: ")

if choice == "1":
    print("Stack and Queue implementations are ready.")
elif choice == "2":
    expression = input("Enter an expression: ")
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                print("Not balanced")
                break
    else:
        print("Balanced" if not stack else "Not balanced")

elif choice == "3":
    print("Print queue simulation")
    print("Use FIFO: First In, First Out.")
elif choice == "0":
    print("Goodbye!")
else:
    print("Invalid choice.")

if name == "main":
main()
