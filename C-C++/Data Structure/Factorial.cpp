#include<iostream>
using namespace std;

int Factorial(int x)
{
    int Multiply = 1, i , temp=0 ;

    for(int i =0 ;i<x ;i++)
    {
        temp = x-i;
        Multiply = Multiply*temp;
    }

    cout<<"Factorial Of a Number "<<x<<" is : "<<Multiply;


}



int main()
{   int a;
    cout<<"Enter The Number You Want To Factorial: " ;
    cin>>a;
    Factorial(a);
}
