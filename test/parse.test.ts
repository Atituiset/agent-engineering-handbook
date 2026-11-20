import { describe, expect, it } from "vitest";

import { DurationError, parseDuration } from "../src/index.js";

describe("parseDuration", () => {
  it.each([
    ["0s", 0],
    ["90s", 90],
    ["1m", 60],
    ["1h30m", 5400],
    ["2h5s", 7205],
    ["1h1m1s", 3661],
  ])("parses %s as %i seconds", (text, expected) => {
    expect(parseDuration(text)).toBe(expected);
  });

  it.each(["", "h", "10", "1x", "1m1h", "1h1h", " 1h", "1h "])("rejects %j", (text) => {
    expect(() => parseDuration(text)).toThrow(DurationError);
  });
});
