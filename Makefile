CMD_PYTHON			:= python3 -m
PYTHON_PIP			:= $(CMD_PYTHON) pip
CMD_MYPY			:= mypy .
MYPY_FLAGS			:= --strict
CMD_FLAKE8			:= flake8 .
FLAKE8_FLAGS		:= --ignore=
CMD_EXEC			:= -exec
CMD_RM_FLAGS		:= rm -rf
CMD_FIND			:= find .
FIND_FLAGS			:= -type d -name
MAIN_DIR			:= ./
MAZE_MAIN_DIR 		:= a_maze_ing.py
MAZE_TEST_DIR		:= $(MAIN_DIR)tests
MAZE_CONFIG_DIR		:= $(MAIN_DIR)config
MAZE_CONFIG_FILE	?= $(MAZE_CONFIG_DIR)/config.txt# con ?= se pueden hacer cosas sin modificar el Makefile como -> make run CONFIG=examples/config_big.txt
DEPENDENCIES_DIR	:= $(MAIN_DIR)dependencies
DEPENDENCIES_PIP	:= $(DEPENDENCIES_DIR)/requirements.txt
VENV_DIR 			:= .venv
VENV_PIP_DIR 		:= $(VENV_DIR)/bin/pip
VENV_PYTHON_DIR 	:= $(VENV_DIR)/bin/python
VENV_STAMP_DIR 		:= $(VENV_DIR)/.requirements-installed
# La solución que usaría es un stamp file basado en el hash del requirements.txt. Así:
#	primera ejecución → crea .venv e instala;
#	siguientes ejecuciones → no instala nada;
#	si cambia requirements.txt → vuelve a instalar;
#	si borras .venv → la vuelve a crear;
#	make install sigue siendo seguro de ejecutar tantas veces como quieras.
.PHONY: all install run debug build clean fclean re lint lint-strict test

$(VENV_DIR):
	$(PYTHON) venv $(VENV_DIR)

$(VENV_STAMP_DIR): $(VENV_DIR) $(DEPENDENCIES_PIP)
	$(VENV_PIP_DIR) install --upgrade pip
	$(VENV_PIP_DIR) install -r $(DEPENDENCIES_PIP)
	@touch $@

install: $(VENV_STAMP_DIR)
	@echo "Environment ready."

all: lint test

run: install# ejecuta -> .venv/bin/python a_maze_ing.py config.txt 
	$(VENV_PYTHON_DIR) $(MAZE_MAIN_DIR) $(MAZE_CONFIG_DIR)

debug: install
	$(CMD_PYTHON) pdb $(MAZE_MAIN_DIR) $(MAZE_CONFIG_DIR)

build: install
	$(CMD_PYTHON) build

clean:
# Dentro de un Makefile necesitas $$ para que $ llegue al shell porque $(...) sin escapar lo intenta interpretar make, no Bash.
	@echo "Cleaning ..."
	@if [ -d "dist" ]; then \
		echo "Removing -> $(CMD_RM_FLAGS) dist/ ..."; \
		$(CMD_RM_FLAGS) dist/; \
	fi
	@if [ -d "build" ]; then \
		echo "Removing -> $(CMD_RM_FLAGS) build/ ..."; \
		$(CMD_RM_FLAGS) build/; \
	fi
	@if [ -n "$$($(CMD_FIND) $(FIND_FLAGS) '*.egg-info' -print -quit 2>/dev/null)" ]; then \
		echo "Removing -> $(CMD_FIND) $(FIND_FLAGS) *.egg-info $(CMD_EXEC) $(CMD_RM_FLAGS) {} +; \
		$(CMD_FIND) $(FIND_FLAGS) "*.egg-info" $(CMD_EXEC) $(CMD_RM_FLAGS) {} +; \
	fi
	@if [ -n "$$($(CMD_FIND) $(FIND_FLAGS) '__pycache__' -print -quit 2>/dev/null)" ]; then \
		echo "Removing -> __pycache__ ..."; \
		$(CMD_FIND) $(FIND_FLAGS) "__pycache__" $(CMD_EXEC) $(CMD_RM_FLAGS) {} +; \
	fi
	@if [ -n "$$($(CMD_FIND) $(FIND_FLAGS) '.mypy_cache' -print -quit 2>/dev/null)" ]; then \
		echo "Removing -> .mypy_cache ..."; \
		$(CMD_FIND) $(FIND_FLAGS) ".mypy_cache" $(CMD_EXEC) $(CMD_RM_FLAGS) {} +; \
	fi
	@if [ -n "$$($(CMD_FIND) $(FIND_FLAGS) '.pytest_cache' -print -quit 2>/dev/null)" ]; then \
		echo "Removing -> .pytest_cache ..."; \
		$(CMD_FIND) $(FIND_FLAGS) ".pytest_cache" $(CMD_EXEC) $(CMD_RM_FLAGS) {} +; \
	fi
	@echo ""

fclean: clean
	@echo "Full Cleaning ..."
	@if [ -d $(VENV_DIR) ]; then \
		echo "Removing -> $(CMD_RM_FLAGS) $(CMD_RM_FLAGS) $(VENV_DIR) ..."; \
		$(CMD_RM_FLAGS) $(VENV_DIR); \
	fi

re: clean all

lint: install
	$(CMD_FLAKE8)
	$(CMD_MYPY) --warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs

lint-strict: install
	$(CMD_MYPY) $(MYPY_FLAGS)
	$(CMD_FLAKE8) $(FLAKE8_FLAGS)

test: install
	$(CMD_PYTHON) pytest $(TEST_DIR)

Un pequeño cambio respecto a mi propuesta anterior

Hay algo que prefiero corregir ahora: no pondría all: lint test como objetivo principal sin más.

Para un proyecto educativo como este, prefiero que make sea predecible y que cada acción importante tenga su target explícito.
Podemos dejar all como una comprobación completa, pero no hacer que cualquier make genere o modifique cosas inesperadamente.

La base anterior nos sirve, pero la estructura definitiva la haría alrededor de Python packaging + MazeGenerator reutilizable, que es una de las partes centrales del enunciado.