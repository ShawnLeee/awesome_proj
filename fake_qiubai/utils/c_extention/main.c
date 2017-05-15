#include <stdio.h>
#include "command.h"
#include "list.h"

int main(){
    int a = 1;
    int b = 3;
    compare(a, b);
    printf("in main.c\n");
    printf("in main.c\n");
    list_init(1);
    return 0;
}