#include <iostream>
#include "add.h"
#include "subtract.h"

int main() {
    using namespace std;
    int x = mySubtract(6, 5);

    cout << "3 - 4 = " << mySubtract(3, 4) << endl;
    cout << "3 + 4 = " << myAdd(3, 4) << endl;
    
}
