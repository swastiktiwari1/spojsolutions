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
stack<char> s;
main()
{
    int n;
    cin >> n;
    string sp;
    cin >> sp;
    bool ck = 0, ck1 = 0;
    int cnt = 0;
    for (int i = 0; i < sp.size(); i++)
    {
        if (sp[i] == '(')
            s.push(sp[i]);
        else
        {
            if (!s.empty())
                s.pop();
            else
            {
                if (!ck)
                {
                    ck = 1;
                }
                else
                {
                    ck1 = 1;
                    break;
                }
            }
        }
    }
    if (ck1)
        puts("NO");
    else
    {
        if (!ck)
        {
            if (s.empty())
                puts("YES");
            else
                puts("NO");
        }
        else
        {
            if (!s.empty())
            {
                s.pop();
                if (s.empty())
                    puts("YES");
                else
                    puts("NO");
            }
            else
                puts("NO");
        }
    }
}