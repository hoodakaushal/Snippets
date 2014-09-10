#include <stdio.h>
#include <cstring>
#include <string>
#include <iostream>
#define N 1000000007
#define MOD(a,n) (a%n)
using namespace std;
typedef long long int lli;

int main(int argc, char* argv[])
{
	char* path;
    path =  argv[1];
    //scanf("%s",path);
    int i= 0;
    int a=1;
    while (path[i] != '\0')
    {
        if (i%2==0)
        {
            if (path[i] == 'l')
                a= ((lli)(a*2))%N;
            else
                a = ((lli)(a*2+2))%N;

        }
        else
        {
            if (path[i] == 'l')
                a= ((lli)(a*2-1))%N;
            else
                a= ((lli)(a*2+1))%N;
        }
        i++;
    }
    printf("%d\n",a);
	return 0;
}