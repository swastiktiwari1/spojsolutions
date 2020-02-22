#include<bits/stdc++.h>
#include<string.h>
using namespace std;
#define fastIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define int long long int
#define fi first
#define se second
#define pub push_back
#define mkp make_pair
#define pi pair<int,int>
#define push push
#define all(v) (v).begin(), (v).end()
#define rep(i, l, r) for(int i=(int)(l);i<(int)(r);i++)
#define repd(i, l, r) for (int i=(int)(l);i>=(int)(r);i--)
int power(int x, unsigned int y){int res = 1;while (y > 0){ if (y & 1){res = res*x;} y = y>>1;x = x*x;}return res;}
int powermod(int x, unsigned int y, int p){int res = 1;x = x % p;while (y > 0){if (y & 1){res = (res*x) % p;}y = y>>1; x = (x*x) % p;}return res;}
#define print2d(mat,n,m){for(int i=0;i<(int)(n);i++){for(int j=0;j<(m);j++){cout<<mat[i][j]<<" "<< "endl";}}}
#define print1d(mat,n){for(int i=0;i<(int)(n);i++)cout<<mat[i]<<" ";cout<<endl;}
#define clr(a,x) memset(a,x,sizeof(a))
#define rr(v) for(auto &val:v)
#define print(v) for (const auto itr : v){cout<<itr<<' ';}cout<<endl;
#define init(v,x) for (auto &itr:v){itr=x;}
#define minpq(x) x,vector<x>,greater<x>
#define ln length()
#define sz size()
#define inf 1e18;
int dsu[100005];
int rank1[100005];
int fin(int x)
{
    while (dsu[x]!=x)
    {
        dsu[x]=dsu[dsu[x]];
        x=dsu[x];
    }
    return x;
}
void unio(int a, int b)
{
    int fa=fin(a);
    int fb=fin(b);
    if (rank1[fa]>rank1[fb])
    {
        dsu[fb]=fa;
    }
    else if (rank1[fb]>rank1[fa])
    {
        dsu[fa]=fb;
    }
    else
    {
        dsu[fb]=fa;
        rank1[fa]+=1;
    }
}
int32_t main()
{
    int n,m,u,v;
    cin>>n>>m;
    if(n!=m+1)
    {
        cout<<"NO";
        exit(0);
    }
    else
    {
        int flag=0;
        clr(rank1,0);
        rep(i,0,n)
        {
            dsu[i]=i;
        }
        rep(i,0,m)
        {
            cin>>u>>v;
            if(fin(u)==fin(v))
            {
                flag=1;
            }
            else
            {
                unio(u,v);
            }
        }
        if(flag==1)
        cout<<"NO";
        else
        cout<<"YES";
        
    }
}
