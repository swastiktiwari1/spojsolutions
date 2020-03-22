#include <bits/stdc++.h>
using namespace std;
vector <long long int> k;
long long int n,m,i,j,d,e,f,lk,i1;
long long int visited [500005]={0};
vector <long long int> adj[500005];
void dfs(long long int s)
{
    k.push_back(s);
    visited[s]=1;
    for(auto itr = adj[s].begin();itr!=adj[s].end();itr++)
    {
        if(visited[*itr]==0)
            dfs(*itr);
    }
    
}
int main() {
	
	cin>>n;
	cin>>m;
	
	for(i=0;i<m;i++)
	{
	    f=-1;
	    cin>>d;
	    for(j=0;j<d;j++)
	    {
	       cin>>e;
	       if (f!=-1)
	       {
	           adj[e-1].push_back(f-1);
	           adj[f-1].push_back(e-1);
	       }
	       f=e;
	    }
	}
	
	long long int kitne[n+1]={0};
	for(i=0;i<n;i++)
	{
	    if (visited[i]==0)
	    {
	        lk=k.size();
	        for(j=0;j<lk;j++)
	        {
	            kitne[k[j]]=lk;
	        }
	        k.clear();
	        dfs(i);
	    }
	}
	lk=k.size();
	for(j=0;j<lk;j++)
    {
        kitne[k[j]]=lk;
    }
	for(i=0;i<n;i++)
	{
	    cout<<kitne[i]<<" ";
	}
}