// https://www.hackerrank.com/challenges/linkedin-practice-dynamic-programming-lcs/problem
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
// int power(int x, unsigned int y){int res = 1;while (y > 0){ if (y & 1){res = res*x;} y = y>>1;x = x*x;}return res;}
// int powermod(int x, unsigned int y, int p){int res = 1;x = x % p;while (y > 0){if (y & 1){res = (res*x) % p;}y = y>>1; x = (x*x) % p;}return res;}
#define print2d(mat,n,m){for(int i=0;i<(int)(n);i++){for(int j=0;j<(m);j++){cout<<mat[i][j]<<" ";}cout<< endl;}}
#define print1d(mat,n){for(int i=0;i<(int)(n);i++)cout<<mat[i]<<" ";cout<<endl;}
#define clr(a,x) memset(a,x,sizeof(a))
#define rr(v) for(auto &val:v)
#define print(v) for (const auto itr : v){cout<<itr<<' ';}cout<<endl;
#define init(v,x) for (auto &itr:v){itr=x;}
#define minpq(x) x,vector<x>,greater<x>
#define ln length()
#define sz size()
#define inf 1e18;
#define elif else if

int32_t main()
{
    fastIO
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    // #endif

    int dp[130][130],n,m;
    clr(dp,0);
    int s1[104],s2[110];
    cin>>n>>m;
    rep(i,0,n)
    {
        cin>>s1[i];
    }
    rep(i,0,m)
    {
        cin>>s2[i];
    }
    rep(i,0,n)
    {
        rep(j,0,m)
        {
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j]);
            if(s1[i]==s2[j])
            {
                dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+1);
            }
        }
    }
    // print2d(dp,n+1,m+1)
    int i=n;
    int j=m;
    // cout<<dp[i][j]<<endl;
    vector<int> st;
    while(i>0 && j>0)
    {
        if(s1[i-1]==s2[j-1])
        {
            // i-=1;
            j-=1;
            i-=1;
            // j-=1;
            st.pub(s2[j]);
        }
        elif(dp[i-1][j]>dp[i][j-1] )
        {
            // i-=1;
            i-=1;
            // st.pub(s1[i]);
        }
        else
        {
            j-=1;
            // j-=1;
        }
        
    }
    reverse(st.begin(),st.end());
    print(st)

}
