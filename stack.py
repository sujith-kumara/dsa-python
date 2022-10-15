stack = []
top = -1

def push(a,top):
    stack.append(a)
    top += 1
def pops(top):
    stack.pop()
    top -= 1
def peek(top):
    print(stack[top])
print(stack)
push(1,top)
push(2,top)
push(3,top)
print(stack)
pops(top)
print(stack)
peek(top)


