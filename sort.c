#include<stdio.h>
int main(void)
{
    int a[15],n,i,j;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }

 for(i=0;i<n-1;i++)
 {
     int z;
 
  for(j=i+1;j<n;j++)
 { 
     if(a[i]>a[j])
     {
     z=a[i];
     a[i]=a[j];
     a[j]=z;
 }
 }
 }
 for(i=0;i<n;i++)
 {
     printf(" %d",a[i]);
 }
 return 0;
}
