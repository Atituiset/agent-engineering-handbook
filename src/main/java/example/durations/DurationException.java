package example.durations;

/** Thrown when a duration string is malformed. */
public final class DurationException extends IllegalArgumentException {
  private static final long serialVersionUID = 1L;

  public DurationException(String message) {
    super(message);
  }

  public DurationException(String message, Throwable cause) {
    super(message, cause);
  }
}
