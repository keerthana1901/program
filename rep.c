#include <stdio.h>

int main(void) {
	int n,a[100],i,j,k=0,count=0,t,c[100];
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		for(j=1;j<n;j++)
		{
			if(a[j-1]>a[j])
			{
				t=a[j-1];
				a[j-1]=a[j];
				a[j]=t;
			}
		}
	}
	t=0;
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++)
		{
			if(a[i]==a[j])
			{
				count++;
				t++;		
			}
		}
		if(count>0)
		{
			c[k]=a[i];
			k++;
		}
		count=0;
	}
	if(t>0)
	{
	for(i=0;i<k;i++)
	{
		for(j=i+1;j<k;j++)
		{
			if(c[j]==c[i])
			{
				count++;
			}
		}
		if(count==0)
		{
		  printf("%d ",c[i]);
		}
		count=0;
	}
	}
	else
	{
		printf("unique");
	}
	return 0;
}
