#include <iostream>

int main()
{
    int a,b;
    int c;
    int d;

    a = 20;
    b = 30;
    c = a + b;
    d = 50;

    std::cout << "Hello World!" << std::endl;
    std::cout << a << " + " << b << " = " << c << "\n";
    std::cout << d << " / " << c << " = " << d / c << "\n";
    std::cout << "My first C++ program!" << "\n";
    return 0;
} 
// To complie a C++ program do the following:
    // 1) g++ hello.cpp
    // 2) ./a.out 
// To change a.out do the following:
    // 1) rm a.out  (if you already created a a.out)
    // 2) g++ -o name name.cpp
    // 2) ./name
    // 3) check by doing an ls command