include <stdio.h>

int main(void) {
int a[200],i,j,n;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(a[i]==a[j])
            {
                printf("%d",a[i]);
                goto jump;
            }
        }
    }
    jump:
	return 0;
}