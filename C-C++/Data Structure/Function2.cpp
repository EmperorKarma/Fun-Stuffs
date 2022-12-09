#include<iostream>
using namespace std;

int Sum(int x, int y);
int Palindrome(int num)
{
    int temp, rev = 0, rem, a ;
    temp = num;
    while(temp>0)
    {
        rem = temp%10;
        rev = (rev*10) + rem ;
        temp = temp/10;
    }

     if(rev==num)
     {

         cout<<"Palindrome Number: "<<rev;
     }
     else
     {
         Sum(rev , num);

     }

}


int Sum(int q, int r)
{

}

int main()
{   int a;
    cout<<"Enter The No. :" ;
    cin>>a;

    Palindrome(a);
}



