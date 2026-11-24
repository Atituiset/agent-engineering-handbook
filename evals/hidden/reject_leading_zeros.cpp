// Hidden eval tests for task reject_leading_zeros. Compiled by evals/run_evals.py, never by CMake.
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest.h>

#include <cstdint>
#include <string_view>
#include <utility>
#include <vector>

#include "durations/parse.hpp"

using durations::DurationError;
using durations::parse_duration;

TEST_CASE("reject_leading_zeros (hidden eval)") {
    const std::vector<std::pair<std::string_view, std::int64_t>> valid{
        {{"0s", 0}, {"10m", 600}, {"1h0m", 3600}, {"100s", 100}}};
    for (const auto& [text, want] : valid) {
        CAPTURE(text);
        CHECK(parse_duration(text) == want);
    }
    for (std::string_view text : {"01h", "00s", "1h05m", "007s"}) {
        CAPTURE(text);
        CHECK_THROWS_AS((void)parse_duration(text), DurationError);
    }
}
