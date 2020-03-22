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
#define elif else if
int32_t main()
{
    fastIO
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    // #endif
    int n,k;
    cin>>n>>k;
    string arr[10004],fi,fj;
    unordered_set <string> s;
    map<char,int> m;
    rep(i,0,n)
    {
        cin>>arr[i];
        s.insert(arr[i]);
    }
    int ans=0;
    rep(i,0,n)
    {
        fi=arr[i];
        rep(j,i+1,n)
        {
            fj=arr[j];
            string lol="";
            rep(p,0,k)
            {
                if (fi[p]==fj[p])
                {
                    lol+=fi[p];
                }
                else
                {
                    m[fi[p]]=1;
                    m[fj[p]]=1;
                    if(!m['S'])
                    {
                        lol+="S";
                    }
                    else if(!m['E'])
                    {
                        lol+="E";
                    }
                    else
                    {
                        lol+="T";
                    }
                    m[fi[p]]=0;
                    m[fj[p]]=0;
                    
                }
                
            }
            // cout<<lol<<endl;
            if(s.find(lol)!=s.end())
            {
                ans+=1;
            }
            
        }
        s.erase(fi);
    }
    cout<<ans/2<<endl;
    
}