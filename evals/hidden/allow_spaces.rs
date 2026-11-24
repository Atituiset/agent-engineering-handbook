//! Hidden eval tests for task allow_spaces. Copied in and run by evals/run_evals.py only.

use durations::parse_duration;

#[test]
fn hidden_valid() {
    for (text, want) in [
        ("1h 30m", 5400),
        ("1h  30m", 5400),
        ("2h 5s", 7205),
        ("1h 1m 1s", 3661),
        ("90s", 90),
    ] {
        assert_eq!(parse_duration(text), Ok(want), "input {text:?}");
    }
}

#[test]
fn hidden_invalid() {
    for text in [" 1h", "1h ", "1h\t30m", "1h 1h", "30m 1h", "1 h", " "] {
        assert!(parse_duration(text).is_err(), "input {text:?} should fail");
    }
}
