#include<iostream>
using namespace std;
int main()
{
	char str[20];
	char stack[20];
	int top=0;
	cout<<"Given grammer is:\ns->aABe\nA->Abc/b\nB->d"<<endl;
	cout<<"Enter String"<<endl;
	cin>>str;
	cout<<"stack input buffer\t\tAction"<<endl;
	cout<<"_________________________________"<<endl;
	stack[top]='$';
	top++;
	cout<<"$\t\t\tabbcde$\tShift"<<endl;
	stack[top]=str[0];
	top++;
	cout<<"$a\t\tbbcde$\t\tShift"<<endl;
	stack[top]=str[1];
	if(stack[top]=='b')
	{
		cout<<"$ab\t\tbcde$\t\tReduce"<<endl;
		stack[top]='A';
		top++;
		cout<<"$aA\t\tbcde$\t\tShift"<<endl;
		stack[top]='b';
		top++;
		cout<<"$aAb\t\tcde$\t\tShift"<<endl;
		stack[top]='c';
		cout<<"$aAbc\t\tde$\t\tReduce"<<endl;
	}
	if((stack[top]=='c') && (stack[top-1]=='b'))
	{
		top=top-2;
		cout<<"$aA\t\tde$\t\tShift"<<endl;
		top++;
		stack[top]='d';
		cout<<"$aAd\t\te$\t\tReduce"<<endl;
	}
	if(stack[top]=='d')
	{
		stack[top]='B';
		cout<<"$aAB\t\te$\t\tShift"<<endl;
		top++;
		stack[top]='e';
		cout<<"$aABe\t\t$\t\tReduce"<<endl;
		top=top-4;
		stack[top]='s';
		cout<<"$S\t\t$\t\tACCEPT"<<endl;
	}
	if(stack[top]=='S')
	{
		cout<<"String is valid"<<endl;
	}
	else
	{
		cout<<"String is not valid"<<endl;
	}
	return(0);

}
