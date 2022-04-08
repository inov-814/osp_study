#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	printf("hello world!\n");
	int two;
	two = 2;
	printf("two + argc = %d\n",two+argc);
	exit(0);
}
