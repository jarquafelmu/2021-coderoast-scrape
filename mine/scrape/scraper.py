"""The results of a scrape."""
from dataclasses import dataclass


@dataclass
class ScrapeResult:
    """The results of a scrape."""
    doi: str
    wordscore: int
    frequency: list[tuple[str, int]]
    study_design: list[tuple[str, int]]
