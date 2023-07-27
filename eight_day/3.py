import logging
import os

class RotatingFileHandler(logging.Handler):
    def __init__(self, filename, max_lines=1000):
        super().__init__()
        self.filename = filename
        self.max_lines = max_lines
        self.line_count = 0
        self.file_count = 0
        self.file_handler = None
        self.rotate_file()

    def rotate_file(self):
        if self.file_handler:
            self.file_handler.close()
        self.file_handler = open(f"{self.filename}{self.file_count}.log", "a")
        self.file_count += 1
        self.line_count = 0

    def emit(self, record):
        msg = self.format(record)
        self.file_handler.write(msg + '\n')
        self.line_count += 1
        if self.line_count >= self.max_lines:
            self.rotate_file()

    def close(self):
        if self.file_handler:
            self.file_handler.close()
        super().close()

def setup_logger(filename):
    logger = logging.getLogger("rotating_logger")
    logger.setLevel(logging.INFO)

    # Create a rotating file handler to write logs to the log file
    file_handler = RotatingFileHandler(filename, max_lines=1000)
    file_handler.setLevel(logging.INFO)

    # Create a formatter to specify the log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the rotating file handler to the logger
    logger.addHandler(file_handler)

    return logger

if __name__ == "__main__":
    log_filename = "log"
    logger = setup_logger(log_filename)

    for i in range(2000):
        logger.info(f"This is log message {i}")

    logger.info("Logs have been written successfully.")
