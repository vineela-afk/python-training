import logging

def setup_logger():
    logger = logging.getLogger("word_logger")
    logger.setLevel(logging.INFO)

    # Create a file handler to write logs to a file named "log.txt"
    file_handler = logging.FileHandler("log.txt")
    file_handler.setLevel(logging.INFO)

    # Create another file handler for CRITICAL logs to log words less than 4 characters
    critical_handler = logging.FileHandler("log.txt")
    critical_handler.setLevel(logging.CRITICAL)

    # Create a formatter to specify the log format
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    critical_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(critical_handler)

    return logger

def display_words(file_name):
    logger = setup_logger()

    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    if len(word) < 4:
                        logger.critical(word)
                    else:
                        logger.info(word)

    except FileNotFoundError:
        logger.error("Error: File not found")

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    display_words(file_name)
