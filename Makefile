##
## EPITECH PROJECT, 2020
## Gomoku
## File description:
## Makefile
##

SRC	=	./src

ifdef OS
   CM = pyinstaller.exe $(SRC)/pbrain-gomoku-ai.py --name pbrain-gomoku-ai.exe --onefile && cp ./dist/pbrain-gomoku-ai.exe pbrain-gomoku-ai.exe
else
   ifeq ($(shell uname), Linux)
      CM = cp $(SRC)/pbrain-gomoku-ai.py pbrain-gomoku-ai
   endif
endif

all:
	$(CM)

clean: fclean

fclean:	
	rm pbrain-gomoku-ai*

re:	fclean all

.PHONY: all clean fclean re