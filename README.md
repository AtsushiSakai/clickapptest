# clickapptest
A click based cli app test

# How to install

>$ pip install git+https://github.com/AtsushiSakai/clickapptest.git

# Examples

>$ clickapptest
Usage: clickapptest [OPTIONS] COMMAND [ARGS]...

  This is a sample click test

Options:
  --help  Show this message and exit.

Commands:
  run-test1  run test1
  run-test2  This is a command line tool for run test2

>$ clickapptest run-test1 takashi
this is common
run test1 for takashi!!!
 
>$ clickapptest run-test2 -n 4
run test2!!!run test2!!!run test2!!!run test2!!!

# Bash Completion

add this in your .bashrc

> eval "$(_CLICKAPPTEST_COMPLETE=bash_source clickapptest)"
