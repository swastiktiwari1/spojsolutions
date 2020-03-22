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
vector < pair <int,int> > xaxis[1000006];
int32_t main()
{
   int x1,x2,y1,y2;
   cin>>x1>>y1>>x2>>y2;
   int ma=max(y1,y2);
   int mi=min(y1,y1);
   rep(i,min(x1,x2),max(x1,x2))
   {
       xaxis[i].pub({mi,ma});
   }
   cin>>x1>>y1>>x2>>y2;
   ma=max(y1,y2);
   mi=min(y1,y1);
   rep(i,min(x1,x2),max(x1,x2))
   {
        rep(j,0,xaxis[i].sz)
        {
            if(mi<= xaxis[i][j].fi && ma<=xaxis[i][j].fi)
            {
                int xx=0;
            }
            elif(mi>= xaxis[i][j].se && ma>=xaxis[i][j].se)
            {
                int xx=0;
            }
            elif (mi<=xaxis[i][j].fi && ma<xaxis[i][j].se)
                xaxis[i][j].fi=ma;
            elif (mi>=xaxis[i][j].fi && ma<=xaxis[i][j].se)
            {
                xaxis[i].pub({ma,xaxis[i][j].se});
                xaxis[i][j]={xaxis[i][j].fi,mi};
            }
            elif ((mi>=xaxis[i][j].fi && mi<=xaxis[i][j].se) && ma>=xaxis[i][j].se)
                xaxis[i][j].se=mi;
            elif (mi<=xaxis[i][j].fi && ma>=xaxis[i][j].se)
                xaxis[i][j]={0,0};
        }
   }
   cin>>x1>>y1>>x2>>y2;
   ma=max(y1,y2);
   mi=min(y1,y1);
   rep(i,min(x1,x2),max(x1,x2))
   {
        rep(j,0,xaxis[i].sz)
        {
            if(mi<= xaxis[i][j].fi && ma<=xaxis[i][j].fi)
            {
                int xx=0;
            }
            elif(mi>= xaxis[i][j].se && ma>=xaxis[i][j].se)
            {
                int xx=0;
            }
            elif (mi<=xaxis[i][j].fi && ma>=xaxis[i][j].se)
                xaxis[i][j]={0,0};
            elif (mi<=xaxis[i][j].fi && ma<xaxis[i][j].se)
                xaxis[i][j].fi=ma;
            elif (mi>=xaxis[i][j].fi && ma<=xaxis[i][j].se)
            {
                xaxis[i].pub({ma,xaxis[i][j].se});
                xaxis[i][j]={xaxis[i][j].fi,mi};
            }
            elif ((mi>=xaxis[i][j].fi && mi<=xaxis[i][j].se) && ma>=xaxis[i][j].se)
                xaxis[i][j].se=mi;
            
        }
   }
   int flag=0;
   rep(i,0,1000005)
   {
       if (xaxis[i].sz!=0)
       {
           rr(xaxis[i])
           {
               if (val.se>val.fi)
               {
                 //  cout<<i<<" "<<val.fi<<" "<<val.se<<endl;
                flag=1;
               }
           }
       }
   }
   if(flag==1)
    cout<<"YES";
   else
    cout<<"NO";


}