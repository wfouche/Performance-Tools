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

long N = 0;

/* ----------------------------------------------------------------------- */

double compute_N(int waiting) {
  struct timeval start, end;
  long secs_used, micros_used;
  time_t time_utc;
  struct tm * time_now;

  long n = N;

  while (waiting) {
    time( & time_utc);
    time_now = localtime( & time_utc);
    if (time_now->tm_sec == 0) {
      waiting = 0;
    } else {
      // https://stackoverflow.com/questions/1157209/is-there-an-alternative-sleep-function-in-c-to-milliseconds
      // sleep for 10 milliseconds
      usleep(10 * 1000);
    }
  }

  gettimeofday( & start, NULL); {
    while (n) {
      n -= 1;
      //
      // Intel x64 (gcc -O -S) - machine code.
      //
      // .L9:
      //       subq    $1, %rbx
      //       jne     .L9
      //
    }
  }
  gettimeofday( & end, NULL);

  secs_used = (end.tv_sec - start.tv_sec);
  micros_used = ((secs_used * 1000000) + end.tv_usec) - (start.tv_usec);

  double m = micros_used / 1000000.0;
  // printf("%lf\n", m);	
  return m;
}

/* ----------------------------------------------------------------------- */

void * worker_thread(void * x_void_ptr) {
  int waiting = 1;
  double elapsed_time = compute_N(waiting);

  double * x_ptr = (double * ) x_void_ptr;
  *x_ptr = elapsed_time;

  return NULL;
}

/* ----------------------------------------------------------------------- */

int main(int argc, char * argv[]) {

  if (argc == 1) {
    printf("0.000\n");
    return 0;
  }

  long n = atol(argv[1]);

  N = n;

  int waiting = 0;
  int num_threads = 0;
  if (argc == 3) {
    waiting = 1;
    num_threads = atoi(argv[2]);
  }

  if (num_threads == 0) {
    // Multiple processes
    double elapsed_time = compute_N(waiting);
    printf("%lf\n", elapsed_time);
  } else {
    // Multiple threads
    double elapsed_times[num_threads];
    pthread_t threads[num_threads];

    for (int i = 0; i < num_threads; i++) {
      elapsed_times[i] = -1.0;

      if (pthread_create( &threads[i], NULL, worker_thread, &elapsed_times[i])) {
        fprintf(stderr, "Error creating thread\n");
        return 1;
      }
    }

    for (int i = 0; i < num_threads; i++) {
      if (pthread_join(threads[i], NULL)) {
        fprintf(stderr, "Error joining thread\n");
        return 2;
      }
      printf("%lf\n", elapsed_times[i]);
    }
  }

  return 0;
}

/* ----------------------------------------------------------------------- */