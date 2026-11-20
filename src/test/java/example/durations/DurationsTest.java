package example.durations;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

class DurationsTest {

  @ParameterizedTest
  @CsvSource({"0s, 0", "90s, 90", "1m, 60", "1h30m, 5400", "2h5s, 7205", "1h1m1s, 3661"})
  void parsesValidDurations(String text, long expected) {
    assertEquals(expected, Durations.parse(text));
  }

  @ParameterizedTest
  @ValueSource(
      strings = {"", "h", "10", "1x", "1m1h", "1h1h", " 1h", "1h ", "99999999999999999999s"})
  void rejectsInvalidDurations(String text) {
    assertThrows(DurationException.class, () -> Durations.parse(text));
  }
}
