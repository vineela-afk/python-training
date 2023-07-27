import os
import json
import logging

def setup_logger():
    logger = logging.getLogger("file_logger")
    logger.setLevel(logging.INFO)

    # Create a file handler to write logs to a file named "log.txt"
    file_handler = logging.FileHandler("log.txt")
    file_handler.setLevel(logging.INFO)

    # Create another file handler for CRITICAL logs
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

def check_files_in_folders(json_file_path, base_folder_path):
    logger = setup_logger()

    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        for folder_name, files_list in data.items():
            folder_path = os.path.join(base_folder_path, folder_name)
            
            logger.info(f"Checking files in folder: {folder_path}")

            for file_name in files_list:
                file_path = os.path.join(folder_path, file_name)
                if os.path.exists(file_path):
                    logger.info(f"File found: {file_path}")
                else:
                    logger.critical(f"File not found: {file_path}")

    except FileNotFoundError:
        logger.error("Error: JSON file not found")

if __name__ == "__main__":
    json_file_path = "files.json"  # Provide the path to your JSON file here
    base_folder_path = "/home/techno-530/Downloads/python-training"  # Provide the path to your predefined folder here
    check_files_in_folders(json_file_path, base_folder_path)
