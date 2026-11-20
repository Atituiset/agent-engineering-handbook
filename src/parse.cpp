#include "durations/parse.hpp"

#include <array>
#include <cstddef>
#include <limits>
#include <string>

namespace durations {
namespace {

struct Unit {
    char symbol;
    std::int64_t seconds;
};

// Order matters: units must appear in this (descending) order in the input.
constexpr std::array<Unit, 3> kUnits{{
    {.symbol = 'h', .seconds = 3600},
    {.symbol = 'm', .seconds = 60},
    {.symbol = 's', .seconds = 1},
}};

[[noreturn]] void fail(const std::string& why, std::string_view text) {
    throw DurationError(why + " in \"" + std::string(text) + "\"");
}

bool is_digit(char c) { return c >= '0' && c <= '9'; }

}  // namespace

std::int64_t parse_duration(std::string_view text) {
    if (text.empty()) {
        throw DurationError("empty duration");
    }
    constexpr std::int64_t kMax = std::numeric_limits<std::int64_t>::max();
    std::int64_t total = 0;
    std::size_t pos = 0;
    std::size_t next_rank = 0;  // index of the first unit still allowed
    while (pos < text.size()) {
        const std::size_t digits_start = pos;
        std::int64_t amount = 0;
        while (pos < text.size() && is_digit(text[pos])) {
            const auto digit = static_cast<std::int64_t>(text[pos] - '0');
            if (amount > (kMax - digit) / 10) {
                fail("number too large", text);
            }
            amount = amount * 10 + digit;
            ++pos;
        }
        if (pos == digits_start) {
            fail("expected a number at " + std::to_string(pos), text);
        }
        if (pos == text.size()) {
            fail("missing unit at end", text);
        }
        const char symbol = text[pos++];
        std::size_t rank = next_rank;
        while (rank < kUnits.size() && kUnits.at(rank).symbol != symbol) {
            ++rank;
        }
        if (rank == kUnits.size()) {
            fail(std::string("unknown, repeated or out-of-order unit '") + symbol + "'", text);
        }
        const std::int64_t seconds = kUnits.at(rank).seconds;
        if (amount > (kMax - total) / seconds) {
            fail("duration too large", text);
        }
        total += amount * seconds;
        next_rank = rank + 1;
    }
    return total;
}

}  // namespace durations
