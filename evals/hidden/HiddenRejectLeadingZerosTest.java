package example.durations;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

/** Hidden eval tests for task reject_leading_zeros. Copied in and run by evals/run_evals.py only. */
class HiddenRejectLeadingZerosTest {

  @ParameterizedTest
  @CsvSource({"'0s', 0", "'10m', 600", "'1h0m', 3600", "'100s', 100"})
  void parsesValid(String text, long expected) {
    assertEquals(expected, Durations.parse(text));
  }

  @ParameterizedTest
  @ValueSource(strings = {"01h", "00s", "1h05m", "007s"})
  void rejectsInvalid(String text) {
    assertThrows(DurationException.class, () -> Durations.parse(text));
  }
}
