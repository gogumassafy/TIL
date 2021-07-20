#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

struct interval
{
    int start;  // inclusive
    int end;    // exclusive
    struct interval* next;

};

struct interval* my_alloc(int _start, int _end, struct interval* _next) {
    struct interval* inter = malloc(sizeof(struct interval));

    inter->start = _start;
    inter->end = _end;
    inter->next = _next;

    return inter;
}

struct interval_set
{
    struct interval* intervals;
    int cnt;
};


struct interval_set* interval_set_new(void)
{
    // interval_set 자료구조 생성하는 함수입니다.
    // 이 함수는 수정하지 마세요.
    struct interval_set* s = malloc(sizeof(struct interval_set));

    s->intervals = NULL;
    s->cnt = 0;

    return s;
}

void recursive_free(struct interval* s) {
    struct interval* ptr = s->next;

    if (ptr) recursive_free(ptr);
    free(s);
}

void interval_set_free(struct interval_set* s)
{
    // 구현해보세요.
    struct interval* ptr = s->intervals;
    
    if (ptr) recursive_free(ptr);
}

bool interval_set_add(struct interval_set* s, int start, int end)
{
    // 주어진 [start, end) 범위를 추가합니다.
    // 만일
    //  - 해당 범위를 일부분 또는 완전히 포함하는 interval이 이미 있었으면 아무런 변화를 주지않고 false를 리턴합니다. 1
    //  - 해당 범위가 기존 interval들과 전혀 겹치지 않는다면 신규 interval을 생성해서 추가하고 true를 리턴합니다. 2
    //  - 해당 범위가 기존 interval들과 전혀 겹치지 않지만 맞닿아있는 interval이 있으면 merge하고 true를 리턴합니다. 3    
    // 구현해보세요.
    
    if (s->cnt == 0 || s->intervals->start >= end) {
        if (s->intervals && end == s->intervals->start) {
            s->intervals->start = start;
        }
        else {
            s->intervals = my_alloc(start, end, s->intervals);

            s->cnt++;
        }
    }
    else {
        struct interval tmp;
        struct interval* ptr = &tmp;
        ptr->next = s->intervals;

        while (ptr->next) {
            if (start >= ptr->next->start && start < ptr->next->end) return false; // 1
            if (end >= ptr->next->start && end < ptr->next->end) return false; // 1
            if (start <= ptr->next->start && end >= ptr->next->end) return false; // 1

            if (ptr->next->next) {
                if (start < ptr->next->next->start) {
                    ptr = ptr->next;
                    if (ptr->next && end > ptr->next->start) return false;
                    break;
                }
            }

            ptr = ptr->next;
        }

        // 3
        struct interval* next = ptr->next;

        if (next && ptr->end == start && next->start == end) {
            ptr->end = next->end;
            ptr->next = next->next;
            free(next);
            s->cnt--;
        }
        else if (next && next->start == end) {
            next->start = start;
        }
        else if (ptr->end == start) {
            ptr->end = end;
        }
        else {
            // 2
            struct interval *new_one = my_alloc(start, end, 0);
            s->cnt++;
            if (ptr->next) new_one->next = next;

            ptr->next = new_one;
        }
    }

    // seg tree 쓰면 1, 2, 3 바로 수행 가능한데.
    // interval set을 어차피 수정해야 되니 사용 x

    return true;
}

bool interval_set_contains(struct interval_set* s, int start, int end)
{
    // 주어진 [start, end) 범위를 완전히 포함하는 구간이 있을때만 true를 리턴합니다.
    // 그렇지 않으면 false를 리턴합니다.
    // 구현해보세요.

    struct interval* ptr = s->intervals;

    while (ptr) {
        if (ptr->start <= start && ptr->end >= end) return true;
        if (ptr->start >= end) break;

        ptr = ptr->next;
    }

    return false;
}

void interval_set_clear(struct interval_set* s)
{
    // 구현해보세요.
    interval_set_free(s);
    s->cnt = 0;
    s->intervals = 0;
}

static int parse_interval(char* str, int* start, int* end)
{
    char* last;
    char* tok, * brk = str;

    tok = strtok_r(str, " ,\r\n", &brk);
    if (NULL == tok)
        return -1;
    *start = (int)strtol(tok, &last, 10);
    if ('\0' != *last)
        return -1;

    tok = strtok_r(NULL, " ,\r\n", &brk);
    if (NULL == tok)
        return -1;
    *end = (int)strtol(tok, &last, 10);
    if ('\0' != *last)
        return -1;

    return 0;
}

int
main(void)
{
    int ret;
    int start, end;
    // line 변수는 parse_interval() 함수안에서, strtok_r()로 토큰을 자르면서 내용을 수정해야 하는데
    // 아래와 같이 스택변수로 생성했더니, parse_interval() 함수안에서 이 메모리 영역을 수정할 수가 없다.
    // (해커랭크 사이트 시스템의 제약인듯)
    // char line[256];
    char* line = malloc(256);
    struct interval_set* s = interval_set_new();

    bool ok = interval_set_add(s, 4, 5);
     ok = interval_set_add(s, 0, 1);
     ok = interval_set_add(s, 2, 3);
     ok = interval_set_add(s, 0, 4);
     ok = interval_set_add(s, 6, 7);
     ok = interval_set_add(s, 7, 8);
     ok = interval_set_add(s, 9, 10);
     ok = interval_set_add(s, 8, 9);

     ok = interval_set_add(s, 20, 40);
     ok = interval_set_add(s, 20, 39);
     ok = interval_set_add(s, 20, 41);

     ok = interval_set_add(s, 19, 41);
     ok = interval_set_add(s, 19, 39);
     ok = interval_set_add(s, 19, 40);

    interval_set_clear(s);

    ok = interval_set_add(s, 0, 2);
    ok = interval_set_add(s, 0, 4);
    ok = interval_set_add(s, 6, 7);
    ok = interval_set_add(s, 7, 8);
    ok = interval_set_add(s, 9, 10);
    ok = interval_set_add(s, 8, 9);

    ok = interval_set_add(s, 20, 40);
    ok = interval_set_add(s, 20, 39);
    ok = interval_set_add(s, 20, 41);

    ok = interval_set_add(s, 19, 41);
    ok = interval_set_add(s, 19, 39);
    ok = interval_set_add(s, 19, 40);

    return 0;
}