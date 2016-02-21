#include <iostream>

double calcNums() {
    using namespace std;
    
    cout << "Choose first number: \n";
    double num1;
    cin >> num1;
    
    cout << "Choose second number: \n";
    double num2;
    cin >> num2;
    
    
    cout << "Choose 1 operation (+, -, *. /): \n";
    char operation;
    cin >> operation;
    
    if (operation == '+')
        return num1 + num2;
    else if (operation == '-')
        return num1 - num2;
    else if (operation == '*')
        return num1 * num2;
    else if (operation == '/')
        return num1 / num2;
    else 
        return -1;
}