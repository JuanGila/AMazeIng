


LIB_NAME		:= push_swap.a
LIB_NAME_EXE	:= push_swap
LIB_SRCS_DIRS	:= . bench core errors helpers parser stack strategy utils
LIB_SRCS_FILES	:= $(foreach dir,$(LIB_SRCS_DIRS),$(wildcard $(dir)/*.c))
LIB_OBJS_DIR	:= build
LIB_OBJS_FILES	:= $(addprefix $(LIB_OBJS_DIR)/,$(LIB_SRCS_FILES:.c=.o))

## COMANDOS
CMD_PYTHON			:= python3 -m
PYTHON_PIP			:= $(CMD_PYTHON) pip
CMD_MYPY			:= mypy .
CMD_MYPY_FLAGS		:= --strict
CMD_FLAKE8			:= flake8 .
FLAKE8_FLAGS		:= --ignore=
CMD_EXEC			:= -exec
CMD_RM_FLAGS		:= rm -rf
CMD_FIND			:= find .
CMD_FIND_FLAGS		:= -type d -name
# DIRECTORIES
MAZE_MAIN_DIR 		:= a_maze_ing.py
MAZE_TEST_DIR		:= ./tests
MAZE_CONFIG_DIR		:= ./config/config.txt
DEPENDENCIES_DIR	:= ./dependencies/requirements.txt


.PHONY: all install run debug package test lint lint-strict clean

all: lint test

install:
	$(PYTHON_PIP) install -r $(DEPENDENCIES_DIR)

run:
	$(CMD_PYTHON) $(MAIN) $(CONFIG)

debug:
	$(CMD_PYTHON) pdb $(MAIN) $(CONFIG)

package:
	$(CMD_PYTHON) build

test:
	$(CMD_PYTHON) pytest $(TEST_DIR)

lint:
	$(CMD_FLAKE8)
	$(CMD_MYPY) --warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs

lint-strict:
	$(CMD_MYPY) $(CMD_MYPY_FLAGS)
	$(CMD_FLAKE8) $(FLAKE8_FLAGS)

clean:
	$(CMD_RM_FLAGS) dist/
	$(CMD_RM_FLAGS) build/
	$(CMD_FIND) $(CMD_FIND_FLAGS) "*.egg-info" $(CMD_EXEC) $(CMD_RM_FLAGS) {} +
	$(CMD_FIND) $(CMD_FIND_FLAGS) "__pycache__" $(CMD_EXEC) $(CMD_RM_FLAGS) {} +
	$(CMD_FIND) $(CMD_FIND_FLAGS) ".mypy_cache" $(CMD_EXEC) $(CMD_RM_FLAGS) {} +
	$(CMD_FIND) $(CMD_FIND_FLAGS) ".pytest_cache" $(CMD_EXEC) $(CMD_RM_FLAGS) {} +


Un pequeño cambio respecto a mi propuesta anterior

Hay algo que prefiero corregir ahora: no pondría all: lint test como objetivo principal sin más.

Para un proyecto educativo como este, prefiero que make sea predecible y que cada acción importante tenga su target explícito.
Podemos dejar all como una comprobación completa, pero no hacer que cualquier make genere o modifique cosas inesperadamente.

La base anterior nos sirve, pero la estructura definitiva la haría alrededor de Python packaging + MazeGenerator reutilizable, que es una de las partes centrales del enunciado.