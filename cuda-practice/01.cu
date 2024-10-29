#include <iostream>

__global__ void kernel(void) {
    printf("Hello, Cuda\n");
}

int main(void) {
    kernel<<< 1, 1 >>>();
    cudaDeviceSynchronize();
    printf("Hello, world");
    return 0;
}