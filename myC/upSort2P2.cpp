#include <iostream>
using namespace std;

// ���׷��̵�� ����: (1) �Լ��� �����
int *upSort(int *array, int len) {

    for (int h = 0; h < len; h++) {
        for (int i = len-1; i > h; i--) {
            if (array[i] < array[i-1]) {
                int exc = array[i-1];
                array[i-1] = array[i];
                array[i] = exc;
            }
        }
    }
    return array;
    
}
int main() {
    int array[5] = {10, 36, 25, 81, 64};
    for (int i = 0; i < 5; i++) cout << upSort(array, 5)[i] << " ";
}