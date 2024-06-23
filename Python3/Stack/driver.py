import random


class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,val):
        self.stack.append(val)
    
    def pop(self):
        if not len(self.stack):
            print(f"stack is empty, nothing to pop")
            return None
        return self.stack.pop()




def main():

    return



if __name__ == '__main__':
    main()