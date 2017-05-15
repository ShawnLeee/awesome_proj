#include <stdio.h>
#include "defs.h"
int compare(int a, int b)
{
    printf("in command.c\n");
    return d_compare(a, b);
}