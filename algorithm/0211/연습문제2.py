pair_num = [0]
pair_dict = {'[': 0, }

def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        print("Stack is Empty!")
        return
    else:
        return s.pop(-1)

def isPair(items):
    if not len(items) % 2:
        return False
    for i in items:
        if i == "(":
            push(i)
        elif i == ")":
            if len(s) == 0:
                return False
            pop()

    return True if not len(s) else False

s=[]

print(isPair(input()))
