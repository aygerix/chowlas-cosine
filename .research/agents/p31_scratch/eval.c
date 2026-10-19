#include <math.h>
#include <stddef.h>

double cosine_value(const long long *a, size_t n, double x) {
    long double s = 0;
    for (size_t j=0; j<n; ++j) s += cosl((long double)a[j]*x);
    return (double)s;
}

double bu_value(const long long *s, size_t k, double x) {
    long double r = 0, g = 0;
    for (size_t j=0; j<k; ++j) {
        r += cosl((3*(long double)s[j]+0.5L)*x);
        g += cosl((6*(long double)s[j]+1)*x);
    }
    return (double)(r*r-(long double)k/2-g/2);
}
