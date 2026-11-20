//! Behaviour tests for `parse_duration`.

use durations::parse_duration;

#[test]
fn parses_valid_durations() {
    let cases = [
        ("0s", 0),
        ("90s", 90),
        ("1m", 60),
        ("1h30m", 5400),
        ("2h5s", 7205),
        ("1h1m1s", 3661),
    ];
    for (text, want) in cases {
        assert_eq!(parse_duration(text), Ok(want), "input {text:?}");
    }
}

#[test]
fn rejects_invalid_durations() {
    for text in [
        "",
        "h",
        "10",
        "1x",
        "1m1h",
        "1h1h",
        " 1h",
        "1h ",
        "99999999999999999999s",
    ] {
        assert!(parse_duration(text).is_err(), "input {text:?} should fail");
    }
}
