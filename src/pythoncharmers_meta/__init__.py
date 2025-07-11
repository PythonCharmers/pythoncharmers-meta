"""
Python Charmers meta-package.

This package is for use in Python Charmers training courses.

You can load the IPython extension like so:

    %load_ext pythoncharmers_meta

assuming the pythoncharmers_meta packages has been installed system-wide.

This package depends on packages used in Python Charmers training courses. It
also provides an IPython extension that enables three new magic commands:

- %nb
- %ai

The %nb magic is for grabbing a few code or markdown cells (respectively) from
a notebook on the filesystem. It defaults to the most recently modified
notebook in the latest ~/Trainer_XYZ folder.

The %ai magic invokes the `llm` package for quick use of an LLM like gpt-4o-mini.

For help on the magics, add a trailing question mark. For example:

    %nb?

Two additional magics are available for getting and setting the current
path and/or file that %nb queries. To get help on these, run:

    %nbfile?
    %nbpath?

"""

from .nb_magic import NotebookMagic
try:
    from .ai_magic import AIMagic
except Exception as e:
    print(e)


def load_ipython_extension(ipython):
    """
    Any module file that defines a function named `load_ipython_extension`
    can be loaded via `%load_ext module.path` or be configured to be
    autoloaded by IPython at startup time.
    """
    # You can register the class itself without instantiating it.  IPython will
    # call the default constructor on it.
    ipython.register_magics(NotebookMagic)

    try:
        ipython.register_magics(AIMagic)
    except Exception as e:
        print(e)


