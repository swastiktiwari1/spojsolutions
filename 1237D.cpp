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
int tree[2000006];
int tree1[2000006];
int a[500005];
int ans[500005];
pair<int,int>  a1[500005] ;
void build(int node,int start,int end)
{
    if(start == end)
        tree[node] = a[start];
    else
    {
        int mid = (start + end) / 2;
        build(2*node, start, mid);
        build(2*node+1, mid+1, end);
        tree[node] = min(tree[2*node+1],tree[2*node]);
    }
}
void update(int node,int start,int end,int idx,int val)
{
    if(start == end)
    {
        a[idx]= val;
        tree[node]= val;
    }
    else
    {
        int mid = (start+end)/2;
        if(idx >= start && idx <= mid)
            update(2*node, start, mid, idx, val);
        else
            update(2*node+1, mid+1, end, idx, val);
         tree[node] = min(tree[2*node],tree[2*node+1]);
    }
}
int query(int node, int start, int end, int l, int r)
{
    if(l > end || start > r)
        return 99999999999999999;
    if(l <= start && r >= end)
        return tree[node];
    int p1,p2;
    int mid = (start+end)/2;
    p1 = query(2*node, start, mid, l, r);
    p2 = query(2*node+1, mid+1, end, l, r);
    return min(p1,p2);
}
void build1(int node,int start,int end)
{
    if(start == end)
        tree1[node] = a[start];
    else
    {
        int mid = (start + end) / 2;
        build1(2*node, start, mid);
        build1(2*node+1, mid+1, end);
        tree1[node] = max(tree1[2*node+1],tree1[2*node]);
    }
}
void update1(int node,int start,int end,int idx,int val)
{
    if(start == end)
    {
        a[idx]= val;
        tree1[node]= val;
    }
    else
    {
        int mid = (start+end)/2;
        if(idx >= start && idx <= mid)
            update1(2*node, start, mid, idx, val);
        else
            update1(2*node+1, mid+1, end, idx, val);
         tree1[node] = max(tree1[2*node],tree1[2*node+1]);
    }
}
int query1(int node, int start, int end, int l, int r)
{
    if(l > end || start > r)
        return -99999999999999999;
    if(l <= start && r >= end)
        return tree1[node];
    int p1,p2;
    int mid = (start+end)/2;
    p1 = query1(2*node, start, mid, l, r);
    p2 = query1(2*node+1, mid+1, end, l, r);
    return max(p1,p2);
}
int32_t main()
{
   // fastIO
    int n,mina,maxa,high,low,mid,q,mii,mai;
   // cin>>n;
    scanf("%lld",&n);
    rep(i,0,n)
    {
      //  cin>>a[i];
        scanf("%lld",&a[i]);
        a[n+i]=a[i];
        a[n+n+i]=a[i];
    }
    clr(tree,0);
    clr(tree1,0);
    clr(ans,0);
    maxa=*max_element(a,a+n);
    mina=*min_element(a,a+n);
    if(maxa<=2*mina)
    {
        rep(i,0,n)
        {
            printf("-1 ");
        }
        printf("\n");
    }
    else
    {
        rep(i,0,n)
        {
            a1[i]={a[i],i};
        }
        sort(a1,a1+n);
      //  reverse(a1.begin(),a1.end());
        build(1,0,3*n-1);
        build1(1,0,3*n-1);
    //    print1d(tree,20);
    //    print1d(tree1,20);
        repd(i,n-1,0)
        {
            int jv=a1[i].fi;
            int ji=a1[i].se;
            high=n+1;
            low=1;
            while(low<=high)
            {
                mid=(high+low)/2;
 
                q=query(1,0,3*n-1,ji+1,ji+mid);
             //   cout<<mid<<" "<<q<<endl;
             //   cout<<q<<endl;
                if(q*2>=jv)
                {
                    low=mid+1;
                }
                else
                {
                    high=mid-1;
                }
 
            }
            mii=low;
          //  cout<<mii<<endl;
            high=n+1;
            low=1;
            while(low<=high)
            {
                mid=(high+low)/2;
                q=query1(1,0,3*n-1,ji+1,ji+mid);
              //  cout<<q<<endl;
                if(q>jv)
                {
                    high=mid-1;
                }
                else
                {
                    low=mid+1;
                }
            }
            mai=low;
     //       cout<<jv<<" "<<mii<<" "<<mai<<endl;
            if(mii<mai)
            {
                ans[ji]=mii;
                ans[n+ji]=mii;
                ans[n+n+ji]=mii;
            }
            else
            {
                ans[ji]=ans[ji+mai]+mai;
                ans[n+ji]=ans[ji+mai]+mai;
                ans[n+n+ji]=ans[ji+mai]+mai;
            }
        }
        rep(i,0,n)
        {
            printf("%lld ",ans[i]);
        }
   //     print1d(ans,n);
    }
}