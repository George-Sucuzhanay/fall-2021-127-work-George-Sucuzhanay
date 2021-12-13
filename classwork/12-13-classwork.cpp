// Exam Info
// Python (60%)

// answers.py
// convert binary => decimal
// create a program or by hand


// C++ (30%)
// Last commit for take-home final will be before the final start on Thursday 11:30am

// main w/ one function and another inside it

// Extras (105)

#include <iostream>

void if_example() {
    int a;
    a = 6;
    if (a > 5) {
       std::cout << " a is greater than 5\n ";
       std::cout << "This is also in the if\n";
    } 
    else if (a == 4) {
       std::cout << " a is 4\n";
    }
    else{
       std::cout << "This is in the else\n";
       std::cout << "so is this\n";
    }
    std::cout << "after the if\n";
}

void while_example() {
    int i;
    i = 0;
    while (i < 10) {
        std::cout << i << std::endl;
        i = i + 1;
        if (i == 10) {
            break;
            // break exits the loop imediately
            // if we return in here it would have
            // returned imediately
        }
    }
    std::cout << "this is after the loop\n";
}
void do_example() {
    int i = 10;
    do {
        std::cout << i << std::endl;
        i--;
    } while (i > 0);
}
// this is the for COUNTING loop
void for_example() {
    // for (start value; boolean test; change expression)
    int i;
    for(i = 0; i < 10; i = i + 1) {
        std::cout << i << "\n";
    }
    std::cout << "\n\n";

    // notice we can declare the variable in the for 
    // but it will be created when the for excutes
    // and it will be destroyed when the loop exits
    for (int a = 10; a > 0 ; a = a - 2){
        std::cout << "a is " << a << "\t";
    }
    std::cout << "\n";
}
int main()
{
    /*
    if (boolean)
        statement
    */
   // if_example();
   // while_example();
   // do_example();
   for_example();
   return  0;
}
