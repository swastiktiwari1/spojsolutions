#include<bits/stdc++.h>
using namespace std;
vector<long long int> adj[300005];
long long int n,a[300005],par[300005],i,j,used[300005],k,visited[300005];
void dfs(long long int s)
{
    long long int uuu=1,llll=0;
    visited[s]=1;
    for(auto& itr : adj[s])
    {
        if((visited[itr])!=1)
        {
           // cout<<s<<" "<<itr<<"\n";
            dfs(itr);
            if(a[s]==1)
            {
                if(used[s]==0)
                used[s]=max(uuu,used[itr]);
                else if (used[s]!=0)
                {
                    llll=min(used[s],used[itr]);
                    used[s]=max(uuu,llll);

                }
            }
            else
            {
                 used[s]+=(max(uuu,used[itr]));
            }

        }
    }
}
int main()
{
    cin>>n;
    for (i=0;i<n;i++)
    {
        cin>>a[i];
        visited[i]=0;
    }
    for(i=0;i<n-1;i++)
    {
        cin>>par[i];
    }
    for(i=0;i<n-1;i++)
    {
        adj[par[i]-1].push_back(i+1);
    }

    memset(used,0,sizeof(used));
    //memset(visited,0,sizeof(visited));
    dfs(0);
    k=0;
    for(i=0;i<n;i++)
    {

        if (adj[i].size()==0)
        k+=1;
    }
    //cout<<"\n";

    cout<<k-used[0]+1;
    return 0;
}