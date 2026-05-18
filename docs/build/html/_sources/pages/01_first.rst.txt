Create a project
================

Download Git and Python
_______________________


To start with this part, make sure you have downloaded Git and Python. 

You can find both these softwares to download using the following links : 

- Git download : https://git-scm.com/install/

.. note::

    When downloading Python, make sure you check the option :red:`"Add PATH"`. This allows your code to be compiled with any kind of operating system.

- Python download : https://www.python.org/downloads/


.. note::

   If you couldn't complete this last step succesfully or if Python was already installed on your device, please check the following website to help you set up this feature : https://realpython.com/add-python-to-path/



After downloading these two softwares, you can check the success of the operation by closing the terminal, and after opening it again, typing these commands that will show you the current version installed : 

.. hint::
   .. code-block:: python
       
      python --version or python -V 
      git --version 


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


Start a Documentation
=====================

Create and import a repository
______________________________

Go to your Github online account and create a new repository (project). 
You will find a link on that same page that represents your project. 
After copiying it, you can import it as a local project in your computer by using : 

.. code-block:: python
  
   git clone git clone git@github.com:YOUR-USERNAME/YOUR-REPOSITORY.git

Create a main branch
____________________

You have now created your project. 

You need to make sure that you are actually located in the repository of your project to be able to modify it. 

Your command line should look like ``C:\Users\YOUR-USERNAME\YOUR-REPOSITORY$>``

By default, your root location in the terminal is ``C:\Users\YOUR-USERNAME\$``

It is possible to move to your repository by using the comand ``cd`` (change directory) + ``expected location`` as in the following example : 


.. code-block:: python
      
   cd C:\Users\YOUR-USERNAME\YOUR-REPOSITORY

And from here it is recommended to make your repository as a ``main`` branch. 

.. code-block:: python
      
   git branch -M main

.. note: 

   To verify the status of the main branch you just created : 
   
   .. code-blocks:: python 
          
      git branch



Create your first file
______________________

Before saving our project, we will create a first file inside it. This step can be done right after cloning the repository as a local repository. 

The first file to create is usually a ``README`` text file. 

It contains information about the global project and is usually the first one opened by the user. 


The command ``nano`` enables to edit various types of files via the terminal (``.txt``, ``.rst``, ``.js``, ``.css``, etc.). If no such file has been previously created, the command ``nano`` creates the file. 

.. code-block:: python 
 
   nano README.txt 



Make your first commit
______________________

Once you are satisfied with your files and created the correct environment to publish documentation, we can 'save' our project by using the command ``git commit`` ; 

.. code-block:: python
    :linenos:
 
    git status 
    git add . 
    git commit -m "YOUR MESSAGE"
    git push 


In this project, my first commit corresponds to : 

- `Download Git and Python`_ 

- `Download Sphinx`_

- `Create and import a repository`_

- `Create your first file`_ 

- `Create your first file`_

- `Make your first commit`_

 
My second commit follow the steps of : 

- `Set up a Python virtual environment`_

- `Create basic breadcrumbs`_

- `Create a main branch`_


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

Thanks to this bootstrapping step, you already have everything needed to render
the documentation as HTML for the first time.  To do that, run this command:




Then, open your terminal and login to gitHub. You'll need to setup your user name first using these commands to set and check if the operation was successful. 

https://www.geeksforgeeks.org/git/how-to-login-using-the-git-terminal/
