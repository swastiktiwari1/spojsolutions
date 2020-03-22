#include<bits/stdc++.h>
using namespace std;
main()
{
    unsigned long long int n,k,l;
    cin>>n>>k;
    l=ceil((1.0*n*8)/k)+ceil((1.0*n*5)/k)+ceil((1.0*n*2)/k);
    cout<<l;
}