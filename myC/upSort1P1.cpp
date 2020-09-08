#include <iostream>
using namespace std;

// 업그레이드된 내용: (1) 배열에 들어갈 수를 사용자가 직접 입력
int main() {
    int len;
    cout << "몇 개의 숫자를 정렬하고 싶으십니까? ";
    cin >> len;
    int *array = new int[len];

    for (int i = 0; i < len; i++) {
        cout << i+1 << "번째 수: ";
        cin >> array[i];
    }

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
    for (int i = 0; i < len; i++) cout << array[i] << " ";
    delete []array;
}