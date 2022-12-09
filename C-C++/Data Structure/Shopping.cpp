#include<iostream>
using namespace std;
int Pencil(int x)
{
    int  sum = 0 , Discount , Total_Amount;
    sum = (x + sum)*1;
    Discount = x/12;
    Total_Amount = sum-1*(Discount);
    cout<<"Total Amount : "<<sum<<endl<<"Discount :"<<1*(Discount)<<endl<<"Total Amount Paid By The Customer :"<<Total_Amount<<endl;
    return Total_Amount;
}

int Eraser(int y)
{
    int  sum = 0 , Discount , Total_Amount;
    sum = (y + sum)*10;
    Discount = y/6;
    Total_Amount = sum-2*(Discount);
    cout<<"Total Amount : "<<sum<<endl<<"Discount :"<<2*(Discount)<<endl<<"Total Amount Paid By The Customer : "<<Total_Amount<<endl;
    return Total_Amount;
}

int Pens(int z)
{
    int  sum = 0 , Discount , Total_Amount;
    sum = (z + sum)*20;
    Discount = z/6;
    Total_Amount = sum-3*(Discount);
    cout<<"Total Amount : "<<sum<<endl<<"Discount :"<<3*(Discount)<<endl<<"Total Amount Paid By The Customer :"<<Total_Amount<<endl;
    return Total_Amount;
}
int main()
{    int x,y,z, x1,y1,z1;
    cout<<"Enter The Number of Pencils You Want: ";
    cin>>x;
    cout<<"Enter The Number of Eraser You want: ";
    cin>>y;

    cout<<"Enter The Number Of Pens you Want: ";
    cin>>z;

    x1 = Pencil(x);
    y1 = Eraser(y);
    z1 = Pens(z);
    cout<<endl<<"Total Number of Money You Paid :"<<x1+y1+z1;



}
