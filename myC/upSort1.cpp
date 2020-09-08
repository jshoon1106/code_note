#include <iostream>
using namespace std;

int main() {
    int array[5] = {2, 8, 6, 4, 7};

    for (int i = 0; i < 4; i++) {
        int minIndex = i;
        int exc;
        for (int j = i+1; j < 5; j++) {
            if (array[minIndex] > array[j]) minIndex = j;
        }
        exc = array[i];
        array[i] = array[minIndex];
        array[minIndex] = exc;
    }
    for (int i = 0; i < 5; i++) cout << array[i] << " ";
}