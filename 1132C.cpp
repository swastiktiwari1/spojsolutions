#include<bits/stdc++.h>
using namespace std;
struct ssee
{
    long long int si;
    long long int ei;
};
struct ssee foi(long long int as1,long long int ae,long long int bs,long long int be)
   { struct ssee llll;
   long long int os,oe;
   llll.si=0;
   llll.ei=0;
       if ( bs>ae or as1>be )
        return (llll);
    else
       { os=max(as1,bs);
        oe=min(ae,be);
        llll.si=os;
        llll.ei=oe;
        return (llll);}}

main()
{
    long long int n,q,arr[5005],i,tc1,mi,j,oc[5005],tc[5005],a,b,kitnehe=0;
    long long int queries[10005][2];
    cin>>n>>q;
    struct ssee k;
    memset(oc,0,sizeof(oc));
    memset(tc,0,sizeof(tc));
    memset(arr,0,sizeof(arr));
    for(i=0;i<q;i++)
    {
        cin>>a>>b;
        queries[i][0]=(a);
        queries[i][1]=(b);
         //cout<<queries[i][1];
        arr[a]+=1;
        arr[b+1]-=1;

    }
    for(i=1;i<n+1;i++)
    {
        arr[i]+=arr[i-1];
      //  cout<<arr[i]<<" ";
    }
    for(i=1;i<n+1;i++)
    {
    oc[i]=oc[i-1];
    tc[i]=tc[i-1];
    if (arr[i]==1)
        {oc[i]+=1;
        tc[i]+=1;}
    else if (arr[i]==2)
        tc[i]+=1;
    if (arr[i]>0)
        kitnehe+=1;
      //  cout<<tc[i]<<" ";
    }
    mi=n;

    for(i=0;i<q-1;i++)
    {
        for(j=i+1;j<q;j++)
        {
            //cout<<queries[i][1];
            tc1=oc[queries[i][1]]-oc[queries[i][0]-1];

        tc1+=oc[queries[j][1]]-oc[queries[j][0]-1];

        k=foi(queries[i][0],queries[i][1],queries[j][0],queries[j][1]);
        if (k.ei!=0 && k.si!=0)
          { tc1-=oc[k.ei]-oc[k.si-1];
           tc1+=tc[k.ei]-tc[k.si-1];}


        //cout<<tc1<<"\n";
        mi=min(mi,tc1);
        //cout<<mi<<" ";
        }
    }
    cout<<kitnehe-mi;

}