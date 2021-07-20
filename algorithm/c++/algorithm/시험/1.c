#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 512

int top;
int stack[MAXN];

int pop() {
    if (top == 0) return 0;

    return stack[--top];
}


int push(char c) {
    if (top == MAXN) return 0;

    stack[top++] = c;

    return 1;
}

bool is_matched(const char* s)
{
    // 구현해보세요.
    top = 0;


    for (register int i = 0; *(s + i); ++i) {
        char c = *(s + i);
        if (c == '(' || c == '{' || c == '[') {
            if (!push(c)) return false;
        }
        else if (c == ')' && pop() != '(') return false;
        else if (c == '}' || c == ']') {
            if (c - pop() != 2) return false;
        }
    }

    if (top != 0) return false;

    return true;
}

int main(void)