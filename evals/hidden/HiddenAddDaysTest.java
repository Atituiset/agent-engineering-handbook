package example.durations;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

/** Hidden eval tests for task add_days. Copied in and run by evals/run_evals.py only. */
class HiddenAddDaysTest {

  @ParameterizedTest
  @CsvSource({"'1d', 86400", "'1d2h', 93600", "'2d30m5s', 174605", "'0d', 0", "'1h30m', 5400"})
  void parsesValid(String text, long expected) {
    assertEquals(expected, Durations.parse(text));
  }

  @ParameterizedTest
  @ValueSource(strings = {"1h1d", "1d1d", "1s1d", "d", "1D"})
  void rejectsInvalid(String text) {
    assertThrows(DurationException.class, () -> Durations.parse(text));
  }
}
