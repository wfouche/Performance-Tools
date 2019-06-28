/* ----------------------------------------------------------------------- */

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>
#include <unistd.h>

#include <pthread.h>
#include <errno.h>
#include <ctype.h>

/* ----------------------------------------------------------------------- */

double compute_N(int waiting, long n) {
    struct timeval start, end;
    long secs_used,micros_used;
    time_t        time_utc;
    struct tm *   time_now;	

    while (waiting) {
        time(&time_utc);
        time_now = localtime(&time_utc);
        if (time_now->tm_sec == 0) {
            waiting = 0;
        } else {
            // https://stackoverflow.com/questions/1157209/is-there-an-alternative-sleep-function-in-c-to-milliseconds
            // sleep for 10 milliseconds
            usleep(10*1000);
        }
    }

    gettimeofday(&start, NULL); 
    {
        while (n) { 
            //
            // Intel x64 (gcc -O -S) - machine code.
            //
            // .L9:
            //       subq    $1, %rbx
            //       jne     .L9
            //
            n -= 1;
	}
    }
    gettimeofday(&end, NULL);

    secs_used =(end.tv_sec - start.tv_sec);
    micros_used = ((secs_used*1000000) + end.tv_usec) - (start.tv_usec);

    double m = micros_used / 1000000.0;
    // printf("%lf\n", m);	
    return m;
}

/* ----------------------------------------------------------------------- */

int main(int argc, char* argv[]) {

    if (argc == 1) {
        printf ("0.000\n");
        return 0;
    }

    long n = atol(argv[1]);

    int waiting = 0;
	int num_threads = 0;
    if (argc == 3) {
        waiting = 1;
        num_threads = atoi(argv[2]);
    }
 	
    if (num_threads == 0) {
        // Multiple processes
        double elapsed_time = compute_N(waiting, n);
        printf("%lf\n", elapsed_time);	
    } else {
        // Multiple threads
        printf("compute_N.c: multi-threading - not yet support.\n");
        exit(1);
    }
	
    return 0;
}

/* ----------------------------------------------------------------------- */
