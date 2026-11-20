package durations

import (
	"errors"
	"testing"
)

func TestParseDurationValid(t *testing.T) {
	cases := []struct {
		text string
		want int64
	}{
		{"0s", 0},
		{"90s", 90},
		{"1m", 60},
		{"1h30m", 5400},
		{"2h5s", 7205},
		{"1h1m1s", 3661},
	}
	for _, c := range cases {
		t.Run(c.text, func(t *testing.T) {
			got, err := ParseDuration(c.text)
			if err != nil {
				t.Fatalf("ParseDuration(%q) error: %v", c.text, err)
			}
			if got != c.want {
				t.Fatalf("ParseDuration(%q) = %d, want %d", c.text, got, c.want)
			}
		})
	}
}

func TestParseDurationInvalid(t *testing.T) {
	for _, text := range []string{"", "h", "10", "1x", "1m1h", "1h1h", " 1h", "1h ", "99999999999999999999s"} {
		t.Run(text, func(t *testing.T) {
			if _, err := ParseDuration(text); !errors.Is(err, ErrInvalid) {
				t.Fatalf("ParseDuration(%q) error = %v, want ErrInvalid", text, err)
			}
		})
	}
}
