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
    
    for (int h = 0; h < len; h++) {
        for (int i = len; i > h; i--) {
            if (array[i] < array[i-1]) {
                int exc = array[i-1];
                array[i-1] = array[i];
                array[i] = exc;
            }
        }
    }
    for (int i = 0; i < len; i++) cout << array[i] << " ";
    delete []array;
}