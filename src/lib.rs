//! Parse human-readable durations such as `"1h30m"` into seconds.
//!
//! Grammar: one or more `<integer><unit>` pairs, units in strictly descending
//! order, each unit at most once. Supported units: `h` (hours), `m` (minutes),
//! `s` (seconds). Examples: `"90s"`, `"1h30m"`, `"2h5s"`.

use std::fmt;

/// Error returned for malformed durations.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct DurationError(String);

impl fmt::Display for DurationError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "invalid duration: {}", self.0)
    }
}

impl std::error::Error for DurationError {}

/// Units in the (descending) order they must appear in the input.
const UNITS: [(u8, u64); 3] = [(b'h', 3600), (b'm', 60), (b's', 1)];

/// Return the total number of seconds in `text`.
///
/// # Errors
///
/// Returns [`DurationError`] if `text` is empty, has an unknown unit, repeats
/// a unit, lists units out of order, has stray characters, or overflows `u64`.
pub fn parse_duration(text: &str) -> Result<u64, DurationError> {
    let fail = |why: &str| Err(DurationError(format!("{why} in {text:?}")));
    if text.is_empty() {
        return fail("empty");
    }
    let bytes = text.as_bytes();
    let mut total: u64 = 0;
    let mut next_rank = 0; // index of the first unit still allowed
    let mut pos = 0;
    while pos < bytes.len() {
        let start = pos;
        let mut amount: u64 = 0;
        while pos < bytes.len() && bytes[pos].is_ascii_digit() {
            let digit = u64::from(bytes[pos] - b'0');
            let Some(next) = amount.checked_mul(10).and_then(|a| a.checked_add(digit)) else {
                return fail("number too large");
            };
            amount = next;
            pos += 1;
        }
        if pos == start {
            return fail(&format!("expected a number at {pos}"));
        }
        let Some(&symbol) = bytes.get(pos) else {
            return fail("missing unit at end");
        };
        pos += 1;
        let Some(offset) = UNITS[next_rank..].iter().position(|&(s, _)| s == symbol) else {
            return fail(&format!(
                "unknown, repeated or out-of-order unit {:?}",
                char::from(symbol)
            ));
        };
        let rank = next_rank + offset;
        let seconds = UNITS[rank].1;
        let Some(sum) = amount
            .checked_mul(seconds)
            .and_then(|s| total.checked_add(s))
        else {
            return fail("duration too large");
        };
        total = sum;
        next_rank = rank + 1;
    }
    Ok(total)
}
