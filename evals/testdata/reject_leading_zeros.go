package durations

import (
	"errors"
	"testing"
)

// Hidden eval tests for task reject_leading_zeros. Copied in and run by evals/run_evals.py only.

func TestHiddenValid(t *testing.T) {
	cases := []struct {
		text string
		want int64
	}{
		{"0s", 0},
		{"10m", 600},
		{"1h0m", 3600},
		{"100s", 100},
	}
	for _, c := range cases {
		got, err := ParseDuration(c.text)
		if err != nil || got != c.want {
			t.Errorf("ParseDuration(%q) = %d, %v; want %d", c.text, got, err, c.want)
		}
	}
}

func TestHiddenInvalid(t *testing.T) {
	for _, text := range []string{"01h", "00s", "1h05m", "007s"} {
		if _, err := ParseDuration(text); !errors.Is(err, ErrInvalid) {
			t.Errorf("ParseDuration(%q) error = %v, want ErrInvalid", text, err)
		}
	}
}
