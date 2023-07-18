import os
import shutil

# Path to the unit tests file
tests_file_path = "/home/project/xzceb-flask_eng_fr/final_project/machinetranslation/tests.py"

# Destination path for the tests folder
tests_folder_path = "/home/project/xzceb-flask_eng_fr/final_project/machinetranslation/tests"

# Copy the unit tests into the tests folder
shutil.copy(tests_file_path, tests_folder_path)