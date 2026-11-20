// Package durations parses human-readable durations such as "1h30m" into seconds.
//
// Grammar: one or more <integer><unit> pairs, units in strictly descending
// order, each unit at most once. Supported units: h (hours), m (minutes),
// s (seconds). Examples: "90s", "1h30m", "2h5s".
package durations

import (
	"errors"
	"fmt"
	"math"
)

// ErrInvalid is wrapped by every error ParseDuration returns.
var ErrInvalid = errors.New("invalid duration")

type unit struct {
	symbol  byte
	seconds int64
}

// Order matters: units must appear in this (descending) order in the input.
var units = []unit{
	{symbol: 'h', seconds: 3600},
	{symbol: 'm', seconds: 60},
	{symbol: 's', seconds: 1},
}

// ParseDuration returns the total number of seconds in text.
// Every error wraps ErrInvalid, so callers can use errors.Is(err, ErrInvalid).
func ParseDuration(text string) (int64, error) {
	if text == "" {
		return 0, fmt.Errorf("%w: empty", ErrInvalid)
	}
	var total int64
	nextRank := 0 // index of the first unit still allowed
	pos := 0
	for pos < len(text) {
		start := pos
		var amount int64
		for pos < len(text) && text[pos] >= '0' && text[pos] <= '9' {
			digit := int64(text[pos] - '0')
			if amount > (math.MaxInt64-digit)/10 {
				return 0, fmt.Errorf("%w: number too large in %q", ErrInvalid, text)
			}
			amount = amount*10 + digit
			pos++
		}
		if pos == start {
			return 0, fmt.Errorf("%w: expected a number at %d in %q", ErrInvalid, pos, text)
		}
		if pos == len(text) {
			return 0, fmt.Errorf("%w: missing unit at end of %q", ErrInvalid, text)
		}
		symbol := text[pos]
		pos++
		rank := nextRank
		for rank < len(units) && units[rank].symbol != symbol {
			rank++
		}
		if rank == len(units) {
			return 0, fmt.Errorf("%w: unknown, repeated or out-of-order unit %q in %q", ErrInvalid, symbol, text)
		}
		seconds := units[rank].seconds
		if amount > (math.MaxInt64-total)/seconds {
			return 0, fmt.Errorf("%w: duration too large in %q", ErrInvalid, text)
		}
		total += amount * seconds
		nextRank = rank + 1
	}
	return total, nil
}
