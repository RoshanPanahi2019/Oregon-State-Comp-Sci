#include <math.h>   
#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
using namespace std;
#define XMIN     -1.
#define XMAX      1.
#define YMIN     -1.
#define YMAX      1.

#define N	0.70

int NUMNODES = 100; // numbr of subdivisions  
int NUMT = 2; // number of threads
int NUMTRIES = 8;

float Height(int, int);	// function prototype

float
Height(int iu, int iv)	// iu,iv = 0 .. NUMNODES-1
{
	float x = -1. + 2. * (float)iu / (float)(NUMNODES - 1);	// -1. to +1.
	float y = -1. + 2. * (float)iv / (float)(NUMNODES - 1);	// -1. to +1.

	float xn = pow(fabs(x), (double)N);
	float yn = pow(fabs(y), (double)N);
	float r = 1. - xn - yn;
	if (r <= 0.)
		return 0.;
	float height = pow(r, 1. / (float)N);
	return height;
}

int main(int argc, char* argv[])
{
#ifndef _OPENMP
	fprintf(stderr, "No OpenMP support!\n");
	return 1;
#endif
		std::ofstream myfile;
		myfile.open("Results.txt", ios::app);

		if (argc = 2)
			NUMT = atoi(argv[1]);

		if (argc = 3)
			NUMNODES = atoi(argv[2]);
		omp_set_num_threads(NUMT);

		const float fullTileArea = (((XMAX - XMIN) / (float)(NUMNODES - 1)) *
		((YMAX - YMIN) / (float)(NUMNODES - 1)));
		const float halfTileArea = (float)(fullTileArea / 2);
		const float quarterTileArea = (float)( fullTileArea / 4);
		float totalVolume;
		float maxPerformance = 0;

		for (int j = 0; j < NUMTRIES; j++) 
		{
			float volume = 0;
			double time0 = omp_get_wtime();
#pragma omp parallel for reduction(+:volume)
			for (int i = 0; i < NUMNODES * NUMNODES; i++)
			{
				int iu = i % NUMNODES;
				int iv = i / NUMNODES;
				float z = Height(iu, iv);
				float area;

				if ((iu != (NUMNODES - 1) && iu != 0) && (iv != (NUMNODES - 1) && iv != 0))
				{
					area = fullTileArea;
				}
				else
				{
					if ((iu == (NUMNODES - 1) || iu == 0) && (iv == (NUMNODES - 1) || iv == 0))
					{
						area = quarterTileArea;
					}
					else
					{
						area = halfTileArea;
					}
				}
				volume += 2 * z * area;
				totalVolume = volume;

			}
		
			double time1 = omp_get_wtime();
			double megaHeightsPerSecond = (double)(NUMNODES * NUMNODES) / (time1 - time0) / 1000000.0;

			if (megaHeightsPerSecond > maxPerformance)
			{
				maxPerformance = megaHeightsPerSecond;
			}
			/*if (j == 7)
			{
				std::cout << "   volume  " << totalVolume;
				//write this to the file and create the report
			}*/
		}
		
		fprintf(stderr, "%2d threads : %8d NUMNODES ;  MegaHeights/sec = %6.2lf\n",
			NUMT, NUMNODES, maxPerformance);
		if (myfile.is_open())
			myfile << NUMT << ", " << NUMNODES << ", " << maxPerformance << "\n";

		//%6.2lf volume;
	
	// sum up the weighted heights into the variable "volume"
	// using an OpenMP for loop and a reduction:

	//? ? ? ? ?
}
