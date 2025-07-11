import os
import threading
from datetime import datetime
from enum import Enum

class LogLevel(Enum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40

class Logger:
    def __init__(self, log_file="log.txt", enable_console_output=True, level=LogLevel.INFO):
        self.log_file = log_file
        self.enable_console_output = enable_console_output
        self.level = level
        self.lock = threading.Lock()

    def _get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _write(self, message):
        with self.lock:
            with open(self.log_file, "a") as f:
                f.write(message + "\n")
        if self.enable_console_output:
            print(message)

    def log(self, message, level="INFO"):
        level_enum = LogLevel[level.upper()]
        if level_enum.value < self.level.value:
            return
        timestamp = self._get_timestamp()
        formatted_message = f"[{timestamp}] [{level.upper()}] {message}"
        self._write(formatted_message)

    def info(self, message): self.log(message, "INFO")
    def warning(self, message): self.log(message, "WARNING")
    def error(self, message): self.log(message, "ERROR")
    def debug(self, message): self.log(message, "DEBUG")
    def clear_log(self): open(self.log_file, 'w').close()


class Logger:
    def __init__(self, log_file="log.txt", enable_console_output=True):
        self.log_file = log_file
        self.enable_console_output = enable_console_output
        self.lock = threading.Lock()

    def _get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _write(self, message):
        with self.lock:
            with open(self.log_file, "a") as f:
                f.write(message + "\n")
        if self.enable_console_output:
            print(message)

    def log(self, message, level="INFO"):
        timestamp = self._get_timestamp()
        formatted_message = f"[{timestamp}] [{level.upper()}] {message}"
        self._write(formatted_message)

    def info(self, message):
        self.log(message, "INFO")

    def warning(self, message):
        self.log(message, "WARNING")

    def error(self, message):
        self.log(message, "ERROR")

    def debug(self, message):
        self.log(message, "DEBUG")

    def clear_log(self):
        """Clears the log file."""
        with self.lock:
            open(self.log_file, 'w').close()

# Example usage:
if __name__ == "__main__":
    logger = Logger()
    logger.info("Application started")
    logger.debug("Debugging mode on")
    logger.warning("This is a warning")
    logger.error("An error occurred")
