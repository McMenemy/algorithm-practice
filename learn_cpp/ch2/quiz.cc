#include <iostream>

int main() {
    using namespace std;
    
    cout << "Enter a number less than 5 and see if it is prime\n";
    
    int num;
    cin >> num;
    
    bool prime(false);
    
    if (num == 2) 
      prime = true;
    else if (num == 3)
      prime = true;
    
    if (prime) 
      cout << "the number is prime\n";
    else
      cout << "the number is not prime\n";
    
}