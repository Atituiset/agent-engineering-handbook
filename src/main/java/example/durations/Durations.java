package example.durations;

import java.util.List;

/**
 * Parse human-readable durations such as {@code "1h30m"} into seconds.
 *
 * <p>Grammar: one or more {@code <integer><unit>} pairs, units in strictly descending order, each
 * unit at most once. Supported units: {@code h} (hours), {@code m} (minutes), {@code s} (seconds).
 * Examples: {@code "90s"}, {@code "1h30m"}, {@code "2h5s"}.
 */
public final class Durations {

  private record Unit(char symbol, long seconds) {}

  /** Units in the (descending) order they must appear in the input. */
  private static final List<Unit> UNITS =
      List.of(new Unit('h', 3600), new Unit('m', 60), new Unit('s', 1));

  private Durations() {}

  /**
   * Returns the total number of seconds in {@code text}.
   *
   * @throws DurationException if {@code text} is empty, has an unknown, repeated or out-of-order
   *     unit, has stray characters, or overflows {@code long}
   */
  public static long parse(String text) {
    if (text == null || text.isEmpty()) {
      throw new DurationException("empty duration");
    }
    long total = 0;
    int nextRank = 0; // index of the first unit still allowed
    int pos = 0;
    while (pos < text.length()) {
      int start = pos;
      long amount = 0;
      while (pos < text.length() && text.charAt(pos) >= '0' && text.charAt(pos) <= '9') {
        try {
          amount = Math.addExact(Math.multiplyExact(amount, 10), text.charAt(pos) - '0');
        } catch (ArithmeticException e) {
          throw new DurationException("number too large in \"" + text + "\"", e);
        }
        pos++;
      }
      if (pos == start || pos == text.length()) {
        throw new DurationException("expected <number><unit> at " + start + " in \"" + text + "\"");
      }
      char symbol = text.charAt(pos++);
      int rank = nextRank;
      while (rank < UNITS.size() && UNITS.get(rank).symbol() != symbol) {
        rank++;
      }
      if (rank == UNITS.size()) {
        throw new DurationException(
            "unknown, repeated or out-of-order unit '" + symbol + "' in \"" + text + "\"");
      }
      try {
        total = Math.addExact(total, Math.multiplyExact(amount, UNITS.get(rank).seconds()));
      } catch (ArithmeticException e) {
        throw new DurationException("duration too large in \"" + text + "\"", e);
      }
      nextRank = rank + 1;
    }
    return total;
  }
}
