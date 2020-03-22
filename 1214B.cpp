 
    #include<bits/stdc++.h>
    using namespace std;
    int main(){
    	int b,g,n,a,c,d,e,f;
    	cin>>b>>g>>n;
    	a=max(b,g);
    	c=min(b,g);
    	if(n>=a){
    		d=n-a;
    		e=c-d+1;
    		cout<<e;
    	}
    	else if(n<a&&n>=c){
    		cout<<c+1;
    	}
    	else{
    		cout<<n+1;
    	}
    }