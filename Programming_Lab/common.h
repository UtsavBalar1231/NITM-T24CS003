#ifndef COMMON_H
#define COMMON_H

#define print_arr(inputs, size)             \
do {                                        \
	int i = 0;                          \
	for (; i < (size); ++i) {           \
		printf("%d ", (inputs)[i]); \
	}                                   \
	printf("\n");                       \
} while(0)                                  \

#define get_arr_size(inputs)                           \
do {                                                      \
	int ret = -1; \
	ret = (sizeof((inputs))/sizeof((inputs)[0])); \
	ret; \
} while(0)

#endif // COMMON_H
