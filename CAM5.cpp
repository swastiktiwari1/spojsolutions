#include<bits/stdc++.h>
using namespace std; 
long long int cc;

class Graph 
{ 
    long long int V;    
    list<long long int> *adj; 

    void DFSUtil(long long int v, bool visited[]); 
public: 
    Graph(long long int V);  
    void addEdge(long long int v, long long int w); 
    void connectedComponents(); 
}; 
  
void Graph::connectedComponents() 
{ 
  
    bool *visited = new bool[V]; 
    for(long long int v = 0; v < V; v++) 
        visited[v] = false; 
  
    for (long long int v=0; v<V; v++) 
    { 
        if (visited[v] == false) 
        { 
            
            DFSUtil(v, visited); 
            cc+=1;
 
        } 
    } 
} 
  
void Graph::DFSUtil(long long int v, bool visited[]) 
{ 
    visited[v] = true; 

    list<long long int>::iterator i; 
    for(i = adj[v].begin(); i != adj[v].end(); ++i) 
        if(!visited[*i]) 
            DFSUtil(*i, visited); 
} 
  
Graph::Graph(long long int V) 
{ 
    this->V = V; 
    adj = new list<long long int>[V]; 
} 
  
// method to add an undirected edge 
void Graph::addEdge(long long int v, long long int w) 
{ 
    adj[v].push_back(w); 
    adj[w].push_back(v); 
} 
  
// Drive program to test above 
main() 
{ 
    long long int t,n,m,a,b,i;
    cin>>t;
    while(t--)
    {
        cin>>n;
        cin>>m;
        Graph g(n);
        cc=0;
        for(i=0;i<m;i++)
        {
            cin>>a;
            cin>>b;
            g.addEdge(a,b);
        }
        g.connectedComponents();
        cout<<cc<<"\n";
        
        
    }
    
} 
