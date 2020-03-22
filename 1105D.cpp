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
 int visited[1005][1005];
  char arr[1005][1005];
  queue < pair<int,int> > qs[11];
   queue < pair<int,int> > nqs[11];
int32_t main()
{
    
   int n,m,p,s[11];
   cin>>n>>m>>p;
   rep(i,0,p)
   cin>>s[i];

  rep(i,0,n)
   cin>>arr[i];


   int lq[11];
   clr(lq,0);

   clr(visited,0);
   rep(i,0,n)
   {
       rep(j,0,m)
       {
           if (arr[i][j]!='.' && arr[i][j]!='#')
           {
               qs[(arr[i][j])-('1')].push({i,j});
                lq[(arr[i][j])-('1')]+=1;

           }
       }
   }
//   rep(i,0,p)
//   {cout<<qs[i].front().fi<<" ";}
   int x,y;
   int zc=0;
   do
   {
       zc=0;
     //  cout<<"shuru";
       rep(i,0,p)
       {
           rep(k,0,s[i])
           {
               while(!qs[i].empty())
               {
                pair<int,int> p1=qs[i].front();
                x= p1.fi;
                y= p1.se;
                
                qs[i].pop();
                visited[x][y]=1;
                if (x-1>=0 && arr[x-1][y]=='.' && visited[x-1][y]==0)
                    {
                    //    cout<<"idhar";
                        visited[x-1][y]=i;
                    nqs[i].push(mkp((x-1),y));
                    arr[x-1][y]=char((i+1)+'0');
               //     cout<<x-1<<" "<<y<<endl;

                    }
                if (x+1<n && arr[x+1][y]=='.' && visited[x+1][y]==0)
                    {
                        visited[x+1][y]=1;
                  //      cout<<x+1<<" "<<y<<endl;
                    nqs[i].push(mkp((x+1),y));
                    arr[x+1][y]=char((i+1)+'0');

                    }
                if (y-1>=0 && arr[x][y-1]=='.' && visited[x][y-1]==0)
                    {
                        visited[x][y-1]=1;
                   //     cout<<x<<" "<<y-1<<endl;
                    nqs[i].push(mkp(x,(y-1)));
                    arr[x][y-1]=char((i+1)+'0');

                    }
                if (y+1<m && arr[x][y+1]=='.' && visited[x][y+1]==0)
                    {
                    //    cout<<x<<" "<<y+1<<endl;
                        visited[x][y+1]=1;
                    nqs[i].push(mkp(x,(y+1)));
                    arr[x][y+1]=char((i+1)+'0');
                 //   cout<<char((i+1)+'0')<<endl;

                    }


               }
               lq[i]=0;
             while(!nqs[i].empty())
                    {
                        pair<int,int> p1=nqs[i].front();
                         x= p1.fi;
                        y= p1.se;
                     //   cout<<x<<" "<<y<<endl;
                       qs[i].push({x,y});
                    nqs[i].pop();
                    lq[i]+=1;}
                if(lq[i]==0)break;
           }
       }
       rep(i,0,p)
       {
           if (lq[i]==0)
           zc+=1;
       }
   }
   while(zc!=p);
   int counts[11];
   clr(counts,0);
 //  print2d(visited,n,m)
   rep(i,0,n)
   {
       rep(j,0,m)
       {
          // cout<<visited[i][j]<<" ";
           if(arr[i][j]!='#' && arr[i][j]!='.')
           counts[arr[i][j]-'1']+=1;
       }
     // cout<<endl;
   }
  // print2d(visited,n,m)
   print1d(counts,p);



}