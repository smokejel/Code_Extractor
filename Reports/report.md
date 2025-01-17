1. The system shall declare an integer variable `n` to hold the size of the array, initialized to 5.
2. The system shall declare a pointer `ptr` to hold the address of dynamically allocated memory.
3. The system shall allocate memory for `ptr` using `calloc`, allowing space for `n` integers.
4. The system shall allow user input to populate the array via a loop iterating `n` times.
5. The system shall print the contents of the array after the first population.
6. The system shall allow the value of `n` to be modified to 10.
7. The system shall resize the memory allocated for `ptr` using `realloc` to hold 10 integers.
8. The system shall allow user input to populate the resized array via a loop iterating `n` times.
9. The system shall print the contents of the resized array after the second population.
10. The system shall ensure proper memory management by freeing the allocated memory before exiting.