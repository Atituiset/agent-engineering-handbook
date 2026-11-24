/* Hidden eval tests for task reject_leading_zeros. Compiled by evals/run_evals.py, never by CMake.
 */
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

static void test_reject_leading_zeros(void) {
    check_valid("0s", 0);
    check_valid("10m", 600);
    check_valid("1h0m", 3600);
    check_valid("100s", 100);
    check_invalid("01h");
    check_invalid("00s");
    check_invalid("1h05m");
    check_invalid("007s");
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_reject_leading_zeros);
    return UNITY_END();
}
