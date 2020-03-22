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
int ans[10005];
int visited[10005];
vector < pair<int,int> > adj[10005];
void dfs(int s)
{
    visited[s]=1;
    rr(adj[s])
    {
        
        if (visited[val.fi]==0)
        {
            ans[val.se]=1;
             dfs(val.fi);
            
        }
        if (visited[val.fi]==2)
        {
            ans[val.se]=1;
        }
        else
        {
            ans[val.se]=2;
        }
    }
    visited[s]=2;
    
}
int32_t main()
{
    int n,m,a,b;
    cin>>n>>m;
    rep(i,0,m)
    {
        ans[i]=2;
    }
    rep(i,0,m)
    {
        cin>>a>>b;
        adj[a-1].pub({b-1,i});
    }
    clr(visited,0);
    rep(i,0,n)
    {
        if(!visited[i])
            dfs(i);
    }
    int ma=1;
    rep(i,0,m)
    {
        ma=max(ma,ans[i]);
    }
    cout<<ma<<endl;
    print1d(ans,m)
}