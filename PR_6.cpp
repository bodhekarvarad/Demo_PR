#include<iostream>
#include<stdlib.h>
using namespace std;
struct symbol
{
	char alpha;
	int value;
};
void display(symbol tab[],int n);
void modify(symbol tab[],int n,char alpha);
void search(symbol tab[],int n,char alpha);
void delete1(symbol tab[], int &n,char alpha);

int main()
{
	symbol *table;
	int n,i;
	char alpha;
	cout<<"How Many Symbol You Have To Enter: ";
	cin>>n;
	table=new symbol[n];
	cout<<"Symbol\tValue\n";
	for(i=0;i<n;i++)
	{
		cin>>table[i].alpha>>table[i].value;
	}
	while(1)
	{
		int choice;
		cout<<endl;
		cout<<"1.Display\t"<<endl;
		cout<<"2.Modify\t"<<endl;
		cout<<"3.Search\t"<<endl;
		cout<<"4.Delete"<<endl;
		cout<<"\nEnter your choice";
		cin>>choice;
		switch(choice)
		{
			case 1:
				display(table,n);
				break;
			case 2:
				modify(table,n,alpha);
				break;
			case 3:
				search(table,n,alpha);
				break;
			case 4:
				delete1(table,n,alpha);
				break;
			default:
				exit(0);
		}
	}
	return 0;
}
void display(symbol tab[],int n)
{
	int i;
	for(i=0;i<n;i++)
	{
		cout<<tab[i].alpha<<"\t"<<tab[i].value<<endl;
	}
}
void modify(symbol tab[],int n,char alpha)
{
	int temp,i;
	cout<<"Enter the symbol to be modified";
	cin>>alpha;
	cout<<"Enter the value after modification";
	cin>>temp;
	for(i=0;i<n;i++)
	{
		if(tab[i].alpha==alpha)
		{
			tab[i].value=temp;
			cout<<endl;
			display(tab,n);
		 }
	}
}
void search(symbol tab[],int n, char alpha)
{
	int i;
	cout<<"Enter the symbol to be Searched";
	cin>>alpha;
	for(i=0;i<n;i++)
	{
		if(tab[i].alpha==alpha)
		{
			cout<<tab[i].alpha<<"\t"<<tab[i].value<<endl;
		}
	}
}
void delete1(symbol tab[], int &n, char alpha)
{
	int i;
	cout<<"Enter the symbol to be Deleted";
	cin>>alpha;
	for(i=0;i<n;i++)
	{
		if(tab[i].alpha==alpha)
		{
			tab[i].alpha=tab[i+1].alpha;
			tab[i].value=tab[i+1].value;
		}
	}
		n=n-1;
		display(tab,n);
}
