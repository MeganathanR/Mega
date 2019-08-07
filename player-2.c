#include <stdio.h>
void main()
{
    int i, fact = 1, num;

    scanf("%d", &num);
    if (num <= 0)
        fact = 1;
    else
    {
        for (i = 1; i <= num; i++)
        {
            fact = fact * i;
        }
    }
    printf(" %d",fact);
}
