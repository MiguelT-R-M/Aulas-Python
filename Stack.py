Stack = [1, 2 ,3]

def push(x):

    Stack.append(x)

def top(x):

    return(x[len(x)-1])

def empty(x):

    if len(x)==0:
        print("Stack vazio")
    if len(x)>0:
        print("Stack não vazio")

def pop(x):

    print("pop", top(x))
    x.pop(len(x)-1)
    
empty(Stack)
print(top(Stack))
push(4)
print(top(Stack))
pop(Stack)
print(top(Stack))
empty(Stack)
pop(Stack) 
pop(Stack)
pop(Stack)
empty(Stack)