#!/usr/bin/env python3

import os
import sys

"""
Warning! This program will operate on the given folder an only so it won't work
RECURSIVELY!
"""

# Folder to process files in
folder_path = ""
# Will replace "&"s in files names
ampersand_replacer = "_and_"
ampersand_snake_case = "_&_"
# Character used to replace a space
space_delimiter = "_"

# Characters to remove in the file name
# Exclude '.' because file extensions and '-' because we keep it
# Also exclude '&' because it's REPLACED.
utf_eight_characters = ["!", '"', "#", "$", "%", "'", "(", ")", "*", "+", ",", "/",
":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "`", "{", "|", "}", "~"
]

special_characters = ["°", "ù"]
excluded_characters = []
# ALSO ADD UTF8 AND THE 2 LAST CHARACTERS IN A SEPARATE LIST?


# Merge UTF8 and special characters in a list of characters to exclude
def build_character_list_to_exclude():
    for character in utf_eight_characters:
        excluded_characters.append(character)

    for character in special_characters:
        excluded_characters.append(character)


def convert_all_files_to_snake_case():
    new_file_name = ""

    old_file_path = ""
    new_file_path = ""

    for file in os.listdir(folder_path):
        old_file_path = folder_path + "/" + file

        new_file_name = file
        new_file_name = new_file_name.lower()
        # Replace spaces with the space delimiter
        new_file_name = new_file_name.replace(" ", space_delimiter)

        # Replace "_&_" by "_and_" because dj&dj and dj_&_dj
        if ampersand_snake_case in new_file_name:
            new_file_name = new_file_name.replace(ampersand_snake_case, ampersand_replacer)

        # Replace "&" by "and" as explained above
        if "&" in new_file_name:
            new_file_name = new_file_name.replace("&", ampersand_replacer)

        # Replace " - " by "_-_"
        if " - " in new_file_name:
            new_file_name = new_file_name.replace(" - ", "")


        # Delete special characters. This operation must be done last.
        for character in excluded_characters:
            if character in new_file_name:
                new_file_name = new_file_name.replace(character, "")

        # Eliminate multiple underscores until no one is left
        # space_delimiter replaced spaces already
        while "__" in new_file_name:
            new_file_name = new_file_name.replace("__", "_")

        new_file_path = folder_path + "/" + new_file_name

        os.rename(old_file_path, new_file_path)


def main():
    global folder_path

    print("This program will convert all the files")
    print("in the given directory to snake_case.\n")

    build_character_list_to_exclude()

    # LEAVE BLANK FOR FOLDER WHERE SCRIPT IS!
    folder_path = input("Enter the folder path to cycle through: ")
    print("\n")

    convert_all_files_to_snake_case()

    input("Press the enter key to exit...")
    sys.exit()


main()
