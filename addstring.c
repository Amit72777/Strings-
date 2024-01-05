 // add three string in a one string  without use any function 
#include <stdio.h>
int main()
{
    char str1[30], str2[30], str3[30], str4[30];
    int i, k, j;
    // taking input the string 
    printf("enter the string ");
    scanf("%s", str1);
    printf("Enter the second string ");
    scanf("%s", str2);
    printf("Enter the third  string ");
    scanf("%s", str4);
// using loop perform operation 
    for (i = 0; str1[i] != '\0'; i++)
    {
        str3[i] = str1[i];
    }
    str3[i] = ' ';
    i++;
    for (k = 0; str2[k] != '\0'; k++)
    {
        str3[i] = str2[k];
        i++;
    }
    str3[i] = ' ';
    i++;

    for (j = 0; str4[j] != '\0'; j++, i++)
    {
        str3[i] = str4[j];
    }
    str3[i] = '\0';
    printf("\n%s\n", str3);
    printf("\n the number of character is :%d", i);

    return 0;
}