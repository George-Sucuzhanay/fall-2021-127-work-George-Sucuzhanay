#include <iostream>
#include <stdlib.h>

int main() {
    srand(time(NULL));

    // show that we can generate random numbers
    // between 0 and 99 inclusive
    // for (int i = 0; i < 10; i++) {
    //     std::cout << rand()%100 << "\n";
    // }
    int answer = rand()%100;
    int guess = answer + 1;

    // get the first guess
    std::cout << "Enter a guess: ";
    std::cin >> guess;
    int guesses = 1;

    while (guess != answer){
        // give a hint
        if (guess < answer){
            std::cout << "Too Low!\n";
        }
        else{
            std::cout << "Too High!\n";
        }
        // get the next guess
        std::cout << "Enter a new guess: ";
        std::cin >> guess;
        guesses = guesses + 1;
    }   
    std::cout << "You got it !!!\n";
    std::cout << "It took you " << guesses << " guesses.\n";
    return 0;
}