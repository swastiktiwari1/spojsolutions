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
int dsu[1000];
int ran[1000];
int fin(int x)
{
    while(x!=dsu[x])
    {
        dsu[x]=dsu[dsu[x]];
        x=dsu[x];
    }
    return x;
}
void unio(int x, int y)
{
    int fx=fin(x);
    int fy=fin(y);
    if(ran[fx]>ran[fy])
    dsu[fy]=fx;
    elif(ran[fy]>ran[fx])
    dsu[fx]=fy;
    else
    {
        dsu[fx]=fy;
        ran[fy]+=1;
    }
}
int32_t main()
{
    fastIO
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
    #endif
    clr(dsu,0);
    clr(ran,0);
    rep(i,0,26)
    dsu[i]=i;
    string s;
    int n;
    cin>>n;
    set <int> lol;
    rep(i,0,n)
    {
        cin>>s;
        lol.insert(s[0]-'a');
        rep(j,1,s.sz)
        {
            unio(s[j-1]-'a',s[j]-'a');
            lol.insert(s[j]-'a');
        }
    }
    set < int > haha;
    rr(lol)
    {
        haha.insert(fin(val));
    }
    // print(haha)
    cout<<haha.sz<<endl;
    return 0;
}