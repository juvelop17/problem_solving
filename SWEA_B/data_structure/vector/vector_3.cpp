#include <iostream>

using namespace std;

template <class T>
class _vector {
public:
    int _size;
    int capacity;
    T *arr;

    _vector(){
        _size = 0;
        capacity = 32;
        arr = new T[capacity];
    }
    ~_vector() {
        delete[] arr;
    }

    void clear(){
        delete[] arr;
        _size = 0;
        capacity = 32;
        arr = new T[capacity];
    }
    void resize(int k){
        T *temp = new T[k]; 
        for(int i=0;i<_size;i++){
            temp[i] = arr[i];
        }
        delete[] arr;
        arr = temp;
        _size = capacity = k;
    }
    int size(){
        return _size;
    }
    T* front(){
        return &arr[0];
    }
    T* back(){
        return &arr[_size - 1];
    }
    void push_back(T t){
        if (_size == capacity){
            resize(_size * 2);
            _size /= 2;
        }
        arr[_size++] = t;
    }
    void pop_back(){
        _size--;
    }
    T& operator[](int k){
        return arr[k];
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
