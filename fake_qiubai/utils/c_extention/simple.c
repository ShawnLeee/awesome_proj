#include <sys/wait.h>
#include <sys/socket.h>
#include <sys/select.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/time.h>
#include <stdint.h>
#include <inttypes.h>
#include <netdb.h>

#include <pwd.h>
#include <unistd.h>
#include <dirent.h>
#include <pthread.h>
#include <stdlib.h>
#include "simple.h"
int add(int x, int y){
    return x + y;
}

int xa_start_thread(xa_thread_func_t func, void *param){
    pthread_t thread_id;
    pthread_attr_t attr;
    (void) pthread_attr_init(&attr);
    (void) pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);

    return pthread_create(&thread_id, &attr, func, param);
}
void printids(const char *s){
    pid_t pid;
    pthread_t tid;
    pid = getpid();
    tid = pthread_self();
    printf("\n---------------------\n");
    printf("%s pid %lu tid %lu \n", s, (unsigned long)pid, (unsigned long)tid);
    printf("\n---------------------\n");
}
void *
thr_func(void *arg){
    printids("new thread:");
    int int_arg = *((int *)arg);
    printf("I am get called\n");
    printf("%d\n", int_arg);
    // free(arg);
    return (void*)0;
}
int thread_test(int param){
    pthread_t tid;
    int i = 0;
    printf("%d\n", param);
    for(;i < 10;i++){
        pthread_create(&tid, NULL, thr_func, (void *)&i);
    }
    return 0;
}