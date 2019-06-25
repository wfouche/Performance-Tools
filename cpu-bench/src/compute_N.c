/* ----------------------------------------------------------------------- */

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>
#include <unistd.h>

/* ----------------------------------------------------------------------- */

int main(int argc, char* argv[])
{
    struct timeval start, end;
    long secs_used,micros_used;

    if (argc == 1)
    {
	printf ("0.000\n");
        return 0;
    }


    time_t        time_utc;
    struct tm *   time_now;

    int waiting = 0;
    if (argc > 2)
    {
        waiting = atoi(argv[2]);
    }
    while (waiting)
    {
        time(&time_utc);
        time_now = localtime(&time_utc);
        if (time_now->tm_sec == 0)
        {
            waiting = 0;
        }
        else
        {
            // https://stackoverflow.com/questions/1157209/is-there-an-alternative-sleep-function-in-c-to-milliseconds
			// sleep for 10 milliseconds
            usleep(10*1000);
        }
    }

    long n = atol(argv[1]);
    gettimeofday(&start, NULL);
    {

        while (n) { n -= 1; }
		//
		// Intel x64 (gcc -O -S) - machine code.
		//
		// .L9:
		//       subq    $1, %rbx
		//       jne     .L9
		//
    }
    gettimeofday(&end, NULL);

    secs_used=(end.tv_sec - start.tv_sec);
    micros_used= ((secs_used*1000000) + end.tv_usec) - (start.tv_usec);

    double m = micros_used / 1000000.0;
    printf("%lf\n", m);

    return 0;
}

/* ----------------------------------------------------------------------- */
