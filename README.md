# Python BINGO generator

Bingo generator using Python and LaTeX, will will generate X amount of PDF's with randomized numbers that can be printed out.  


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

### Rules

Will generate columns containing random unique values, see integer ranges in table below.  

| B      | I       | N       | G       | O       |
|--------|---------|---------|---------|---------|
| (1-15) | (15-30) | (30-45) | (45-60) | (60-75) |
| (1-15) | (15-30) | (30-45) | (45-60) | (60-75) |
| (1-15) | (15-30) | (30-45) | (45-60) | (60-75) |
| (1-15) | (15-30) | (30-45) | (45-60) | (60-75) |
| (1-15) | (15-30) | (30-45) | (45-60) | (60-75) |

## Results

See: [demo-bingo.pdf](deom-bingo.pdf)
