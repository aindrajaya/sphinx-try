.. Test documentation master file, created by
   sphinx-quickstart on Fri Dec 15 09:44:31 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Test's documentation!
================================

Roadmap
-------
`Material for Sphinx <https://github.com/bashtage/sphinx-material>`_ is a work in progress.  While
I believe that it is ready for use, there are a number of important limitation.  The most
important it to improve the CSS generation to use
`SASS <https://en.wikipedia.org/wiki/Sass_(stylesheet_language)>`_. It uses some python to
modify Sphinx output, which is not ideal.

The other issues are:

* improving the documentation;
* providing examples;
* sidebar customization;
* improving the search box; and
* ensuring that all Sphinx blocks work as intended.

You can see how it works on `statsmodels <https://www.statsmodels.org/>`_.

Getting Started
---------------
Install from git

.. code-block:: bash

   pip install git+https://github.com/bashtage/sphinx-material.git

Update your ``conf.py`` with the required changes:

.. code-block:: python

   html_theme = 'sphinx_material'

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   section1/index
   section2/index
   section3/index
   section4/index
   section5/index
   section6/index
   section7/index
   section8/index
   section9/index
   section10/index

.. toctree::
   :caption: Other Examples
   :maxdepth: 1

   basics/trial
   .. basics/index

.. toctree::
   :caption: Example Navigation
   :maxdepth: 2
   :hidden:

   customization/index
   customization2/index
   customization3/index

Index
~~~~~
* :ref:`genindex`
