#include <math.h>   
#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

#include <iostream>
#include <fstream>

int	NowYear;		// 2021 - 2026
int	NowMonth;		// 0 - 11

float	NowPrecip;		// inches of rain per month
float	NowTemp;		// temperature this month
float	NowHeight;		// grain height in inches
float	NowinsectEfect;
int	NowNumDeer;		// number of deer in the current population

omp_lock_t	Lock;
int		NumInThreadTeam;
int		NumAtBarrier;
int		NumGone;

void	InitBarrier(int);
void	WaitBarrier();

const float GRAIN_GROWS_PER_MONTH = 9.0;
const float ONE_DEER_EATS_PER_MONTH = 1.0;

const float AVG_PRECIP_PER_MONTH = 7.0;	// average
const float AMP_PRECIP_PER_MONTH = 6.0;	// plus or minus
const float RANDOM_PRECIP = 2.0;	// plus or minus noise

const float AVG_TEMP = 60.0;	// average
const float AMP_TEMP = 20.0;	// plus or minus
const float RANDOM_TEMP = 10.0;	// plus or minus noise

const float MIDTEMP = 40.0;
const float MIDPRECIP = 10.0;

unsigned int seed = 0; // make this global 

void
WaitBarrier()
{
	
	omp_set_lock(&Lock);
	{
		NumAtBarrier++;
		if (NumAtBarrier == NumInThreadTeam)
		{
			NumGone = 0;
			NumAtBarrier = 0;
			// let all other threads get back to what they were doing
// before this one unlocks, knowing that they might immediately
// call WaitBarrier( ) again:
			while (NumGone != NumInThreadTeam - 1);
			omp_unset_lock(&Lock);
			return;
		}
	}
	omp_unset_lock(&Lock);

	while (NumAtBarrier != 0);	// this waits for the nth thread to arrive

#pragma omp atomic
	NumGone++;			// this flags how many threads have returned
}

void
InitBarrier(int n)
{
	n = 3;
	NumInThreadTeam = n;
	NumAtBarrier = 0;
	omp_init_lock(&Lock);
}

float
SQR(float x)
{
	return x * x;
}

float
Ranf(unsigned int* seedp, float low, float high)
{
	float r = (float)rand();              // 0 - RAND_MAX //change this line to  "float r = (float) rand_r( seedp ); "


	return(low + r * (high - low) / (float)RAND_MAX);
}

int
Ranf(unsigned int* seedp, int ilow, int ihigh)
{
	float low = (float)ilow;
	float high = (float)ihigh + 0.9999f;

	return (int)(Ranf(seedp, low, high));
}


void
insectEfect() {
	
	while (NowYear < 2027) {
		float tempFactor = exp(-SQR((NowTemp - MIDTEMP) / 10.));
		float precipFactor = exp(-SQR((NowPrecip - MIDPRECIP) / 10.));
		int Capacity = (int)(NowHeight);
		float nextinsectEfect = NowinsectEfect;
		if (nextinsectEfect < Capacity)
			nextinsectEfect++;
		else
			if (nextinsectEfect > Capacity)
				nextinsectEfect--;

	
		nextinsectEfect += tempFactor * precipFactor*1;
		nextinsectEfect -= (float)NowNumDeer * .5;
		nextinsectEfect += (int)NowHeight*.1 ;
		if (nextinsectEfect < 0)
			nextinsectEfect = 0;
		//std::cout << NowYear;
		WaitBarrier();				//1.
		NowinsectEfect = nextinsectEfect;
		WaitBarrier();				//2.
		//do nothing
		WaitBarrier();				//3. 
	}
}


void
deer() {
	
	while (NowYear < 2027) {

		int nextNumDeer = NowNumDeer;
		int carryingCapacity = (int)(NowHeight);
		int insectCapacity = (int)(NowinsectEfect);

		if (nextNumDeer < insectCapacity)
			nextNumDeer++;
		else
			if (nextNumDeer > insectCapacity)
				nextNumDeer--;

		if (nextNumDeer < carryingCapacity)
			nextNumDeer++;
		else
			if (nextNumDeer > carryingCapacity)
				nextNumDeer--;

		if (nextNumDeer < 0)
			nextNumDeer = 0;

		WaitBarrier();				//1.
		NowNumDeer = nextNumDeer;

		WaitBarrier();				//2.

		// do nothing 
		WaitBarrier();				//3.
	}


}
void


grain() {
	while (NowYear < 2027) {
		float tempFactor = exp(-SQR((NowTemp - MIDTEMP) / 10.));
		float precipFactor = exp(-SQR((NowPrecip - MIDPRECIP) / 10.));

		float nextHeight = NowHeight;
		nextHeight += tempFactor * precipFactor * GRAIN_GROWS_PER_MONTH;
		nextHeight -= (float)NowNumDeer * ONE_DEER_EATS_PER_MONTH;
		nextHeight -= NowinsectEfect*.8;

		if (nextHeight < 0)
			nextHeight = 0;
		
		WaitBarrier();				//1.
		NowHeight = nextHeight;
		WaitBarrier();				//2.
		//do nothing
		WaitBarrier();				//3. 
	}
}

void
watcher() {
	while (NowYear < 2027) {
		//do nothing
		WaitBarrier();						 //1.
		//do nothing
		WaitBarrier();						 //2.
		// write out state:

		std::ofstream myfile;
		myfile.open("Results.txt", std::ios::app);
		std::cout << "   NowYear:" << NowYear << "    NowMonth"<< NowMonth <<"   NowTemp:" << NowTemp << "   NowPrecip:" << NowPrecip << "   NowNumDeer:" << NowNumDeer << "   NowHeight:" << NowHeight<<"   NowinsectEfect: "<< NowinsectEfect << "\n";
		if (myfile.is_open())
			myfile << NowYear << "," << NowMonth << "," << NowTemp << "," << NowPrecip << "," << NowNumDeer << "," << NowHeight << ","<<NowinsectEfect << "\n";
	

		NowMonth += 1;
		//std::cout << NowMonth;
		if (NowMonth%12 == 0) {
			NowYear += 1;
		}

		float ang = (30. * (float)NowMonth + 15.) * (M_PI / 180.);
		float temp = AVG_TEMP - AMP_TEMP * cos(ang);
		float precip = AVG_PRECIP_PER_MONTH + AMP_PRECIP_PER_MONTH * sin(ang);
		NowTemp = temp + Ranf(&seed, -RANDOM_TEMP, RANDOM_TEMP);
		NowPrecip = precip + Ranf(&seed, -RANDOM_PRECIP, RANDOM_PRECIP);
		if (NowPrecip < 0.)
			NowPrecip = 0.;

		WaitBarrier();						 //3.
	}

}

int main()
{
	
#ifndef _OPENMP
	fprintf(stderr, "No OpenMP support!\n");
	return 1;
#endif
	

	NowMonth = 0;
	NowYear = 2021;
	NowNumDeer = 1;
	NowHeight = 1.;
	NowinsectEfect = 1.;

	//std::ofstream myfile;
	//myfile.open("Results.txt", ios::app);
	omp_set_num_threads(4);	// same as # of sections
	InitBarrier(3);
#pragma omp parallel sections // define globals and privates 
	{
#pragma omp section
		{
			deer();	
		}

#pragma omp section
		{
			 grain();
		}

#pragma omp section
		{
			insectEfect();
		}
#pragma omp section
		{
			watcher();
		}
		
//#pragma omp section
	//	{
			//MyAgent();	// your own
		//}
	//}       // implied barrier -- all functions must return in order
		// to allow any of them to get past here

	}	
}		
	


















