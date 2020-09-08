#include <iostream>
using namespace std;

int main () {
    int array[5] = {12, 16, 15, 13, 18};
    
    for (int h = 0; h < 5; h++) {
        for (int i = 5; i > h; i--) {
            if (array[i] < array[i-1]) {
                int exc;
                exc = array[i-1];
                array[i-1] = array[i];
                array[i] = exc;
            }
        }
    }
    for (int i = 0; i < 5; i++) cout << array[i] << " ";
}