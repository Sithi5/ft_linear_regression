import os

RESOURCES_DIR_PATH: str = os.path.abspath(os.path.join(__file__, "..", "..", "resources"))
DEFAULT_CSV_FILE_PATH: str = os.path.join(RESOURCES_DIR_PATH, "data.csv")
SAVE_FILE_NAME: str = os.path.join(RESOURCES_DIR_PATH, "save_info.txt")
