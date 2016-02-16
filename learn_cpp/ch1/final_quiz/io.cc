#include <iostream>

using namespace std;

int readNumber() {
    cout << "Enter a number\n";
    int num;
    cin >> num;
    return num;
}

void writeAnswer(int num) { 
    cout << num << endl; 
}