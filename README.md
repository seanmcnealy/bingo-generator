# Python BINGO generator

## Requirements

> LaTeX
> make
> python3

## How to generate BINGO pages

> make -d num_bingo=3


## How is it built?


1. new_numbers.py
  Updates file 'numbers.tex' with new numbers
2. main.tex
  Reads 'numbers.tex' and parses numbers into table
