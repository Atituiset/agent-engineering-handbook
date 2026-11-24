/* Hidden eval tests for task add_days. Compiled by evals/run_evals.py, never by CMake. */
#include <stddef.h>
#include <stdint.h>
#include <unity.h>

#include "durations/parse.h"

void setUp(void) {}
void tearDown(void) {}

static void check_valid(const char *text, int64_t want) {
    int64_t got = -1;
    TEST_ASSERT_EQUAL_INT_MESSAGE(DURATIONS_OK, durations_parse(text, &got), text);
    TEST_ASSERT_EQUAL_INT64_MESSAGE(want, got, text);
}

static void check_invalid(const char *text) {
    int64_t got = -1;
    TEST_ASSERT_NOT_EQUAL_INT_MESSAGE(DURATIONS_OK, durations_parse(text, &got), text);
}

static void test_add_days(void) {
    check_valid("1d", 86400);
    check_valid("1d2h", 93600);
    check_valid("2d30m5s", 174605);
    check_valid("0d", 0);
    check_valid("1h30m", 5400);
    check_invalid("1h1d");
    check_invalid("1d1d");
    check_invalid("1s1d");
    check_invalid("d");
    check_invalid("1D");
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_add_days);
    return UNITY_END();
}
