```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n = 10; // Variable Declaration
    int *ptr; // Pointer Declaration
    ptr = (int *)malloc(n *sizeof(int)); // Dynamic Memory Allocation

    for (int i = 0; i < n; i++) // First For Loop
    {
      ptr[i] = 7 * (i+1); // Data Transformation
    }

    printf("The Array is \n"); // Print Statement

    for (int i = 0; i < n; i++) // Second For Loop
    {
        printf("%d \n", ptr[i]); // Dependency on First Loop's Output
    }

    n = 15; // Change of Size
    ptr = (int *)realloc(ptr, 10 * sizeof(int)); // Resize Memory

    for (int i = 0; i < n; i++) // Third For Loop
    {
        ptr[i] = 7 * (i+1); // Data Transformation
    }

    printf("The Array is \n"); // Print Statement

    for (int i = 0; i < n; i++) // Fourth For Loop
    {
        printf("%d \n", ptr[i]); // Dependency on Resized Array
    }

    return 0; // Return Statement
}
```