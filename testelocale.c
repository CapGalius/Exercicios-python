// locale test

#include <stdio.h>
#include <locale.h>
#include <time.h>

// locale test
void locale_test() {
    // use environment variable to get locale setting,
    setlocale(LC_ALL, "");

    char buf[26];
    time_t now = time(NULL);
    ctime_r(&now, buf);
    printf("time: %s", buf);

    char *time_locale = setlocale(LC_TIME, NULL);
    printf("current LC_TIME locale: %s\n", time_locale);
}

int main(int argc, char *argv[]) {
    locale_test();
    return 0;
}