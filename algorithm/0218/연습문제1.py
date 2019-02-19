str1 = "2*3*4+5"
# 2345/*+
math_o = ['+', '-', '*', '/']
stack = []
for i in str1:
    if i not in math_o:
        print(f'{i}', end="")
    else:
        stack.append(i)
while stack:
    print(stack.pop(),end="")