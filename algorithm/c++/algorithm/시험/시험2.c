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
    // interval_set �ڷᱸ�� �����ϴ� �Լ��Դϴ�.
    // �� �Լ��� �������� ������.
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
    // �����غ�����.
    struct interval* ptr = s->intervals;
    
    if (ptr) recursive_free(ptr);
}

bool interval_set_add(struct interval_set* s, int start, int end)
{
    // �־��� [start, end) ������ �߰��մϴ�.
    // ����
    //  - �ش� ������ �Ϻκ� �Ǵ� ������ �����ϴ� interval�� �̹� �־����� �ƹ��� ��ȭ�� �����ʰ� false�� �����մϴ�. 1
    //  - �ش� ������ ���� interval��� ���� ��ġ�� �ʴ´ٸ� �ű� interval�� �����ؼ� �߰��ϰ� true�� �����մϴ�. 2
    //  - �ش� ������ ���� interval��� ���� ��ġ�� ������ �´���ִ� interval�� ������ merge�ϰ� true�� �����մϴ�. 3    
    // �����غ�����.
    
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

    // seg tree ���� 1, 2, 3 �ٷ� ���� �����ѵ�.
    // interval set�� ������ �����ؾ� �Ǵ� ��� x

    return true;
}

bool interval_set_contains(struct interval_set* s, int start, int end)
{
    // �־��� [start, end) ������ ������ �����ϴ� ������ �������� true�� �����մϴ�.
    // �׷��� ������ false�� �����մϴ�.
    // �����غ�����.

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
    // �����غ�����.
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
    // line ������ parse_interval() �Լ��ȿ���, strtok_r()�� ��ū�� �ڸ��鼭 ������ �����ؾ� �ϴµ�
    // �Ʒ��� ���� ���ú����� �����ߴ���, parse_interval() �Լ��ȿ��� �� �޸� ������ ������ ���� ����.
    // (��Ŀ��ũ ����Ʈ �ý����� �����ε�)
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