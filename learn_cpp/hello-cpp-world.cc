#include <iostream>
using namespace std;

int main() {
    cout << "Hello World!!!\n";
    
    int array[4] = {2, 1, 4, 3};
    int length = sizeof(array) / sizeof(array[0]);
    cout << "array length " << length << " testing" << endl; 
}
