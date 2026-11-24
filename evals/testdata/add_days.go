package durations

import (
	"errors"
	"testing"
)

// Hidden eval tests for task add_days. Copied in and run by evals/run_evals.py only.

func TestHiddenValid(t *testing.T) {
	cases := []struct {
		text string
		want int64
	}{
		{"1d", 86400},
		{"1d2h", 93600},
		{"2d30m5s", 174605},
		{"0d", 0},
		{"1h30m", 5400},
	}
	for _, c := range cases {
		got, err := ParseDuration(c.text)
		if err != nil || got != c.want {
			t.Errorf("ParseDuration(%q) = %d, %v; want %d", c.text, got, err, c.want)
		}
	}
}

func TestHiddenInvalid(t *testing.T) {
	for _, text := range []string{"1h1d", "1d1d", "1s1d", "d", "1D"} {
		if _, err := ParseDuration(text); !errors.Is(err, ErrInvalid) {
			t.Errorf("ParseDuration(%q) error = %v, want ErrInvalid", text, err)
		}
	}
}
