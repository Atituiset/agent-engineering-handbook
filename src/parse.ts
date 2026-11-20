/**
 * Duration parsing.
 *
 * Grammar: one or more `<integer><unit>` pairs, units in strictly descending
 * order, each unit at most once. Supported units: `h` (hours), `m` (minutes),
 * `s` (seconds). Examples: `"90s"`, `"1h30m"`, `"2h5s"`.
 */

const UNIT_SECONDS: ReadonlyMap<string, number> = new Map([
  ["h", 3600],
  ["m", 60],
  ["s", 1],
]);
const UNIT_ORDER = [...UNIT_SECONDS.keys()];
const TOKEN = /(\d+)([a-z])/gy;

/** Thrown when a duration string is malformed. */
export class DurationError extends Error {
  override name = "DurationError";
}

/** Return the total number of seconds in `text`. Throws `DurationError` on bad input. */
export function parseDuration(text: string): number {
  if (text === "") {
    throw new DurationError("empty duration");
  }
  TOKEN.lastIndex = 0;
  let pos = 0;
  let total = 0;
  let lastRank = -1;
  while (pos < text.length) {
    const match = TOKEN.exec(text);
    if (match === null) {
      throw new DurationError(`unexpected character at ${String(pos)}: ${JSON.stringify(text)}`);
    }
    const [whole, digits = "", unit = ""] = match;
    const seconds = UNIT_SECONDS.get(unit);
    if (seconds === undefined) {
      throw new DurationError(`unknown unit "${unit}" in ${JSON.stringify(text)}`);
    }
    const rank = UNIT_ORDER.indexOf(unit);
    if (rank <= lastRank) {
      throw new DurationError(`unit "${unit}" repeated or out of order in ${JSON.stringify(text)}`);
    }
    lastRank = rank;
    total += Number(digits) * seconds;
    pos += whole.length;
  }
  return total;
}
