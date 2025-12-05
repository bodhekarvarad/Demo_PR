#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	char str[20],op[10],chr[10],num[10];
	int j,i=0,k=0,m=0,l;

	cout<<"Enter the equation:";
	cin>>str;
	l=strlen(str);
	for(j=0;j<l;j++)
	{
	    if((str[j]>='a' && str[j]<='z') || (str[j]>='A' && str[j]<='Z'))
		{
			chr[i]=str[j];
			i++;
		}

	       else if(str[j]>='0' && str[j]<='9')
		 {
			num[m]=str[j];
			m++;
		}
else
		{

			op[k]=str[j];
			k++;
		}

	}
	cout<<"\nOPERATOR:{";
	for(j=0;j<k;j++)
	{
		cout<<op[j];
		if(j<k-1) cout<<",";
	}
	cout<<"}\nCHARACTER:{";
	for(j=0;j<i;j++)
	{
		cout<<chr[j];
		if(j<i-1) cout<<",";
	}
	cout<<"}\n Number:{";
	for(j=0;j<m;j++)
	{
		cout<<num[j];
		if(j<m-1) cout<<",";
	}

	cout<<"}\n";
	return 0;
}

