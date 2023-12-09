#include <stdio.h>
int main()
{
    char str[20];

    //  scanf("%s",str);
    gets(str);
    int j = 0;
    int size = 0;
    while (str[size] != '\0')
    {
        size++;
    }

    for (int i = 0; i < size; i++)
    {
        char temp = str[i];
        str[i] = str[size - 1];
        str[size - 1] = temp;

        size--;
    }
    puts(str);

    return 0;
}