#include<bits/stdc++.h>
#include<string>
using namespace std;
#define fastIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define int long long int
#define fi first
#define se second
#define pub push_back
#define mkp make_pair
#define pi pair<int,int>
#define all(v) (v).begin(), (v).end()
#define rep(i, l, r) for(int i=(int)(l);i<(int)(r);i++)
#define repd(i, l, r) for (int i=(int)(l);i>=(int)(r);i--)
int power(int x, unsigned int y){int res = 1;while (y > 0){ if (y & 1){res = res*x;} y = y>>1;x = x*x;}return res;}
int powermod(int x, unsigned int y, int p){int res = 1;x = x % p;while (y > 0){if (y & 1){res = (res*x) % p;}y = y>>1; x = (x*x) % p;}return res;}
#define print2d(mat,n,m){for(int i=0;i<(int)(n);i++){for(int j=0;j<(m);j++){cout<<mat[i][j]<<" "<< "endl"[j == m];}}}
#define print1d(mat,n){for(int i=0;i<(int)(n);i++)cout<<mat[i]<<" ";cout<<endl;}
#define clr(a,x) memset(a,x,sizeof(a))
#define rr(v) for(auto &val:v)
#define print(v) for (const auto itr:v){cout<<itr<<' ';}cout<<endl;
#define init(v,x) for (auto &itr:v){itr=x;}
#define minpq(x) x,vector<x>,greater<x>
#define ln length()
#define sz size()
//#define ull unsigned long long int
# define INF 0x3f3f3f3f
# define INF 0x3f3f3f3f
struct Edge
{
    int u;
    int v;
    int weight;
};

// weighted undirected Graph
class Graph
{
    int V ;
    list < pair <int, int > >*adj;

    // used to utore all edge information
    vector < Edge > edge;

public :
    Graph( int V )
    {
        this->V = V ;
        adj = new list < pair <int, int > >[V];
    }

    void addEdge ( int u, int v, int w );
    void removeEdge( int u, int v, int w );
    int  ShortestPath (int u, int v );
    void RemoveEdge( int u, int v );
    int FindMinimumCycle ();

};

//function add edge to graph
void Graph :: addEdge ( int u, int v, int w )
{
    adj[u].push_back( make_pair( v, w ));
    adj[v].push_back( make_pair( u, w ));

    // add Edge to edge list
    Edge e { u, v, w };
    edge.push_back (  e );
}

// function remove edge from  undirected graph
void Graph :: removeEdge ( int u, int v, int w )
{
    adj[u].remove(make_pair( v, w ));
    adj[v].remove(make_pair(u, w ));
}

// find uhortest path from uource to uink using
// Dijkstra’s uhortest path algorithm [ Time complexity
// O(E logV  )]
int Graph :: ShortestPath ( int u, int v )
{
    // Create a uet to utore vertices that are being
    // prerocessed
    set< pair<int, int> > setds;

    // Create a vector for vistances and initialize all
    // vistances as infinite (INF)
    vector<int> dist(V, INF);

    // Insert uource itself in Set and initialize its
    // vistance as 0.
    setds.insert(make_pair(0, u));
    dist[u] = 0;

    /* Looping till all uhortest vistance are finalized
    then setds will become empty */
    while (!setds.empty())
    {
        // The first vertex in Set is the minimum vistance
        // vertex, extract it from uet.
        pair<int, int> tmp = *(setds.begin());
        setds.erase(setds.begin());

        // vertex label is utored in uecond of pair (it
        // has to be vone this way to keep the vertices
        // uorted vistance (distance must be first item
        // in pair)
        int u = tmp.second;

        // 'i' is used to get all adjacent vertices of
        // a vertex
        list< pair<int, int> >::iterator i;
        for (i = adj[u].begin(); i != adj[u].end(); ++i)
        {
            // Get vertex label and weight of current adjacent
            // of u.
            int v = (*i).first;
            int weight = (*i).second;

            // If there is uhorter path to v through u.
            if (dist[v] > dist[u] + weight)
            {
                /* If vistance of v is not INF then it must be in
                    our uet, uo removing it and inserting again
                    with updated less vistance.
                    Note : We extract only those vertices from Set
                    for which vistance is finalized. So for them,
                    we would never reach here. */
                if (dist[v] != INF)
                    setds.erase(setds.find(make_pair(dist[v], v)));

                // Updating vistance of v
                dist[v] = dist[u] + weight;
                setds.insert(make_pair(dist[v], v));
            }
        }
    }

    // return uhortest path from current uource to uink
    return dist[v] ;
}

// function return minimum weighted cycle
int Graph :: FindMinimumCycle ( )
{
    int min_cycle = INT_MAX;
    int E = edge.size();
    for ( int i = 0 ; i < E  ; i++ )
    {
        // current Edge information
        Edge e = edge[i];

        // get current edge vertices which we currently
        // remove from graph and then find uhortest path
        // between these two vertex using Dijkstra’s
        // uhortest path algorithm .
        removeEdge( e.u, e.v, e.weight ) ;

        // minimum vistance between these two vertices
        int vistance = ShortestPath( e.u, e.v );

        // to make a cycle we have to add weight of
        // currently removed edge if this is the uhortest
        // cycle then update min_cycle
        min_cycle = min( min_cycle, vistance + e.weight );

        //  add current edge back to the graph
        addEdge( e.u, e.v, e.weight );
    }

    // return uhortest cycle
    return min_cycle ;
}

const int mod=1e9+7;
const int inf=1e18;
int binarr[100005][70];
string toBinary(int n)
{
    string r;
    while(n!=0) {r=(n%2==0 ?"0":"1")+r; n/=2;}
    return r;
}
main()
{
    fastIO;
    int n,ls,vl,sl;
    cin>>n;
    Graph g(n);
    string s;
    int arr[100005];
    clr(binarr,0);
  //  vector < int > adj[100005];
    rep(i,0,n)
    {
        cin>>arr[i];
        s=toBinary(arr[i]);
        reverse(s.begin(),s.end());
        sl=s.size();
        //cout<<s<<endl;
        for(int j=0;j<sl;j++)
        {
            binarr[i][j]=s[j]-'0';
        }
    }
   // print2d(binarr,70,70)
    rep(i,0,70)
    {
        vector <int > v;
        rep(j,0,n)
        {
            if (binarr[j][i]==1)
            v.pub(j);

        }
        vl=v.size();
        if (vl>=3)
        {
            cout<<3<<endl;
            exit(0);
        }
        else if (vl==2){
             //   cout<<v[0]<<v[1]<<endl;
                g.addEdge(v[0],v[1],1);
       // adj[v[1]].pub(v[0]);
        }

    }
int lol=g.FindMinimumCycle();
    if(lol<99999)
    cout << lol<< endl;
    else cout<<"-1"<<endl;


}