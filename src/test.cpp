#include "iostream"

using namespace std;

void func(int a, int b, int c=3, int d=4)
{
    cout << a << ", " << b << ", " << c << ", " << d << endl;
}

void test()
{
    func(1,2);
}

