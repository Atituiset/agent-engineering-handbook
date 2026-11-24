import { describe, expect, it } from "vitest";

import { DurationError, parseDuration } from "../src/index.js";

describe("add_days (hidden eval)", () => {
  it.each([
    ["1d", 86400],
    ["1d2h", 93600],
    ["2d30m5s", 174605],
    ["0d", 0],
    ["1h30m", 5400],
  ])("parses %s as %i seconds", (text, expected) => {
    expect(parseDuration(text)).toBe(expected);
  });

  it.each(["1h1d", "1d1d", "1s1d", "d", "1D"])("rejects %j", (text) => {
    expect(() => parseDuration(text)).toThrow(DurationError);
  });
});
