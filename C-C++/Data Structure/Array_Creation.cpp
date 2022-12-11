#include<iostream>
using namespace std;
int main()
{
    int input ;
    cout<<"Enter The Length of the Array : ";
    cin>>input;
    int num[input];
     cout<<"Enter The Values in the Array: ";
    for(int j=0;j < input;++j)
    {

        cin>>num[j];
    }
    cout<<"The Numbers are : ";

    for(int k =0;k < input;++k)
    {
        cout<<endl<<num[k]<<" "<<endl;
    }




}
