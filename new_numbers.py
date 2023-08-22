#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import sample
import fileinput
import re

# Define the name of the file to be read
TEX_FILENAME = 'template.tex'

# Open a file and read its contents
with open(TEX_FILENAME) as f:
    contents = f.read()


# Define the ranges of numbers for each column in bingo grid
col1_range = range(1, 16)
col2_range = range(16, 31)
col3_range = range(31, 46)
col4_range = range(46, 61)
col5_range = range(61, 76)

# # create the columns with specific ranges of numbers
column1 = ', '.join(str(i) for i in sample(col1_range, 5)) + ', ' + ', '.join(str(i) for i in sample(col1_range, 5)) + ','
column2 = ', '.join(str(i) for i in sample(col2_range, 5)) + ', ' + ', '.join(str(i) for i in sample(col2_range, 5)) + ','
column3 = ', '.join(str(i) for i in sample(col3_range, 5)) + ', ' + ', '.join(str(i) for i in sample(col3_range, 5)) + ','
column4 = ', '.join(str(i) for i in sample(col4_range, 5)) + ', ' + ', '.join(str(i) for i in sample(col4_range, 5)) + ','
column5 = ', '.join(str(i) for i in sample(col5_range, 5)) + ', ' + ', '.join(str(i) for i in sample(col5_range, 5)) + ','

# combine the columns into a 5x5 grid
bingo_grid = '\n'.join([column1, column2, column3, column4, column5])

# Transpose the columns in the bingo_grid string
transposed = ""
for i in range(10):
    transposed += "{" + ",".join(row.split(",")[i] for row in bingo_grid.split('\n')) + "},\n"

# Replace the whitespace characters with empty strings
transposed = transposed.replace(" ", "")

# Create a list of replacement strings to simplify re.sub() method
replacements = []
for row in transposed.split('\n'):
    replacements.append(row)

# Find lines that start with a left curly bracket, end with a right curly bracket and a comma
pattern = r"^[^{]*\{[^}]*\},$"

# Find all matches in the contents of the file
matches = re.findall(pattern, contents, re.MULTILINE)


# Print 'contents' before the replacements
print(f"Bingo numbers before replacements:\n {contents}")

# Iterate over the matches and use the re.sub() method to replace each match
# with a different replacement string
for match, replacement in zip(matches, replacements):
    contents = re.sub(match, replacement, contents, flags=re.MULTILINE)

# Print 'contents' after the replacements
print(f"Bingo numbers after replacements:\n {contents}")
# Open the file in write mode and write the updated contents to the file
with open("numbers.tex", "w") as f:
    f.write(contents)
