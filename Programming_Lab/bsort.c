#include <stdio.h>
#include "common.h"

void bubble_sort(int *inputs, int size)
{
	for (int i = 0; i < size; ++i) {
		int swapped = 0;
		if (!swapped) {
			for (int j = i + 1; j < size; ++j) {
				if (inputs[j] < inputs[i]) {
					int temp = inputs[i];
					inputs[i] = inputs[j];
					inputs[j] = temp;
					swapped = 1;
				}
			}
		}
	}
}

int main()
{
	int inputs[7] = {7, 8, 1, 2, 5, 4, 3};
	int size = sizeof(inputs)/sizeof(inputs[0]);
	print_arr(inputs, size);
	bubble_sort(inputs, size);
	print_arr(inputs, size);
}
