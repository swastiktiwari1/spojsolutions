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
#define all(v) (v).begin(), (v).end()
#define rep(i, l, r) for(int i=(int)(l);i<(int)(r);i++)
#define repd(i, l, r) for (int i=(int)(l);i>=(int)(r);i--)
int power(int x, unsigned int y){int res = 1;while (y > 0){ if (y & 1){res = res*x;} y = y>>1;x = x*x;}return res;}
int powermod(int x, unsigned int y, int p){int res = 1;x = x % p;while (y > 0){if (y & 1){res = (res*x) % p;}y = y>>1; x = (x*x) % p;}return res;}
#define print2d(mat,n,m){for(int i=0;i<(int)(n);i++){for(int j=0;j<(m);j++){cout<<mat[i][j]<<" "<< "endl"[j == m];}}}
#define print1d(mat,n){for(int i=0;i<(int)(n);i++)cout<<mat[i]<<" ";cout<<endl;}
#define clr(a,x) memset(a,x,sizeof(a))
#define rr(v) for(auto &val:v)
#define print(v) for (const auto itr:v){cout<<itr<<' ';}cout<<endl;
#define init(v,x) for (auto &itr:v){itr=x;}
#define minpq(x) x,vector<x>,greater<x>
#define ln length()
#define sz size()
main()
{
//#ifndef ONLINE_JUDGE
  //  freopen("sic_in.txt", "r", stdin);
    //freopen("sic_out.txt", "w", stdout);
//#endif
string s;
cin>>s;
int i=0,j=1;
int n=s.sz;
int dp[100005]={0};
string ans;
ans=s;
while (j<n){
    if (s[i]=='1' and s[j]=='0')
     {   dp[i]=1;
        dp[j]=1;
     //  # print(i,j)
        if (i>0 and j<n)
           { while (dp[i]==1 and i>0)
                i-=1;}
        j+=1;}
    else{
        j+=1;
        i=j-1;}}
rep(i,0,n)
{
    if(dp[i]==0)
    {
        ans[i]='0';
    }
}
cout<<ans<<endl;
}