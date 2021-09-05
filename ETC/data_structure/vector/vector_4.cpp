#include <iostream>

using namespace std;


template<class T>
class _vector {
public:
    int capacity;
    int _size;
    T *arr;

    _vector() : capacity(1000), _size(0) {
        arr = new T[capacity];
    }
    ~_vector() {
        delete[] arr;
    }

    void resize(int k) {
        T *tmp = new T[k];
        for (int i=0;i<k;i++){
            tmp[i] = arr[i];
        }
        delete[] arr;
        arr = tmp;
        capacity = _size = k;
    }
    void push_back(T d) {
        if (_size == capacity) {
            resize(_size * 2);
            _size /= 2;
        }
        arr[_size++] = d;
    }
    void pop_back(){
        _size--;
    }
    int size(){
        return _size;
    }
    T* front() {
        return &arr[0];
    }
    T* back() {
        return &arr[_size - 1];
    }
    T& operator[](int k) {
        return arr[k];
    }
    void clear() {
        delete[] arr;
        _size = 0;
        capacity = 100;
        arr = new T[capacity];
    }

};




int main() {
    _vector<int> vec;
    
    vec.push_back(1);
    cout << "vec[0] : " << vec[0] << endl;
    vec[0] = 2;
    cout << "vec[0] : " << vec[0] << endl;

    vec.push_back(3);
    cout << "vec.size() : " << vec.size() << endl;
    
    vec.pop_back();
    cout << "vec.size() : " << vec.size() << endl;

    vec.clear();
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(3);
    cout << "vec.size() : " << vec.size() << endl;
    cout << "vec.front() : " << *vec.front() << endl;
    cout << "vec.back() : " << *vec.back() << endl;

    vec.resize(5);
    cout << "vec.size() : " << vec.size() << endl;

    return 0;
}






