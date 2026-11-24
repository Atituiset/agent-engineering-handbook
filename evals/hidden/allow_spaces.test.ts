import { describe, expect, it } from "vitest";

import { DurationError, parseDuration } from "../src/index.js";

describe("allow_spaces (hidden eval)", () => {
  it.each([
    ["1h 30m", 5400],
    ["1h  30m", 5400],
    ["2h 5s", 7205],
    ["1h 1m 1s", 3661],
    ["90s", 90],
  ])("parses %s as %i seconds", (text, expected) => {
    expect(parseDuration(text)).toBe(expected);
  });

  it.each([" 1h", "1h ", "1h\t30m", "1h 1h", "30m 1h", "1 h", " "])("rejects %j", (text) => {
    expect(() => parseDuration(text)).toThrow(DurationError);
  });
});
