%module board_env

%{
#include "src/board_env.h"
%}

%include "std_vector.i"
%include "std_string.i"

namespace std {
   %template(IntVector) vector<int>;
   %template(DoubleVector) vector<double>;
   %template(StringVector) vector<string>;
}

%include src/board_env.h
