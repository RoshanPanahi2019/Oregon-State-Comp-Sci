#include <omp.h>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <list>
#include <array>


//#define NUMT 4;
int NUMT ;
int mySize;
#define SIZE      	16384 	// you decide
#define NUMTRIES        10	// you decide

float A[SIZE];
float B[SIZE];
float C[SIZE];

int
main(int argc,char*argv[])
{
#ifndef _OPENMP
    fprintf(stderr, "OpenMP is not supported here -- sorry.\n");
    return 1;
#endif

	if (argc=2)
		NUMT = atoi(argv[1]);
		
	if (argc = 3)
		mySize= atoi(argv[2]);

	for (unsigned int a = 0; a < 2; a = a + 1)
	{
		std::cout << "value of a: " << a ;
	}

    // inialize the arrays:
    for (int i = 0; i < mySize; i++)
    {
        A[i] = 1.;
        B[i] = 2.;
    }
	for (int t = 0; t < NUMTRIES; t++)

    omp_set_num_threads(NUMT);
    fprintf(stderr, "Using %d threads\n", NUMT);
    fprintf(stderr, "We have %d processors\n", omp_get_num_procs());

	double minT1 = 0.;
	double sumT1 = 0;
	double executionTime[2];

    for (int t = 0; t < NUMTRIES; t++)
    {
        double time0 = omp_get_wtime();

#pragma omp parallel for
        for (int i = 0; i < SIZE; i++)
        {
            C[i] = A[i] * B[i];
        }
		double time1 = omp_get_wtime();
		double T1 = (time1 - time0) * 10000000;
		sumT1 += T1;
		if (T1 < minT1)
			minT1 = T1;
		if (minT1 == 0) minT1 = T1;
	}
	executionTime[0] = minT1;
	printf("minT1= %8.2lf minT1\n", minT1);

	if (myfile.is_open())
		myfile << minT1 << "\n";

    return 0;
}