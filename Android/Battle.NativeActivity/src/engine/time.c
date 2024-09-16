#include "time.h"

#include "platform.h"

double get_time()
{
	struct timespec ts;

	clock_gettime(CLOCK_MONOTONIC, &ts);

	return ts.tv_sec + ts.tv_nsec / 1e9;
}

void sleep(double duration)
{
	if (duration <= 0.0)
	{
		return;
	}

	struct timespec ts;

	ts.tv_sec = floor(duration);

	ts.tv_nsec = fmod(duration, 1.0) * 1e9;

	clock_nanosleep(CLOCK_MONOTONIC, 0, &ts, NULL);
}
