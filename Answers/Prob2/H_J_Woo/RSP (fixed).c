#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void RSP_result(int User, int PC)
{
	if (User!=0&&User!=1&&User!=2&&PC!=0&&PC!=1&&PC!=2)
	{
		return "No valid";
	}
	
	else if (User == PC)
	{
		switch (User)
		{
		case 0:
			printf("Draw\n (User-Rock,PC-Rock)\n\n");
			break;
		case 1:
			printf("Draw\n (User-Scissors,PC-Scissors)\n\n");
			break;
		case 2:
			printf("Draw\n (User-Paper,PC-Paper)\n\n");
			break;
		}

	}
	else
	{
		switch (User)
		{
		case 0:
			if (PC == 1)
				printf("User wins.\n (User-Rock,PC-Scissors)\n\n");
			else
				printf("PC wins.\n (User-Rock,PC-Paper)\n\n");
			break;
		case 1:
			if (PC == 2)
				printf("User wins.\n (User-Scissors,PC-Paper)\n\n");
			else
				printf("PC wins.\n (User-Scissors,PC-rock)\n\n");
			break;
		case 2:
			if (PC == 0)
				printf("User wins.\n (User-Paper,PC-Rock)\n\n");
			else
				printf("PC wins.\n (User-Paper,PC-Scissors)\n\n");
			break;

		}
	}
}


int main()
{
	float UserSelect;
	float PCSelect;
	float cont;
	srand(time(NULL));

GAME:

	printf("\n<<Please Select the number>>\n(Rock=0,Scissors=1,Paper=2)\n\n");
	PCSelect = (rand() % 3);

	scanf("%f", &UserSelect);

	for (;;)
	{

		if (UserSelect == 0 || UserSelect == 1 || UserSelect == 2)
		{
			printf("\n\n[[Wait some microseconds.]]\n\n\n");
			break;
		}
		else
		{
			printf("\n<<Please insert the right number>>\n(Rock=0,Scissors=1,Paper=2)\n\n");
			scanf("%f", &UserSelect);
		}
	}

	RSP_result((int)UserSelect, (int)PCSelect);

	printf("\n\nDo you want to play again?\n(Yes=0,no=1)\n\n");
	scanf("%f", &cont);
	for (;;)
	{

		if (cont == 1)
		{
			printf("\n\nThank you for your play.\nHave a nice day!\n\n");
			break;
		}
		else if (cont == 0)
		{
			goto GAME;
		}
		else
		{
			printf("\n<<Please insert the right number>>\n\nDo you want to play again?\n(Yes=0,no=1)\n");
			scanf("%f", &cont);
		}
	}

	return 0;
}