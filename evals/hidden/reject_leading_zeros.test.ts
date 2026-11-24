import { describe, expect, it } from "vitest";

import { DurationError, parseDuration } from "../src/index.js";

describe("reject_leading_zeros (hidden eval)", () => {
  it.each([
    ["0s", 0],
    ["10m", 600],
    ["1h0m", 3600],
    ["100s", 100],
  ])("parses %s as %i seconds", (text, expected) => {
    expect(parseDuration(text)).toBe(expected);
  });

  it.each(["01h", "00s", "1h05m", "007s"])("rejects %j", (text) => {
    expect(() => parseDuration(text)).toThrow(DurationError);
  });
});
