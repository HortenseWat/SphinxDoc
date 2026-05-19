Create a documentation
======================

Set up a Python virtual environment
___________________________________

After downloading Python, it is important to set up a virtual environment to use it. This means that any Python modifications we will do in out project won't impact the global Python software but will only be effective in our project. 

.. code-block:: python
      
   python -m venv .venv 

.. warning::
   
   If an error occurs, it may be because your computer doesn't allow to run scripts (feature initially used to block viruses). You can disable it with the following command :

   .. code-block:: python
   
      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

You then need to activate the venv (Virtual Environment) :

.. code-block:: python
  
   .venv\Scripts\activate 

.. hint:: 
   
   You can check if the Virtual Environment has been correctly set if (.venv) is displayed at the beginning of the command line.

 
Download Sphinx
_______________

.. code-block:: python
      
   python -m pip install sphinx


.. hint::

   Verify with :
   
   .. code-block:: python
   
      where sphinx-build OR sphinx-build -version


Create basic breadcrumbs
________________________

**sphinx-quickstart** is an interactive tool that asks some questions about your project and then generates a complete documentation directory and sample Makefile to be used with sphinx-build. 

.. code-block:: python
        
   sphinx-quickstart docs

This will present to you a series of questions required to create the basic
directory and configuration layout for your project inside the ``docs`` folder.
To proceed, answer each question as follows:

- ``> Separate source and build directories (y/n) [n]``: Write "``y``" (without
  quotes) and press :kbd:`Enter`.
- ``> Project name``: Write "``YOUR-PROJECT-NAME``" (without quotes) and press
  :kbd:`Enter`.
- ``> Author name(s)``: Write "``YOUR-NAME``" (without quotes) and press
  :kbd:`Enter`.
- ``> Project release []``: Write "``0.1``" (without quotes) and press
  :kbd:`Enter`.
- ``> Project language [en]``: Leave it empty (the default, English) and press
  :kbd:`Enter`.

.. warning:

   Byh default, sphinx adds "documentation" to your project title. don't call your project ``YOUR-PROJECT_DOCUMENTATION`` or it will be displayed twice.
   

After the last question, you will see the new ``docs`` directory with the
following content.

.. code-block:: text

   docs
   ├── build
   ├── make.bat
   ├── Makefile
    └── source
      ├── conf.py
      ├── index.rst
      ├── _static
      └── _templates

The purpose of each of these files is:

- ``build/``
  An empty directory (for now) that will hold the rendered documentation.

- ``make.bat`` and ``Makefile``
  Convenience scripts to simplify some common Sphinx operations, such as
  rendering the content.

- ``source/conf.py``
  A Python script holding the configuration of the Sphinx project.  It contains
  the project name and release you specified to ``sphinx-quickstart``, as well
  as some extra configuration keys.

- ``source/index.rst``
  The `root document` of the project, which serves as welcome page and
  contains the root of the "table of contents tree" (or *toctree*).


Second Commit
_____________

My second commit follow the steps of : 

- `Download Sphinx`_

- `Set up a Python virtual environment`_

- `Create basic breadcrumbs`_

