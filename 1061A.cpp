#include<bits/stdc++.h>
using namespace std;
main()
{
    long long int n,s;
    cin>>n>>s;
    if (s%n==0)
    cout<<s/n;
    else
    cout<<(s/n)+1;
}