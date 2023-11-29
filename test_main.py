import os
import main

import pytest


"""
Uses predefined test data
Calls out function and saves return value
Calls test function and saves return value
Compares the values so they are the same
"""
def test_search_in_file():
    original_dir = os.getcwd()
    os.chdir('TestData')
    file_path = 'Makaroner.txt'
    keyword = "Vatten"

    found_keyword = main.search_in_file(file_path, keyword)

    def search():
        with open(file_path, 'r', encoding='utf-8') as text:
            content = text.readlines()
            for word in content:
                if word == keyword:
                    return True
            return False

    found_word = search()

    os.chdir(original_dir)

    assert (found_keyword == found_word)


"""
Uses predefined test data
Calls our function and saves return list in a variable
Checks the length of the list
Compares the length of the list that equals how many times the keyword was found in files.
Compares it with hardcoded data
"""
def test_search_in_folder():
    original_dir = os.getcwd()
    os.chdir('TestData')
    current_path = os.getcwd()
    keyword = "Vatten"
    keyword2 = "Koffein"

    files_that_contain_water = 4
    files_that_contain_caffeine = 2

    water = main.search_in_folder(current_path, keyword)
    caffeine = main.search_in_folder(current_path, keyword2)

    files_containing_water = len(water)
    files_containing_caffeine = len(caffeine)

    assert (files_that_contain_water == files_containing_water)
    assert (files_that_contain_caffeine == files_containing_caffeine)

    os.chdir(original_dir)
