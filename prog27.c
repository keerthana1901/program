#include<stdio.h>
int main()
{
char a1[5000],b1[5000];
int i,j,c=0;
scanf("%s %s",a1,b1);
for(i=0,j=0;a1[i]!='\0',b1[j]!='\0';i++,j++)
{
if(a1[i]!=b1[j])
{
c++;
}
}
printf("%d",c);
return 0;
}
