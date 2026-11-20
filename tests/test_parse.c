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

static void check_invalid(const char *text, durations_status want) {
    int64_t got = -1;
    TEST_ASSERT_EQUAL_INT_MESSAGE(want, durations_parse(text, &got), text);
    TEST_ASSERT_EQUAL_INT64_MESSAGE(-1, got, text); /* untouched on error */
}

static void test_parses_valid_durations(void) {
    check_valid("0s", 0);
    check_valid("90s", 90);
    check_valid("1m", 60);
    check_valid("1h30m", 5400);
    check_valid("2h5s", 7205);
    check_valid("1h1m1s", 3661);
}

static void test_rejects_invalid_durations(void) {
    check_invalid("", DURATIONS_ERR_EMPTY);
    check_invalid(NULL, DURATIONS_ERR_EMPTY);
    check_invalid("h", DURATIONS_ERR_SYNTAX);
    check_invalid("10", DURATIONS_ERR_SYNTAX);
    check_invalid(" 1h", DURATIONS_ERR_SYNTAX);
    check_invalid("1h ", DURATIONS_ERR_SYNTAX);
    check_invalid("1x", DURATIONS_ERR_UNIT);
    check_invalid("1m1h", DURATIONS_ERR_UNIT);
    check_invalid("1h1h", DURATIONS_ERR_UNIT);
    check_invalid("99999999999999999999s", DURATIONS_ERR_OVERFLOW);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_parses_valid_durations);
    RUN_TEST(test_rejects_invalid_durations);
    return UNITY_END();
}
