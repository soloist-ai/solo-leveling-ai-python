import logging
import time
from collections import defaultdict
from typing import DefaultDict


class HealthCheckRateLimitFilter(logging.Filter):
    def __init__(self, period_seconds: int = 60, show_suppressed: bool = True):
        super().__init__()
        self.period_seconds = period_seconds
        self.show_suppressed = show_suppressed
        self.last_log_time: DefaultDict[str, float] = defaultdict(float)
        self.suppressed_count: DefaultDict[str, int] = defaultdict(int)

    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        if "/health" not in message:
            return True
        current_time = time.time()
        path_key = "/health"
        if current_time - self.last_log_time[path_key] >= self.period_seconds:
            if self.show_suppressed and self.suppressed_count[path_key] > 0:
                record.msg = f"{record.msg} (suppressed {self.suppressed_count[path_key]} similar logs)"
                self.suppressed_count[path_key] = 0

            self.last_log_time[path_key] = current_time
            return True

        self.suppressed_count[path_key] += 1
        return False
