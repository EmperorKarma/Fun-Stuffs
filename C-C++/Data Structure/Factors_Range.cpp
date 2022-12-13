#include<iostream>
using namespace std;
int Factor(int x)
{
    int i;

    cout << "Factors of " << x << " are: ";
    for(i = 1; i <= x; ++i) {
        if(x % i == 0)
            cout << i << " ";
    }
    cout<<endl;

    return 0;

}
int Range(int a, int b)
{

    for(int i=a;i<=b;i++)
    {

        Factor(a);
        a++;
    }
}

int main()
{
   int c,d;
   cout<<"Enter The initial Range You Want the Factors : ";
   cin>>c;
   cout<<"The Enter The Final Range You Want To Factors : " ;
   cin>>d;
   Range(c,d);
}




