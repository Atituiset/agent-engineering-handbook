// Hidden eval tests for task allow_spaces. Compiled by evals/run_evals.py, never by CMake.
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest.h>

#include <cstdint>
#include <string_view>
#include <utility>
#include <vector>

#include "durations/parse.hpp"

using durations::DurationError;
using durations::parse_duration;

TEST_CASE("allow_spaces (hidden eval)") {
    const std::vector<std::pair<std::string_view, std::int64_t>> valid{
        {{"1h 30m", 5400}, {"1h  30m", 5400}, {"2h 5s", 7205}, {"1h 1m 1s", 3661}, {"90s", 90}}};
    for (const auto& [text, want] : valid) {
        CAPTURE(text);
        CHECK(parse_duration(text) == want);
    }
    for (std::string_view text : {" 1h", "1h ", "1h\t30m", "1h 1h", "30m 1h", "1 h", " "}) {
        CAPTURE(text);
        CHECK_THROWS_AS((void)parse_duration(text), DurationError);
    }
}
