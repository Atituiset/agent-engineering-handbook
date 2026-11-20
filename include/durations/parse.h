#ifndef DURATIONS_PARSE_H
#define DURATIONS_PARSE_H

#include <stdint.h>

#if defined(__GNUC__) || defined(__clang__)
#define DURATIONS_NODISCARD __attribute__((warn_unused_result))
#else
#define DURATIONS_NODISCARD
#endif

typedef enum {
    DURATIONS_OK = 0,
    DURATIONS_ERR_EMPTY,    /* empty or NULL input */
    DURATIONS_ERR_SYNTAX,   /* stray character, missing number or unit */
    DURATIONS_ERR_UNIT,     /* unknown, repeated or out-of-order unit */
    DURATIONS_ERR_OVERFLOW, /* result does not fit in int64_t */
} durations_status;

/*
 * Parse a duration such as "1h30m" and store the total number of seconds in
 * *out_seconds. *out_seconds is only written on success.
 *
 * Grammar: one or more <integer><unit> pairs, units in strictly descending
 * order, each unit at most once. Supported units: h (hours), m (minutes),
 * s (seconds). Examples: "90s", "1h30m", "2h5s".
 */
DURATIONS_NODISCARD durations_status durations_parse(const char *text, int64_t *out_seconds);

#endif /* DURATIONS_PARSE_H */
