// 4) Write a function called doubleNumber() that takes one integer parameter and returns twice the value passed in.

// 5) Write a complete program that reads an integer from the user (using cin, discussed in lesson 1.3a -- A first look at cout, cin, endl, namespaces, and using statements), doubles it using the doubleNumber() function you wrote for question 4, and then prints the doubled value out to the console.

// 1.4a — A first look at function parameters and arguments
#include <iostream>
using namespace std;

int doubleNumber(int num);
void doubleUserInput();

int main() {
    cout << doubleNumber(5) << endl;
    doubleUserInput();
}

int doubleNumber(int num) {
    return num + num;
}

void doubleUserInput() {
    cout << "Input a number to get dobled\n";
    int num;
    cin >> num;
    cout << doubleNumber(num) << endl << endl;
}