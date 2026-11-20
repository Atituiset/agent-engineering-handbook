#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest.h>

#include <string_view>

#include "durations/parse.hpp"

using durations::DurationError;
using durations::parse_duration;

TEST_CASE("parses valid durations") {
    CHECK(parse_duration("0s") == 0);
    CHECK(parse_duration("90s") == 90);
    CHECK(parse_duration("1m") == 60);
    CHECK(parse_duration("1h30m") == 5400);
    CHECK(parse_duration("2h5s") == 7205);
    CHECK(parse_duration("1h1m1s") == 3661);
}

TEST_CASE("rejects invalid durations") {
    for (std::string_view text :
         {"", "h", "10", "1x", "1m1h", "1h1h", " 1h", "1h ", "99999999999999999999s"}) {
        CAPTURE(text);
        CHECK_THROWS_AS((void)parse_duration(text), DurationError);
    }
}
