#include<bits/stdc++.h> 
using namespace std;
 
#define ll long long int
#define ps push
#define pb push_back
#define INF 10000000
#define MOD 1000000007
#define mp make_pair
#define rep(i,a,b) for (int i = a; i < b; i++)
#define repd(i,a,b) for (int i = a; i >= b; i--)
#define all(v) v.begin(),v.end()
#define pii pair<int,int>
#define F first
#define S second
#define mii map<int,int>
#define vi vector<int>
#define vvi vector<vi>
#define vpii vector<pair<int,int>>
#define itr :: iterator it
#define WL(t) while(t --)
#define gcd(a,b) __gcd((a),(b))
#define lcm(a,b) ((a)*(b))/gcd((a),(b))
#define debug(x) cout << x << endl;
#define debug2(x,y) cout << x << " " << y << endl;
#define debug3(x,y,z) cout << x << " " << y << " " << z << endl;
 
int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};
 
int mn=1e9;
int ans;
 
void solve(){
    int n,t;
    cin>>n>>t;
    
    rep(i,0,n){
        int s,d;
        cin>>s>>d;
        // s+r*d>=t
        int r=(t-s)/d;
        while(r<0 || s+r*d<t ) r++;
        if(mn > s+r*d){
            mn=s+r*d;
            ans=i+1;
        }
    }
    debug(ans);
}
 
signed main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
 
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
                  
    int t=1;
    // cin>>t;
    WL(t){
        solve();
    }    }