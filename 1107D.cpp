#include<bits/stdc++.h>
using namespace std;
long long int n,ps[5205][5205];
int f(long long int x)
{
    long long int i,j;
    for(i=x;i<n+1;i+=x)
    {
        for(j=x;j<n+1;j+=x)
        {
            if (ps[i][j]+ps[i-x][j-x]-ps[i][j-x]-ps[i-x][j]!=x*x)
                if (ps[i][j]+ps[i-x][j-x]-ps[i][j-x]-ps[i-x][j]!=0)
                    return 0;
        }
    }
    return 1;
}
string HexToBin(string hexdec)
{
    long int i = 0;
    string s="";
    while (hexdec[i]) {

        switch (hexdec[i]) {
        case '0':
            s+="0000";
            break;
        case '1':
            s+="0001";
            break;
        case '2':
            s+="0010";
            break;
        case '3':
            s+="0011";
            break;
        case '4':
            s+="0100";
            break;
        case '5':
            s+="0101";
            break;
        case '6':
            s+="0110";
            break;
        case '7':
            s+="0111";
            break;
        case '8':
            s+="1000";
            break;
        case '9':
            s+="1001";
            break;
        case 'A':
        case 'a':
            s+= "1010";
            break;
        case 'B':
        case 'b':
            s+= "1011";
            break;
        case 'C':
        case 'c':
            s+= "1100";
            break;
        case 'D':
        case 'd':
            s+= "1101";
            break;
        case 'E':
        case 'e':
            s+= "1110";
            break;
        case 'F':
        case 'f':
            s+= "1111";
            break;
        default:
            s+="";
        }
        i++;
    }
    return s;
}
int main()
{
    cin>>n;
    string arr[5205];
    long long int i,j,k;
    for(i=0;i<n;i++)
    {
        string s;
        cin>>s;
        arr[i]=HexToBin(s);
    }
    for(i=1;i<n+1;i++)
    {
        for(j=1;j<n+1;j++)
        {
            ps[i][j]=arr[i-1][j-1]-'0'-ps[i-1][j-1]+ps[i-1][j]+ps[i][j-1];
            //cout<<ps[i][j]<<" ";
        }
        //cout<<"\n";
    }
    long long int high=n;
    while(1)
    {
        if (n%high==0)
        {if (f(high)==1)
            break;}
        high-=1;
    }
    cout<<high;
}