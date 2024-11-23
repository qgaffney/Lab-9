class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.item.pop()

    def is_empty(self):
        return len(self.items) == 0

def is_balanced(expression):
    stack = []
    opening = ['(', '{', '[']
    closing = [')', '}', ']']

    for char in expression:
        if char in opening:
            stack.append(char)

        elif char in closing:
            if not stack:
                return False
            
            top = stack.pop()
            if opening.index(top) != closing.index(char):
                return False
            
    return not stack

from collections import deque

def enqueue_opening_parentheses(expression):
    queue = deque()
    for char in expression:
        if char in '({[':
            queue.append(char)

    return queue

expression = '{(a + b) * [c - d]}'
result_queue = enqueue_opening_parentheses(expression)

def check_parentheses(expression):
    stack = []
    opening_parentheses = "({["
    closing_parentheses = ")}]"

    for char in expression:
        if char in opening_parentheses:
            stack.append(char)
        
        elif char in closing_parentheses:
            if not stack:
                return False
            
            top = stack.pop()
            if opening_parentheses.index(top) != closing_parentheses.index(char):
                return False
            
    return not stack

expression2 = "[(a - b) * c]"
if check_parentheses(expression2):
    print("Parentheses are balanced.")
else:
    print("Parentheses are not balanced.")

import random

def simulate_print_queue(jobs):
    for job in jobs:
        print("Printing: ", job)

        processing_time = random.randint(1, 8)
        print("Job completed in", processing_time, "seconds.")

if __name__ == "__main__":
    jobs = ["Document1.pdf", "Image.jpeg", "Report.docx"]

    job_queue = deque(["Document1.pdf", "Image.jpeg", "Report.docx"])

    while job_queue:
        job = job_queue.popleft()
        

print(is_balanced("()"))
print(is_balanced("({[]})"))
print(is_balanced("({)}"))
print(is_balanced("("))
print(result_queue)
print(check_parentheses(expression2))
print("Processing:", simulate_print_queue(jobs))