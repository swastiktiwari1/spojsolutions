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
int32_t main()
{
    int n,s1[505],s2[505],temp;
    int su=0;
    vector < pair < int , pair <int,int> > > lol;
    string s;
    cin>>n;
    cin>>s;
    rep(i,0,n)
    {
        if(s[i]==')')
        s1[i]=-1;
        else
        s1[i]=1;
        su+=s1[i];
    }
    if(su==0)
    {
        rep(i,0,n)
        {
            rep(j,0,n)
            {
                rep(k,0,n)
                {
                    s2[k]=s1[k];
                }
                s2[i]=s1[j];
                s2[j]=s1[i];
                rep(k,1,n)
                {
                    s2[k]+=s2[k-1];
                }
                lol.pub({count(s2,s2+n,*min_element(s2,s2+n)),{i+1,j+1}});
            }
        }
        auto x=*max_element(lol.begin(),lol.end());
        cout<<x.fi<<endl;
        cout<<x.se.fi<<" "<<x.se.se<<endl;
    }
    else
        cout<<"0\n1 1\n";
}