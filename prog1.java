/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int m=sc.nextInt();
		int l=0,p=0;
		int a[][]=new int[n][m];
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				a[i][j]=sc.nextInt();
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(a[i][j]==0)
				{
					for(l=0,p=0;l<m&&p<n;l++,p++)
					{
						a[i][l]='*';
						a[p][j]='*';
					l++;
					}
				
				}
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(a[i][j]=='*')
				{
					a[i][j]=0;
				}
				System.out.print(a[i][j]+" ");
			}
			System.out.println();
		}
		sc.close();
	
	}
}
