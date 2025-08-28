# Stack Notepad Exercise 
#-----------------------
#You are building a simple command-line notepad using a stack.
# - Type a word to add it to your document (puch onto a stack).
# - Type 'UNDO' to remove the last word you added (pop from stack).
# - Type 'SHOW' to display the current document (all words in the stack).
#
# NOTE: You must use import the methods from stack_implementation.py. Do not use a Python list directory
#Complete the functions below to make this work!

from stack_implementation import  push, pop, is_empty, size

def add_word(word):
    push(word)