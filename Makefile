all: setup.py board_env_wrap.cxx src/board_env.cpp
	python setup.py build_ext --build-lib target

wrapper: src/board_env.h board_env.i
	swig -c++ -python -outdir target board_env.i
