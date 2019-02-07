

import java.util.*;
import java.lang.*;
import java.io.*;


class holiday
{
	public static void main (String[] args) throws java.lang.Exception
	{
	
		Scanner obj = new Scanner(System.in);
		String s;
		s=obj.next().toLowerCase();
		if(s.equals("sunday") || s.equals("saturday")) 
			System.out.println("yes");
		
		else 
			System.out.println("no");
		
	


	}
}
