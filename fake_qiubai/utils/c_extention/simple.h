#include <stdio.h>

typedef void* (*xa_thread_func_t)(void *);

int add(int x, int y);
int xa_start_thread(xa_thread_func_t func, void *param);
int thread_test();