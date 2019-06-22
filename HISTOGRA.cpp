#include <bits/stdc++.h>
using namespace std;

int main() 
{
    long long int arr[100005];
	while(1)
	{
	    long long int n,i;
	    cin>>n;
	    if (n==0)
	    break;
	    stack<long long int>s;
	    long long int max_a=0;
	    long long int tp;
	    long long int awt;
	    for(i=0;i<n;i++)
	    {
	        cin>>arr[i];
	    }
	    i=0;
	    while(i<n)
	    {
	        if (s.empty()||arr[s.top()]<=arr[i])
	        s.push(i++);
	        else
	        {
	            tp=s.top();
	            s.pop();
	            if(s.empty())
	            awt=arr[tp]*i;
	            else
	            awt=arr[tp]*(i-s.top()-1);
	            if(max_a<awt)
	            max_a=awt;
	            
	        }
	    }
	    while(s.empty()==false)
	    {
	        tp=s.top();
	        s.pop();
	        if(s.empty())
	            awt=arr[tp]*i;
	            else
	            awt=arr[tp]*(i-s.top()-1);
	            if(max_a<awt)
	            max_a=awt;
	        
	    }
	    cout<<max_a<<"\n";
	    
	    
	}
}
