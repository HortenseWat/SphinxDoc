Fill out the documentation
==========================

In this documentation, we will use reStructuedText (``.rst`` extensions). It is a default plaintext markup language used by both Docutils and Sphinx.


Organise your pages with index
______________________________

The ``index.rst`` file is used to organise the different pages of the documentation. It is located in ``YOUR-REPOSITORY/docs/source`` directory. 

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
       :caption: YOUR-TITLE:

       pages/00_YOUR-PAGE0-NAME 
       pages/01_YOUR-PAGE1-NAME
       pages/02_YOUR-PAGE2-NAME

You can add different sections by adding a new section in the Table of contents Tree (toctree) : 

.. code-block:: python
    :linenos:

    nano intex.rst

    .. toctree::
       :maxdepth: 2
       :caption: YOUR-TITLE-1:

       pages/00_YOUR-PAGE0-NAME
       pages/01_YOUR-PAGE1-NAME
       pages/02_YOUR-PAGE2-NAME


    .. toctree::
       :maxdepth: 2
       :caption: YOUR-TITLE-2:

       pages/00_YOUR-PAGE0-NAME
       pages/01_YOUR-PAGE1-NAME
       pages/02_YOUR-PAGE2-NAME



Create your pages directory and files
_____________________________________

To create and organise the documentation pages, it is useful to save them in a ``/pages`` directory. This one is located  in ``\docs\source\pages``.

We will create this directory and the corresponding files. 

.. note::

   The files name needs to be exactly the same as the ones used in the `index.rst` file. 

.. code-block:: python
    :linenos: 
    
    cd docs\source
    mkdir pages
    cd pages 
    nano 00_YOUR-PAGE0-NAME.rst


Fill out your pages with documentation
______________________________________

Once one page has been created, we can fill out its content in the text editor.
And fill out the content as following, making sure that the title length is exactly the same length as the underlining. 

.. code-block::
    :linenos:

    YOUR-PAGE-TITLE
    ===============

    YOUR-PAGE-SUBTITLE1
    ___________________

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed condimentum
    nulla vel neque venenatis, nec placerat lorem placerat. Cras purus eros,
    gravida vitae tincidunt id, vehicula nec nulla. Fusce aliquet auctor cursus.
    Phasellus ex neque, vestibulum non est vitae, viverra fringilla tortor.


    YOUR-PAGE-SUBTITLE2
    ___________________

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed condimentum 
    nulla vel neque venenatis, nec placerat lorem placerat. Cras purus eros,
    gravida vitae tincidunt id, vehicula nec nulla. Fusce aliquet auctor cursus. 
    Phasellus ex neque, vestibulum non est vitae, viverra fringilla tortor.

This is a basic use of Sphinx's documentation, please see the parts :ref:`Applications` .


Build a local documentation
___________________________

Finally, once the pages are filled out as pleased, it is possible to publish a local documentation on your computer.

This documentation is not yet a website, and is published on online GitHub only after ``commit`` and ``puch`` commands. 

In the meanwhile, you will find your documentation in ``YOUR-REPOSITORY\docs\build\html\``. 

.. code-block:: python
    :linenos:
  
    cd ~\SphinxDoc
    python -m sphinx.cmd.build -M clean docs/source docs/build     #Clean the old documentation
    sphinx-build -M html docs/source/ docs/build/                  #Build a new one 

