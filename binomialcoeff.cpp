#include<bits/stdc++.h>
#include<string>
using namespace std;
#define fastIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define int long long int
#define fi first
#define se second
#define pub push_back
#define mkp make_pair
#define pi pair<int,int>0
#define push push
#define all(v) (v).begin(), (v).end()
#define rep(i, l, r) for(int i=(int)(l);i<(int)(r);i++)
#define repd(i, l, r) for (int i=(int)(l);i>=(int)(r);i--)
int power(int x, unsigned int y){int res = 1;while (y > 0){ if (y & 1){res = res*x;} y = y>>1;x = x*x;}return res;}
int powermod(int x, unsigned int y, int p){int res = 1;x = x % p;while (y > 0){if (y & 1){res = (res*x) % p;}y = y>>1; x = (x*x) % p;}return res;}
#define print2d(mat,n,m){for(int i=0;i<(int)(n);i++){for(int j=0;j<(m);j++){cout<<mat[i][j]<<" ";}cout<< endl;}}
#define print1d(mat,n){for(int i=0;i<(int)(n);i++)cout<<mat[i]<<" ";cout<<endl;}
#define clr(a,x) memset(a,x,sizeof(a))
#define rr(v) for(auto &val:v)
#define print(v) for (const auto itr : v){cout<<itr<<' ';}cout<<endl;
#define init(v,x) for (auto &itr:v){itr=x;}
#define ln length()
#define sz size()
#define endl "\n"
#define inf 1e18;
#define elif else if
int dsu[100005];
int rank1[100005];
int bc(int n,int k)
{
    if(k==0 || k==n)
    {
        return 1;
    }
    else
    {
        return bc(n-1,k)+bc(n-1,k-1);
    }
    
}

int32_t main()
{
    // fastIO
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
    #endif
   int pt[105][105];
   clr(pt,0);
   rep(i,0,100)
   {
       rep(j,0,i+1)
       {
           if(j==0 || j==i)
           {
               pt[i][j]=1;
           }
           else
           {
               pt[i][j]=pt[i-1][j]+pt[i-1][j-1];
           }
           
       }
   }
   print2d(pt,10,10)
   int dp[100];
   int n,k;
   cin>>n>>k;
//    int dp[100];
   clr(dp,0);
   dp[0]=1;
   rep(i,0,n+1)
   {
       repd(j,i,1)  
       {
           dp[j]+=dp[j-1];
       }
   }
   cout<<dp[k]<<endl;
   cout<<bc(n,k)<<endl;

}
