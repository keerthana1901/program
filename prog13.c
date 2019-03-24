#include <stdio.h>
int main()
{
	int n,q,p[10],r[10],a[10],i,j,k;
	scanf("%d %d",&n,&q);
	for(i=1;i<=n;i++)
	{
	    scanf("%d",&a[i]);
	}
	for(k=1;k<=q;k++)
	{
	    scanf("%d %d",&p[k],&r[k]);
	}
		for(k=1;k<=q;k++)
	{
	     int x=0;
	    for(i=p[k];i<=r[k];i++)
	    {
	      x=x^a[i];
	      
	    }
	   printf("%d\n",x);
	}

	    return 0;
}
