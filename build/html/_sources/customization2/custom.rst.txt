Customizing the layout
======================

You can customize the theme by overriding Jinja template blocks. For example,
'layout.html' contains several blocks that can be overridden or extended.

Place a 'layout.html' file in your project's '/_templates' directory.

.. code-block:: bash

    mkdir source/_templates
    touch source/_templates/layout.html

Then, configure your 'conf.py':

.. code-block:: python

    templates_path = ['_templates']

Finally, edit your override file ``source/_templates/layout.html``:

.. code-block:: jinja

    {# Import the theme's layout. #}
    {% extends '!layout.html' %}

    {%- block extrahead %}
    {# Lorem Ipsum content for customization #}
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    {# Call the parent block #}
    {{ super() }}
    {%- endblock %}
