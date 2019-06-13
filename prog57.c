#include <stdio.h>

int numericals(char s)
{
switch(s)

{
case 'V':
return 5;
case 'X':
return 10;
case 'I':
return 1;
}
}
int main(void) {
// your code goes here
char s[10];
int num=0,i,len;
scanf("%s",s);
for(len=0;s[len];len++);
if(len==2)
{
if(numericals(s[0])>=numericals(s[1]))
{
num=num+(numericals(s[0])+numericals(s[1]));
}
else
{

num=num+(numericals(s[1])-numericals(s[0]));
}
}
else
{

for(i=len-1;i>1;i--)
{
if(numericals(s[i-1])>=numericals(s[i]))
{
num=num+(numericals(s[i-1])+numericals(s[i]));
}
else 
{

num=num+(numericals(s[i])-numericals(s[i-1]));
}
}

num=num+numericals(s[0]);
}
printf("%d",num);
return 0;
}
