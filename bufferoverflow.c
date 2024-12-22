#include <stdio.h>
#include <string.h>

int main() {
    char realpasswd[10];
    char givenpasswd[10]; //Buffer 
    

    strncpy(realpasswd, "dddddddddd", 10); //Assign a string to the variable.
    printf("Enter the passwd\n");
    gets(givenpasswd); //get the user input

    //compare the string 
    if (0 == strncmp(givenpasswd, realpasswd, 10)) {
        printf("\n*****! Access Granted !*****");
    } else {
        printf("\nAccess Denied 403!");
    }

}

/**
 * Explanation
 * 
 * 1. gets() is a unbounded function that simply reads the text not the size of memory.
 *    This can lead to Bufferoverflow .
 * 
 * 2. The strings realpasswd and givenpasswd are stored nearer to one by one in the stack.
 * 
 * 3. So when the user gives more than 20 charactrers instead of 10 it will the overwrite the realpasswd.
 * 
 */