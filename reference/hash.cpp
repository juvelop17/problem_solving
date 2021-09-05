//
// Created by Junho Kim on 2021/08/19.
//


#define HASH_SIZE (1<<20)
#define HASH_DIV (HASH_SIZE-1)

unsigned long djb2(const char* str) {
    unsigned long hash = 5381;
    int c;
    while (c = *str++) {
        hash = (((hash << 5) + hash) + c);
    }

    return hash & HASH_DIV;
}


