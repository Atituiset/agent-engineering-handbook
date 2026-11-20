"""Parse human-readable durations such as ``"1h30m"`` into seconds."""

from durations.parse import DurationError, parse_duration

__all__ = ["DurationError", "parse_duration"]
