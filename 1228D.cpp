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
int ran[100005];
int dsu[100005];
int fin(int x)
{
    while(dsu[x]!=x)
    {
        dsu[x]=dsu[dsu[x]];
        x=dsu[x];
    }
    return x;
}
void uni(int a,int b)
{
    int fa=fin(a);
    int fb=fin(b);
    if (ran[fa]>ran[fb])
    {
        dsu[fb]=fa;
    }
    else if (ran[fb]>ran[fa])
    {
        dsu[fa]=fb;
    }
    else
    {
        ran[fa]+=1;
        dsu[fb]=fa;
    }
}
 
int32_t main()
{
    fastIO
   int n,m,a,b;
   cin>>n>>m;
   vector <int> adj[100005];
   int ans[100005];
   clr(ans,0);
   int cc=0;
    clr(ran,0);
   rep(i,0,m)
   {
       cin>>a>>b;
       adj[a-1].pub(b-1);
       adj[b-1].pub(a-1);
   }
   rep(i,0,n)
   {
       dsu[i]=i;
   }
 
   int flag=0;
   rep(i,0,n)
   {
       if (fin(i)==i)
       {
           cc+=1;
           
           int j=0;
           set <int> s;
           rr(adj[i])
            s.insert(val);
          
            rep(j,0,n)
            {
                if(s.find(j)==s.end() && i!=j)
                {
                   // cout<<"uni"<<i<<" "<<j<<endl;
                    uni(i,j);
                }
            }
               
          
       }
       rr(adj[i])
       {
           if (fin(i)==fin(val))
           {
           //    cout<<i<<" "<<val<<endl;
               flag=1;
               cout<<"-1";
               exit(0);
           }
       }
 
   }
   int k=1;
   map <int,int> mm;
   set <int> ss;
   map<int,int> m2;
   rep(i,0,n)
   {
       if (mm[fin(i)]==0)
       {
           mm[fin(i)]=k;
           k+=1;
       }
       ans[i]=mm[fin(i)];
       ss.insert(ans[i]);
   }
   int su=0;
   
   
   rep(i,0,n)
       {
           if (m2[ans[i]]==0)
           {
               m2[ans[i]]=adj[i].size();
           }
           else if(m2[ans[i]]!=adj[i].size())
           {
               //cout<<i<<" "<<adj[i].sz<<mm[]
               flag=1;
           }
       }
   if (ss.size()==3 && flag==0)
   {
       
   
    print1d(ans,n)
       
   }
    else
        cout<<"-1"<<endl;
 
 
}