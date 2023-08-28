import os
import sys
import logging
from collections import namedtuple

LOG_FILE = "log.txt"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
DirectoryItem = namedtuple("DirectoryItem",
                           ["name", "extension", "is_directory",
                            "parent_directory"])


def get_directory_info(path):
    try:
        items = os.listdir(path)
        for item in items:
            item_path = os.path.join(path, item)
            parent_directory = os.path.basename(path)
            is_directory = os.path.isdir(item_path)
            if is_directory:
                logging.info(
                    f"{item} | Directory | Parent Directory: {parent_directory}")
                directory_item = DirectoryItem(item, None, True,
                                               parent_directory)
                get_directory_info(item_path)
            else:
                file_name = os.path.splitext(item)[0]
                extension = os.path.splitext(item)[1]
                logging.info(
                    f"{file_name} | File | Extension: {extension} | Parent Directory: {parent_directory}")
                file_item = DirectoryItem(file_name, extension, False,
                                          parent_directory)

    except FileNotFoundError:
        logging.error(f"Directory not found: {path}")

        print(f"Directory not found: {path}")

    except Exception as e:
        logging.error(str(e))

        print("An error occurred while processing the directory.")


if len(sys.argv) < 2:
    print("Please provide a directory path as an argument.")
else:
    directory_path = sys.argv[1]
    get_directory_info(directory_path)
