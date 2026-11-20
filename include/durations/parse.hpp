#pragma once

#include <cstdint>
#include <stdexcept>
#include <string_view>

namespace durations {

/// Thrown when a duration string is malformed.
class DurationError : public std::invalid_argument {
  public:
    using std::invalid_argument::invalid_argument;
};

/// Parse a duration such as "1h30m" and return the total number of seconds.
///
/// Grammar: one or more <integer><unit> pairs, units in strictly descending
/// order, each unit at most once. Supported units: h (hours), m (minutes),
/// s (seconds). Examples: "90s", "1h30m", "2h5s".
///
/// Throws DurationError on empty input, unknown units, repeated or
/// out-of-order units, stray characters, or overflow.
[[nodiscard]] std::int64_t parse_duration(std::string_view text);

}  // namespace durations
