#include <iostream>
using namespace std;

// 업그레이드된 내용: (1) 함수로 만들기
int *upSort(int *array, int len) {
    for (int i = 0; i < len-1; i++) {
        int minIndex = i;
        int exc;
        for (int j = i+1; j < len; j++) {
            if (array[minIndex] > array[j]) minIndex = j;
        }
        exc = array[i];
        array[i] = array[minIndex];
        array[minIndex] = exc;
    }
    return array;
}

int main() {
    int array[5] = {15,36,85,97,25};
    for (int i = 0; i < 5; i++) cout << upSort(array, 5)[i] << " ";
}