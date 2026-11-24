/* Hidden eval tests for task allow_spaces. Compiled by evals/run_evals.py, never by CMake. */
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

static void test_allow_spaces(void) {
    check_valid("1h 30m", 5400);
    check_valid("1h  30m", 5400);
    check_valid("2h 5s", 7205);
    check_valid("1h 1m 1s", 3661);
    check_valid("90s", 90);
    check_invalid(" 1h");
    check_invalid("1h ");
    check_invalid("1h\t30m");
    check_invalid("1h 1h");
    check_invalid("30m 1h");
    check_invalid("1 h");
    check_invalid(" ");
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_allow_spaces);
    return UNITY_END();
}
