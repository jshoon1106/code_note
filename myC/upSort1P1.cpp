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