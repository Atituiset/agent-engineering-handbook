#include "durations/parse.h"

#include <stddef.h>

enum {
    DECIMAL_BASE = 10,
    SECONDS_PER_MINUTE = 60,
    SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE,
};

typedef struct {
    char symbol;
    int64_t seconds;
} unit;

/* Order matters: units must appear in this (descending) order in the input. */
static const unit UNITS[] = {
    {.symbol = 'h', .seconds = SECONDS_PER_HOUR},
    {.symbol = 'm', .seconds = SECONDS_PER_MINUTE},
    {.symbol = 's', .seconds = 1},
};
static const size_t UNIT_COUNT = sizeof UNITS / sizeof UNITS[0];

static int is_digit(char c) { return c >= '0' && c <= '9'; }

durations_status durations_parse(const char *text, int64_t *out_seconds) {
    if (text == NULL || text[0] == '\0') {
        return DURATIONS_ERR_EMPTY;
    }
    int64_t total = 0;
    size_t next_rank = 0; /* index of the first unit still allowed */
    size_t pos = 0;
    while (text[pos] != '\0') {
        const size_t start = pos;
        int64_t amount = 0;
        while (is_digit(text[pos])) {
            const int64_t digit = text[pos] - '0';
            if (amount > (INT64_MAX - digit) / DECIMAL_BASE) {
                return DURATIONS_ERR_OVERFLOW;
            }
            amount = amount * DECIMAL_BASE + digit;
            ++pos;
        }
        if (pos == start || text[pos] == '\0') {
            return DURATIONS_ERR_SYNTAX;
        }
        const char symbol = text[pos++];
        size_t rank = next_rank;
        while (rank < UNIT_COUNT && UNITS[rank].symbol != symbol) {
            ++rank;
        }
        if (rank == UNIT_COUNT) {
            return DURATIONS_ERR_UNIT;
        }
        const int64_t seconds = UNITS[rank].seconds;
        if (amount > (INT64_MAX - total) / seconds) {
            return DURATIONS_ERR_OVERFLOW;
        }
        total += amount * seconds;
        next_rank = rank + 1;
    }
    *out_seconds = total;
    return DURATIONS_OK;
}
