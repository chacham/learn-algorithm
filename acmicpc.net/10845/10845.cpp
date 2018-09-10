#include <iostream>
#include <string>

using namespace std;

class queue {
public:
    queue(int size){
        _start = 0;
        _end = -1;
        _length = 0;
        _size = size;
        _queue = new int[this->_size];
    }
    void enqueue(int item){
        if (_size <= _length) {
            return;
        }
        _end++;
        _end %= _size;
        _queue[_end] = item;
        _length++;
    }
    int dequeue(){
        if (_length <= 0) {
            return -1;
        }
        int ret = _queue[_start];
        _start++;
        _start %= _size;
        _length--;
        return ret;
    }
    int size(){
        return _length;
    }
    int empty(){
        return _length ? 0 : 1;
    }
    int front(){
        if (_length) {
            return _queue[_start];
        }
        return -1;
    }
    int back(){
        if (_length) {
            return _queue[_end];
        }
        return -1;
    }
private:
    int * _queue;
    int _start, _end, _length, _size;
};

int main(){
    int N;
    cin >> N;

    queue myqueue(N);

    string s;
    int tmp;
    for (int i = 0; i < N; i++){
        cin >> s;

        if (s.compare("push") == 0) {
            cin >> tmp;
            myqueue.enqueue(tmp);
        } else if (s.compare("pop") == 0) {
            cout << myqueue.dequeue() << endl;
        } else if (s.compare("size") == 0) {
            cout << myqueue.size() << endl;
        } else if (s.compare("empty") == 0) {
            cout << myqueue.empty() << endl;
        } else if (s.compare("front") == 0) {
            cout << myqueue.front() << endl;
        } else if (s.compare("back") == 0) {
            cout << myqueue.back() << endl;
        }
    }
    
    return 0;
}
