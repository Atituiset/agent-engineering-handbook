package example.durations;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

/** Hidden eval tests for task allow_spaces. Copied in and run by evals/run_evals.py only. */
class HiddenAllowSpacesTest {

  @ParameterizedTest
  @CsvSource({"'1h 30m', 5400", "'1h  30m', 5400", "'2h 5s', 7205", "'1h 1m 1s', 3661", "'90s', 90"})
  void parsesValid(String text, long expected) {
    assertEquals(expected, Durations.parse(text));
  }

  @ParameterizedTest
  @ValueSource(strings = {" 1h", "1h ", "1h\t30m", "1h 1h", "30m 1h", "1 h", " "})
  void rejectsInvalid(String text) {
    assertThrows(DurationException.class, () -> Durations.parse(text));
  }
}
