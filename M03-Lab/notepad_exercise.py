# Stack Notepad Exercise 
#-----------------------
#You are building a simple command-line notepad using a stack.
# - Type a word to add it to your document (puch onto a stack).
# - Type 'UNDO' to remove the last word you added (pop from stack).
# - Type 'SHOW' to display the current document (all words in the stack).
#
# NOTE: You must use import the methods from stack_implementation.py. Do not use a Python list directory
#Complete the functions below to make this work!

# notepad_exercise.py
# -------------------------
# Stack Notepad Exercise
# - Type a word to add it to your document (push onto a stack).
# - Type 'UNDO' to remove the last word you added (pop from stack).
# - Type 'SHOW' to display the current document (all words in the stack).

from stack_implementation import push, pop, is_empty, size

def add_word(word):
    # Push a word onto the stack
    push(word)

def undo():
    # Undo the last word by popping from the stack
    if not is_empty():
        pop()

def show():
    # Display the stack in order of items being added.
    # We can’t access the internal stack directly, so we use a temp list.
    temp = []
    
    # Pop all items into temp
    while not is_empty():
        temp.append(pop())
    
    # Reverse temp to restore original insertion order
    temp.reverse()
    
    # Print the document
    print(" ".join(temp))
    
    # Push items back into the stack
    for word in temp:
        push(word)

def main():
    while True:
        command = input('Enter a command: ').strip()
        
        if command.upper() == "UNDO":
            undo()
        elif command.upper() == "SHOW":
            show()
        elif command.upper() == "SIZE":
            print(size())
        elif command.upper() == "EXIT":
            break
        else:
            add_word(command)

if __name__ == '__main__':
    main()