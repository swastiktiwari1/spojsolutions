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
int tree[4*100005][26];
int a[100005];
int k;
void build(int node, int start, int en)
{
    if(start==en)
    {
        tree[node][a[start]]=1;
    }
    else
    {
        int mid=(start+en)/2;
        build(node*2,start,mid);
        build(node*2+1,mid+1,en);
        rep(i,0,26)
            tree[node][i]+=tree[2*node][i]+tree[2*node+1][i];
    }
}
void update(int node, int start, int en, int idx,int val)
{
     if (start==en)
     {
         a[idx]=val;
         //cout<<k<<endl;
         a[idx]=(a[idx]);
         rep(i,0,26)
         tree[node][i]=0;
         tree[node][a[idx]]=1;
     }
     else
     {
         int mid=(start+en)/2;
         if(start <= idx && idx <= mid)
         {
             update(node*2,start,mid,idx,val);
         }
         else
         {
             update(node*2+1,mid+1,en,idx,val);
         }
         rep(i,0,26)
            tree[node][i]=tree[2*node][i]+tree[2*node+1][i];

     }

}
int query(int node, int start, int en, int l, int r,int j)
{
    if (r<start || l>en)
    {
        return 0;
    }
    if (l<=start && r>=en)
    {
        return tree[node][j];
    }
    int mid=(start+en)/2;
    int q1=query(node*2,start,mid,l,r,j);
    int q2=query(node*2+1,mid+1,en,l,r,j);
    return q1+q2;
}

int32_t main()
{
    string s;
    cin>>s;
    int n=s.sz;
    rep(i,0,n)
    {
        a[i]=s[i]-'a';
    }
    build(1,0,n-1);
    int q,qt,l,r,idx,su,temp;
    char lol;
    cin>>q;
    while(q--)
    {
        cin>>qt;
        if(qt==2)
        {
            cin>>l>>r;
            su=0;
            rep(i,0,26)
            {
             temp=query(1,0,n-1,l-1,r-1,i);   
             if (temp>0)
             {
                 su+=1;
             }
            }
            cout<<su<<endl;
        }
        else{
            cin>>idx;
            cin>>lol;
            update(1,0,n-1,idx-1,lol-'a');
        }
    }
    
    

}