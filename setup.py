from setuptools import setup, Extension 
#name of module 
name  = "board_env"
  
#version of module 
version = "1.0"
  
# specify the name of the extension and source files 
# required to compile this 
ext_modules = Extension(name='_board_env',sources=["board_env_wrap.cxx","./src/board_env.cpp"],extra_compile_args=['-std=c++11']) 
  
setup(name=name, 
      version=version, 
      ext_modules=[ext_modules]) 
