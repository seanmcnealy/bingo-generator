# Python BINGO generator

## Requirements

1. [LaTeX Full](https://www.latex-project.org/get/)
2. [Python3](https://realpython.com/installing-python/)

## How to generate BINGO pages

```
git clone https://github.com/Swepz/bingo.git
cd bingo
make -d num_bingo=3
```
num_bingo=N, where integer N => 1

Depending on make version, 'make -d' might not work, instead use 'make -D'



## How is it built?


1. `new_numbers.py`:
  Updates file 'numbers.tex' with new numbers
2. `main.tex`:
  Reads 'numbers.tex' and parses numbers into table
3. `Makefile`: Loops `num_bingo` times and runs `new_numbers.py` to update new numbers and uses `pdflatex`on `main.tex`to create new pdfs.

## Results

<embed src="demo-bingo.pdf" type="application/pdf">
