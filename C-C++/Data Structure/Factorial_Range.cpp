#include<iostream>
using namespace std;

int Factorial(int x)
{
    double Multiply = 1, i , temp=0 ;

    for(int i =0 ;i<x ;i++)
    {
        temp = x-i;
        Multiply = Multiply*temp;
    }

    cout<<"Factorial Of a Number "<<x<<" is : "<<Multiply<<endl;


}

int Range(int a, int b)
{
    for(int i=a;i<=b;i++)
    {

        Factorial(a);
        a++;
    }
}



int main()
{   int l,k;
    cout<<"Enter The Number You Want To Factorial: " ;
    cin>>l>>k;
    Range(l,k);
}

