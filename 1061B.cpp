#include<bits/stdc++.h>
using namespace std;
main()
{
    long long int n,m,i,x,s=0,l,k,d,u=0;
    cin>>n>>m;
    vector <long long int> v;
    for(i=0;i<n;i++)
    {
        cin>>x;
        v.push_back(x);
        s+=x;
    }
    sort(v.begin(),v.end());
    l=0;k=0;d=0;
    for(i=0;i<n;i++)
    {
        l=v[i];
        d+=v[i]-u;
        if (d<=i)
        d+=1;
        u=v[i];
    }
    cout<<s-d;
    
}