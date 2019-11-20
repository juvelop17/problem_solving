#include <iostream>

using namespace std;

template <class T>
class _vector {
public:
    int _size;
    int capacity;
    T *arr;
    _vector() {
        _size = 0;
        capacity = 32;
        arr = new T[capacity];
    }    
    ~_vector(){
        delete[] arr;
    }
    void clear(){
        delete[] arr;
        _size = 0;
        capacity = 32;
        arr = new T[capacity];
    }
    void resize(int k) {
        T *temp;
        temp = new T[k];
        for(int i=0;i<_size;i++){
            temp[i] = arr[i];
        }
        delete[] arr;
        arr = temp;
        _size = capacity = k;
    }
    int size() const{
        return _size;
    }
    T* begin() const{
        return &arr[0];
    }
    T* end() const{
        return &arr[0] + _size;
    }
    void push_back(T val) {
        if (_size == capacity) {
            resize(_size * 2);
            _size /= 2;
        }
        arr[_size++] = val;
    }
    void pop_back() {
        _size--;
    }
    T& operator [](int idx) {
        return arr[idx];
    }
    // T operator [](int idx)const{
    //     return arr[idx];
    // }
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
    cout << "vec.begin() : " << vec.begin() << endl;
    cout << "vec.end() : " << vec.end() << endl;

    vec.resize(5);
    cout << "vec.size() : " << vec.size() << endl;

    return 0;
}

