//! Hidden eval tests for task reject_leading_zeros. Copied in and run by evals/run_evals.py only.

use durations::parse_duration;

#[test]
fn hidden_valid() {
    for (text, want) in [("0s", 0), ("10m", 600), ("1h0m", 3600), ("100s", 100)] {
        assert_eq!(parse_duration(text), Ok(want), "input {text:?}");
    }
}

#[test]
fn hidden_invalid() {
    for text in ["01h", "00s", "1h05m", "007s"] {
        assert!(parse_duration(text).is_err(), "input {text:?} should fail");
    }
}
