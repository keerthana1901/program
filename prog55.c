#include <stdio.h>

int main(void) {
int n1,s;
scanf("%d",&n1);
int a[n1];
for(int i=0;i<n1;i++)
{
scanf("%d ",&a[i]);
}
s=a[0];
for(int i=1;i<n1;i++)
{
s=s^a[i];
}
printf("%d",s);

	return 0;
}
