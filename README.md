# Python Tools

## Installation

Add the `python-tools` directory to your `$PYTHONPATH`. 

To add a directory to your `$PYTHONPATH`, `cd` into the directory and type <code>echo -e "\nexport PYTHONPATH=\`pwd\`:\$PYTHONPATH" >> ~/.bashrc</code>. Replace `~/.bashrc` with the location of your shell config file.

## Dependencies

* To use the statistics utilities, install [R](http://www.r-project.org/) and [rpy2](http://rpy.sourceforge.net/rpy2.html).

## Includes

- Simon Willison's [optfunc](https://github.com/simonw/optfunc)
- [StoppableThread](http://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python)
- [asyncproc](http://www.lysator.liu.se/~bellman/download/)
