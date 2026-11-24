// Hidden eval tests for task add_days. Compiled by evals/run_evals.py, never by CMake.
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest.h>

#include <cstdint>
#include <string_view>
#include <utility>
#include <vector>

#include "durations/parse.hpp"

using durations::DurationError;
using durations::parse_duration;

TEST_CASE("add_days (hidden eval)") {
    const std::vector<std::pair<std::string_view, std::int64_t>> valid{
        {{"1d", 86400}, {"1d2h", 93600}, {"2d30m5s", 174605}, {"0d", 0}, {"1h30m", 5400}}};
    for (const auto& [text, want] : valid) {
        CAPTURE(text);
        CHECK(parse_duration(text) == want);
    }
    for (std::string_view text : {"1h1d", "1d1d", "1s1d", "d", "1D"}) {
        CAPTURE(text);
        CHECK_THROWS_AS((void)parse_duration(text), DurationError);
    }
}
