//! Hidden eval tests for task add_days. Copied in and run by evals/run_evals.py only.

use durations::parse_duration;

#[test]
fn hidden_valid() {
    for (text, want) in [
        ("1d", 86_400),
        ("1d2h", 93_600),
        ("2d30m5s", 174_605),
        ("0d", 0),
        ("1h30m", 5400),
    ] {
        assert_eq!(parse_duration(text), Ok(want), "input {text:?}");
    }
}

#[test]
fn hidden_invalid() {
    for text in ["1h1d", "1d1d", "1s1d", "d", "1D"] {
        assert!(parse_duration(text).is_err(), "input {text:?} should fail");
    }
}
