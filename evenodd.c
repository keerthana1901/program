/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;


class evenodd
{
	public static void main (String[] args) throws java.lang.Exception
	{
		int n;
     Scanner s=new Scanner(System.in);
     n=s.nextInt();
     int a[]=new int[n];
     for(int i=0;i<n;i++){
         a[i]=s.nextInt();
         
     }
     for(int i=0;i<n;i++){
         if(i%2==0){
             if(a[i]%2!=0){
                 System.out.print(a[i]);
             }
         }
         else if(i % 2 != 0)
         {
             if(a[i]%2==0){
                 System.out.println(a[i]);
             }
         }
     }
	}
}
