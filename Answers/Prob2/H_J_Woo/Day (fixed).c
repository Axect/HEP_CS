#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>


void Calculator_Day(int Day,int Elapsed_time)
{
	int Cal = Day + Elapsed_time;
	int result = (Cal % 7);

	switch (result)
	{
	case 0:
		printf("\nThe day after %d day(s) is Sunday.\n\n",(int)Elapsed_time);
		break;
	case 1:
		printf("\nThe day after %d day(s) is Monday.\n\n", (int)Elapsed_time);
		break;
	case 2:
		printf("\nThe day after %d day(s) is Tuesday.\n\n", (int)Elapsed_time);
		break;
	case 3:
		printf("\nThe day after %d day(s) is Wednesday.\n\n", (int)Elapsed_time);
		break;
	case 4:
		printf("\nThe day after %d day(s) is Thursday.\n\n", (int)Elapsed_time);
		break;
	case 5:
		printf("\nThe day after %d day(s) is Friday.\n\n", (int)Elapsed_time);
		break;
	case 6:
		printf("\nThe day after %d day(s) is Saturday.\n\n", (int)Elapsed_time);
		break;
	}
}


int main()
{
	float Day;
	float Elapsed_time;
	
	printf("\nInsert the day today.\n(Sun=0,Mon1,Tue=2,Wed=3,Thu=4,Fri=5,Sat=6)\n\n");
	scanf("%f", &Day);
	
	for (;;)
	{
		
		if (Day!=(int)Day)
		{
			printf("\nPlease the correct number.\n(Sun=0,Mon1,Tue=2,Wed=3,Thu=4,Fri=5,Sat=6)\n\n");
			scanf("%f", &Day);
		}
		else if (Day != 0 && Day != 1 && Day != 2 && Day != 3 && Day != 4 && Day != 5 && Day != 6)
		{
			printf("\nPlease the correct number.\n(Sun=0,Mon1,Tue=2,Wed=3,Thu=4,Fri=5,Sat=6)\n\n");
			scanf("%f", &Day);
		}
		else
		{
			break;
		}
	}

	printf("\nInsert the Elapsed day.\n(Natural number only)\n\n");
	scanf("%f", &Elapsed_time);

	for (;;)
	{
		if (Elapsed_time!=(int)Elapsed_time||Elapsed_time<0)
		{
			printf("\nPlease the correct number.\n(Only natural number is valid)\n\n");
			scanf("%f", &Elapsed_time);
		}
		else
		{
			break;
		}
	}

	Calculator_Day((int)Day, (int)Elapsed_time);

	return 0;
}