Sidebars
========

.. note::

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin tincidunt,
   purus nec ultricies consequat, dui nisl viverra purus, et molestie quam
   justo et mi. Ut a justo vel quam varius varius. Curabitur luctus, elit vel
   hendrerit gravida, ipsum lectus ultricies nisl, id fermentum risus ex ac
   dui.

You must set ``html_sidebars`` in order for the side bar to appear. There are
four in the complete set.

.. code-block:: python

   html_sidebars = {
       "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
   }

You can exclude any to hide a specific sidebar. For example, if this is changed to

.. code-block:: python

   html_sidebars = {
       "**": ["globaltoc.html"]
   }

then only the global ToC would appear on all pages (``**`` is a glob pattern).
