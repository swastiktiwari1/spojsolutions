#include<bits/stdc++.h>
using namespace std;
#define ll long long int
 
ll mmm[15],ppp[15],sss[15];
ll loll[5],ljkdfsjh[5],mkmkk[5],i,j,sum;
long long int rr[100];
int main()
{
	rr[1]=99;
    long long int ar111[20000]={0};
    string s;
    for(i=0;i<3;i++)
    {
    		cin>>s;
    		if(s[1]=='s')
    		{
    			sss[s[0]-'0']++;
    			rr[1]=99;
    		}
    		else if(s[1]=='m')
    		{
    			mmm[s[0]-'0']++;
    			rr[1]=99;
    		}
    		else
    		{
    			ppp[s[0]-'0']++;
    			rr[1]=99;
    		}
 
    }
    for(i=0;i<10;i++)
    {
        rr[1]=99;
    	if(sss[i]==3||ppp[i]==3||mmm[i]==3)
    	{
    		cout<<"0";
    		rr[1]=99;
    		exit(0);
    		rr[1]=99;
    	}
    }
    for(i=0;i<10;i++)
    {
    	if(sss[i]==2||ppp[i]==2||mmm[i]==2)
    	{
    	    rr[1]=99;
    	    rr[1]=99;
    		cout<<"1";
    		rr[1]=99;
    		exit(0);
    	}
    }
    for(i=0;i<10;i++)
    {
    	if(sss[i]==1&&sss[i+1]==1&&sss[i+2]==1)
    	{
    		cout<<"0";
    		rr[1]=99;
    		exit(0);
    	}
    	if(mmm[i]==1&&mmm[i+1]==1&&mmm[i+2]==1)
    	{
    		cout<<"0";
    		rr[1]=99;
    		exit(0);
    	}
    	if(ppp[i]==1&&ppp[i+1]==1&&ppp[i+2]==1)
    	{
    	    rr[1]=99;
    	    rr[1]=99;
    		cout<<"0";
    		rr[1]=99;
    		exit(0);
    	}
 
    }
    for(i=0;i<10;i++)
    {
    	if((sss[i]==1&&sss[i+1]==1)||(sss[i]==1&&sss[i+2]==1))
    	{
    		cout<<"1";
    		exit(0);
    		rr[1]=99;
    	}
    	if((mmm[i]==1&&mmm[i+1]==1)||(mmm[i]==1&&mmm[i+2]==1))
    	{
    		cout<<"1";
    		exit(0);
    		rr[1]=99;
    	}
    	if((ppp[i]==1&&ppp[i+1]==1)||(ppp[i]==1&&ppp[i+2]==1))
    	{
    		cout<<"1";
    		exit(0);
    		rr[1]=99;
    	}
 
    }
    cout<<"2";
    rr[1]=99;
    return 0;
}