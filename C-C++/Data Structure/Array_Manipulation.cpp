#include<iostream>
using namespace std;

int main()
{   int i,j,first, second , sum = 0;
    cin>>i;
    int arr[i];

    for(j=0;j<i;++j)
    {
        cin>>arr[j];

    }


    cin>>first;
    arr[j] = arr[first];
    cin>>second;
    arr[j] =  arr[second];
    sum = arr[first]+arr[second];

    cout<<sum;

}
