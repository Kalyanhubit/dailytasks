# ---------variables-----------
#
# Variables are containers for storing data values.
#
# --------CreatingVariables-----------
# Python has no command for declaring a variable.A variable is created the moment you first assign a value to it.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
#
# x=50;
# x="newproject"
# x=101.1
# ---------Get the Type---------------
# by using type()
# x=50;
# print(type(x))
# output:<class int>

# ----------------variable names-----------------
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and
# underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different
# variables
#
# ----------multi_word variable----------
# camel case,pascal case,snake case
# x=y=z="vn2solutions"
# print(x)
# output:vn2solutions
# -----------unpacking a variable-------------
# fruits=["apple","bannana","orange"]
# x,y,z=fruits
# print(x)
# output:apple

#
# -----------TYPES OF VARIABLES-----------------
# 1.GLOBAL VARIABLES:
# variables that are created outside the function and can be used both inside and outside the function.
#     it can be accessed through out th function.
# it is declared with a keyword:
#     global()
#
# def myfunc():
#     x="lamborgini"
#     global (X)
#     print("the most loved car in north america is :",x)
# myfunc()
# print("i love to ride",x)


# 2.local variables:
# variables that ara declared inside the function and cannot be accessed out side the function ar eknown as local variables
#
# def func()
#    x=200;
#    print("the price of classmatae note book 400pg",x)
# func()
# print(x):::output: error variable x is not declared
