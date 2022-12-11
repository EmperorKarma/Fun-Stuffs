#include<iostream>
using namespace std;
void SPyr(int x)
{
    int a ,j;

    for(a=0;a<=x;a++)
    {
        for(j=0;j<=a;j++)
        {

             cout<<"@ ";
        }
           cout<<endl;
    }


}

int main()
{
    int a;
    cout<<"Enter the Number of Pattern You want : " ;
    cin>>a;
    SPyr(a);

}


