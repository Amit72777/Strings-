
// Copy one string to another string without use funciton 
#include <stdio.h>
int main()
{
    char str1[80], str2[80];
    int i;
    printf("Enter the string ");
    scanf("%s", str2);
    for (i = 0; str2[i] != '\0'; i++)
    {
        str1[i] = str2[i];
    }
    str1[i] = '\0';
    printf("%s", str1);
    printf("\nthe number of charater is %d", i);
    return 0;
}