#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
    struct timeval start, end;
    long secs_used,micros_used;

    if (argc == 1)
    {
	printf ("0.000\n");
        return 0;
    }

    long n = atol(argv[1]);

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
           usleep(100*000);
        }
    }

    gettimeofday(&start, NULL);
    {
        while (n) { n -= 1; }
    }
    gettimeofday(&end, NULL);

    secs_used=(end.tv_sec - start.tv_sec);
    micros_used= ((secs_used*1000000) + end.tv_usec) - (start.tv_usec);

    double m = micros_used / 1000000.0;
    printf("%lf\n", m);

    return 0;
}
