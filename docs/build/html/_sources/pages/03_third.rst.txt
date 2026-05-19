Fill out the documentation
==========================

In this documentation, we will use reStructuedText (`.rst` extensions). It is a default plaintext markup language used by both Docutils and Sphinx.


Organise your pages with index
______________________________

The `index.rst` file is used to organise the different pages of the documentation. It is located in `YOUR-REPOSITORY/docs/source` directory. 

We access it by using the following commands : 

.. code-block:: python
    :linenos: 

    cd docs\source
    nano index.rst 

Then, the content of the page is as follows :


.. code-block:: python
    :linenos: 
  
    nano intex.rst 

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       pages/00_YOUR-PAGE0-NAME 
       pages/01_YOUR-PAGE1-NAME
       pages/02_YOUR-PAGE2-NAME

You can add different sections by adding a new section in the Table of contents Tree (toctree) : 

.. code-block:: python
    :linenos:

    nano intex.rst

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       pages/00_YOUR-PAGE0-NAME
       pages/01_YOUR-PAGE1-NAME
       pages/02_YOUR-PAGE2-NAME


    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       pages/00_YOUR-PAGE0-NAME
       pages/01_YOUR-PAGE1-NAME
       pages/02_YOUR-PAGE2-NAME



Create your pages directory and files
_____________________________________


Fill out your pages with documentation
______________________________________


Build a local documentation
___________________________


