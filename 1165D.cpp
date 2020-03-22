#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define append(x) push_back(x);

vector <long long int> hh;

void printDivisors(ll n)
{

    // Note that this loop runs till square root
    for (int i=1; i<=sqrt(n); i++)
    {

        if (n%i == 0)
        {
            // If divisors are equal, print only one
            if (n/i == i)
                hh.append(i)

            else // Otherwise print both
                {
                    hh.append(i)
                    hh.append(n/i)
                }
        }
    }
}

main()
{
    ll t,n,a[1000],kk,flag;
    cin>>t;
    while(t--)
    {
        hh.clear();
        cin>>n;
        for(ll i=0;i<n;i++)
        {
            cin>>a[i];
        }
        sort(a,a+n);
        kk=a[0]*a[n-1];
        //print(kk)
        printDivisors(kk);
        sort(hh.begin(),hh.end());
        flag=1;
        if((hh.size())==n+2)
        {
            flag=0;
        for(ll i=0;i<n;i++)
        {
            if (a[i]!=hh[i+1])
                flag=1;
        }}
        if(flag==0)
            cout<<kk<<"\n";
        else
            cout<<"-1"<<"\n";
    }
}