#include <cstdio>
#include <iostream>
// library with advanced tools ???? similar to Python

int main()
{
    int a = 20;
    int b,c;
    char letter;
    bool tf;
    double decnumber; // used for decimal numbers aka floats

    decnumber = 1.0/3.0;

    tf = false;
    letter = 'x';

    c = 10;
    b = a+c;
    std::cout << "b = " << b << "\n";
    // => 1/3 will be INTEGER b/c 1 and 3 are integers
    std::cout << "testing floats: " << decnumber << "\n";
    std::cout<< tf << "" << letter << " " << "b = " << b << "\n";
    std::cout << "Hello World!" << std::endl;
    return 0;

    // Make sure to initalize your variable b/c they the variable not 
    // used will store a randomized integer

    // You need to explictly include the type of each data type
    // Can't mix and match data types

    // To run you do ./compliername

    // For assignment for C++
    // ONLY PUSH THE C++ FILES TO GITHUB NOT THE A.OUT COMPLIER FILE!!!!

}