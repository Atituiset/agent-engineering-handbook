package durations

import (
	"errors"
	"testing"
)

// Hidden eval tests for task allow_spaces. Copied in and run by evals/run_evals.py only.

func TestHiddenValid(t *testing.T) {
	cases := []struct {
		text string
		want int64
	}{
		{"1h 30m", 5400},
		{"1h  30m", 5400},
		{"2h 5s", 7205},
		{"1h 1m 1s", 3661},
		{"90s", 90},
	}
	for _, c := range cases {
		got, err := ParseDuration(c.text)
		if err != nil || got != c.want {
			t.Errorf("ParseDuration(%q) = %d, %v; want %d", c.text, got, err, c.want)
		}
	}
}

func TestHiddenInvalid(t *testing.T) {
	for _, text := range []string{" 1h", "1h ", "1h\t30m", "1h 1h", "30m 1h", "1 h", " "} {
		if _, err := ParseDuration(text); !errors.Is(err, ErrInvalid) {
			t.Errorf("ParseDuration(%q) error = %v, want ErrInvalid", text, err)
		}
	}
}
