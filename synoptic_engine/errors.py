"""Custom exceptions for the pathology synoptic engine."""


class SynopticConfigurationError(ValueError):
    """Raised when a synoptic definition or generated row is malformed."""


__all__ = ["SynopticConfigurationError"]
