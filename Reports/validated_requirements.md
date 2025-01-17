1. The system shall declare an integer variable `n` to hold the size of the array, initialized to 5. (Currently initialized to 10)
2. The system shall declare a pointer `ptr` to hold the address of dynamically allocated memory.
3. The system shall allocate memory for `ptr` using `calloc`, allowing space for `n` integers. (Currently uses `malloc`)
4. The system shall allow user input to populate the array via a loop iterating `n` times. (Currently uses a formula instead of user input)
5. The system shall print the contents of the array after the first population.
6. The system shall allow the value of `n` to be modified to 10. (Currently modifies `n` to 15)
7. The system shall resize the memory allocated for `ptr` using `realloc` to hold 10 integers.
8. The system shall allow user input to populate the resized array via a loop iterating `n` times. (Again, uses a formula instead of user input)
9. The system shall print the contents of the resized array after the second population.
10. The system shall ensure proper memory management by freeing the allocated memory before exiting. (Currently does not free memory)