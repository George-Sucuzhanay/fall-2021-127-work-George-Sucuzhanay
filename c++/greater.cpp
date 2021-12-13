// This program will have a function ~int greater(int a, int b)~ that 
    // will return the larger of the two parameters a and b. 
// It will also have a function ~int greater3(int a, int b, int c)~ 
    // which will return the largest of the three parameters. 

// Your program should use input to take in 3 integer values (using std::cin) and print out results to show the functions work.

#include <iostream>
int greater(int a, int b)
{
    if (a < b) 
    {
       return b;
    }
    else if (a > b) 
    {
       return a;
    }
    return 0;
}
int greater3(int a, int b ,int c)
{
    if (a > b  && a > c )
    {
        return a;
    }
    else if (b >  a && b > c)
    {   
        return b;
    }
    else 
    {
        return c;
    }
    return 0;
}

int main()
{
    std::cout<< greater(2,3)<< std::endl;
    
    int num1, num2, num3;
    std::cout<<"Enter value for first number: ";
    std::cin>> num1;
    std::cout<<"Enter value for second number: ";
    std::cin>> num2;
    std::cout<<"Enter value for third number: ";
    std::cin>>num3;
    std::cout << "You entered " << num1 << " , " << num2 << " , and " << num3 << ".\n";
    std::cout << "The greatest integer is " << greater3(num1, num2, num3) << "." << std::endl;
}