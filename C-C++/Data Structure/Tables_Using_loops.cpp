#include<iostream>
using namespace std;
int Tables(int X)
{
    int Multiply;
   for(int i = 0; i<11 ; i++)
   {
       Multiply = X*i;
       cout<<X<<" * "<<i<<" = "<<Multiply<<endl;
   }
}

int main()
{   int x;
    cout<<"Enter The Number Table You want : " ;
    cin>>x;
    Tables(x);
}
