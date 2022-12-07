all:
	@for i in {1..$(num_bingo)}; do \
		python3 bingo.py; \
		pdflatex -jobname bingo$$i main.tex; \
		sleep 1; \
	done

clean:
	rm -f *.log *.aux *.out *.fls *.fdb_latexmk *.synctex.gz

.PHONY: all clean
