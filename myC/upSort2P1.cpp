#include <iostream>
using namespace std;

// ���׷��̵�� ����: (1) �迭�� �� ���� ����ڰ� ���� �Է�
int main() {
    int len;
    cout << "�� ���� ���ڸ� �����ϰ� �����ʴϱ�? ";
    cin >> len;
    int *array = new int[len];

    for (int i = 0; i < len; i++) {
        cout << i+1 << "��° ��: ";
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