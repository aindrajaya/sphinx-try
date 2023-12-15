.. highlight:: rst

.. _rst-primer:

========================
Example no Scroll on Top
========================

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nec consectetur libero. Fusce in efficitur odio, at tincidunt ex. Nam aliquam elit a aliquam pellentesque. Nulla facilisi. Sed auctor nulla id orci laoreet, ac fermentum lectus tristique. Aliquam vitae aliquam sapien. Ut in suscipit leo. Suspendisse euismod felis a quam interdum, nec auctor libero suscipit.

.. seealso::

   The authoritative `reStructuredText User Documentation
   <http://docutils.sourceforge.net/rst.html>`_.  The "ref" links in this
   document link to the description of the individual constructs in the reST
   reference.

Paragraphs
----------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nec consectetur libero. Fusce in efficitur odio, at tincidunt ex. Nam aliquam elit a aliquam pellentesque. Nulla facilisi. Sed auctor nulla id orci laoreet, ac fermentum lectus tristique. Aliquam vitae aliquam sapien. Ut in suscipit leo. Suspendisse euismod felis a quam interdum, nec auctor libero suscipit.

.. _rst-inline-markup:

Inline markup
-------------

The standard reST inline markup is quite simple: use

* one asterisk: ``*text*`` for emphasis (italics),
* two asterisks: ``**text**`` for strong emphasis (boldface), and
* backquotes: ````text```` for code samples.

If asterisks or backquotes appear in running text and could be confused with
inline markup delimiters, they have to be escaped with a backslash.

Be aware of some restrictions of this markup:

* it may not be nested,
* content may not start or end with whitespace: ``* text*`` is wrong,
* it must be separated from surrounding text by non-word characters.  Use a
  backslash escaped space to work around that: ``thisis\ *one*\ word``.

These restrictions may be lifted in future versions of the docutils.

It is also possible to replace or expand upon some of this inline markup with
roles. Refer to :ref:`rst-roles-alt` for more information.

Lists and Quote-like blocks
---------------------------

List markup (:duref:`ref <bullet-lists>`) is natural: just place an asterisk at
the start of a paragraph and indent properly.  The same goes for numbered
lists; they can also be autonumbered using a ``#`` sign::

   * This is a bulleted list.
   * It has two items, the second
     item uses two lines.

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

::

   1. This is a numbered list.
   2. It has two items too.

1. This is a numbered list.
2. It has two items too.

::

   #. This is a numbered list.
   #. It has two items too.

#. This is a numbered list.
#. It has two items too.

Nested lists are possible, but be aware that they must be separated from the
parent list items by blank lines::

   * this is
   * a list

     * with a nested list
     * and some subitems

   * and here the parent list continues

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

Definition lists (:duref:`ref <definition-lists>`) are created as follows::

   term (up to a line of text)
      Definition of the term, which must be indented

      and can even consist of multiple paragraphs

   next term
      Description.

term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.

Note that the term cannot have more than one line of text.

Quoted paragraphs (:duref:`ref <block-quotes>`) are created by just indenting
them more than the surrounding paragraphs.

Line blocks (:duref:`ref <line-blocks>`) are a way of preserving line breaks::

   | These lines are
   | broken exactly like in
   | the source file.

| These lines are
| broken exactly like in
| the source file.

There are also several more special blocks available:

* field lists (:duref:`ref <field-lists>`, with caveats noted in
  :ref:`rst-field-lists`)
* option lists (:duref:`ref <option-lists>`)
* quoted literal blocks (:duref:`ref <quoted-literal-blocks>`)
* doctest blocks (:duref:`ref <doctest-blocks>`)

.. _rst-literal-blocks:

Literal blocks
--------------

Literal code blocks (:duref:`ref <literal-blocks>`) are introduced by ending a
paragraph with the special marker ``::``.  The literal block must be indented
(and, like all paragraphs, separated from the surrounding ones by blank
lines)::

   This is a normal text paragraph. The next paragraph is a code sample::

      It is not processed in any way, except
      that the indentation is removed.

      It can span multiple lines.

   This is a normal text paragraph again.

This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.

The handling of the ``::`` marker is smart:

* If it occurs as a paragraph of its own, that paragraph is completely left out
  of the document.
* If it is preceded by whitespace, the marker is removed.
* If it is preceded by non-whitespace, the marker is replaced by a single
  colon.

That way, the second sentence in the above example's first paragraph would be
rendered as "The next paragraph is a code sample:".

Code highlighting can be enabled for these literal blocks on a document-wide
basis using the :rst:dir:`highlight` directive and on a project-wide basis
using the :confval:`highlight_language` configuration option. The
:rst:dir:`code-block` directive can be used to set highlighting on a
block-by-block basis. These directives are discussed later.

.. _rst-doctest-blocks:

Doctest blocks
--------------

Doctest blocks (:duref:`ref <doctest-blocks>`) are interactive Python sessions
cut-and-pasted into docstrings. They do not require the
:ref:`literal blocks <rst-literal-blocks>` syntax. The doctest block must end
with a blank line and should *not* end with with an unused prompt::

    >>> 1 + 1
    2

The doctest appears below,

 >>> 1 + 1

.. _rst-tables:

Tables
------

For *grid tables* (:duref:`ref <grid-tables>`), you have to "paint" the cell
grid yourself.  They look like this::

   +------------------------+------------+----------+----------+
   | Header row, column 1   | Header 2   | Header 3 | Header 4 |
   | (header rows optional) |            |          |          |
   +========================+============+==========+==========+
   | body row 1, column 1   | column 2   | column 3 | column 4 |
   +------------------------+------------+----------+----------+
   | body row 2             | ...        | ...      |          |
   +------------------------+------------+----------+----------+

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

*Simple tables* (:duref:`ref <simple-tables>`) are easier to write, but
limited: they must contain more than one row, and the first column cells cannot
contain multiple lines.  They look like this::

   =====  =====  =======
   A      B      A and B
   =====  =====  =======
   False  False  False
   True   False  False
   False  True   False
   True   True   True
   =====  =====  =======

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

Two more syntaxes are supported: *CSV tables* and *List tables*. They use an
*explicit markup block*. Refer to table directives in the Sphinx documentation for more information.

Hyperlinks
----------

External links
~~~~~~~~~~~~~~

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


.. important:: There must be a space between the link text and the opening \< for the URL.

You can also separate the link and the target definition (:duref:`ref
<hyperlink-targets>`), like this::

   This is a paragraph that contains `a link`_.

   .. _a link: https://domain.invalid/


This is a paragraph that contains `a link`_.

.. _a link: https://domain.invalid/

Internal links
~~~~~~~~~~~~~~

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.



Sections
--------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


   =================
   This is a heading
   =================

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


* ``#`` with overline, for parts
* ``*`` with overline, for chapters
* ``=``, for sections
* ``-``, for subsections
* ``^``, for subsubsections
* ``"``, for paragraphs

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.



.. _rst-field-lists:

Field Lists
-----------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
::

   :fieldname: Field content

They are commonly used in Python documentation::

    def my_function(my_arg, my_other_arg):
        """A function just for me.

        :param my_arg: The first of my arguments.
        :param my_other_arg: The second of my arguments.

        :returns: A message (just for me, of course).
        """

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.



.. TODO This ref should be 'rst-roles', but that already exists. Rename the
.. other ones

.. _rst-roles-alt:

Roles
-----

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
 ``:rolename:`content```.

Docutils supports the following roles:

* :durole:`emphasis` -- equivalent of ``*emphasis*`` (*emphasis*)
* :durole:`strong` -- equivalent of ``**strong**`` (**strong**)
* :durole:`literal` -- equivalent of ````literal```` (``literal``)
* :durole:`subscript` -- subscript text (subscript\ :sub:`subscript`)
* :durole:`superscript` -- superscript text (superscript\ :sup:`superscript`)
* :durole:`title-reference` -- for titles of books, periodicals, and other
  materials

Refer to roles in the Sphinx documentation for roles added by Sphinx.


Explicit Markup
---------------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.



.. _rst-directives:

Directives
----------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


Docutils supports the following directives:

* Admonitions: :dudir:`attention`, :dudir:`caution`, :dudir:`danger`,
  :dudir:`error`, :dudir:`hint`, :dudir:`important`, :dudir:`note`,
  :dudir:`tip`, :dudir:`warning` and the generic
  :dudir:`admonition <admonitions>`.  (Most themes style only "note" and
  "warning" specially.)

.. attention::

   Attention

.. caution::

   Caution

.. danger::

   Danger

.. error::

   Error

.. hint::

   Hint

.. important::

   Important

.. note::

   Note

.. tip::

   Tip

.. warning::

   Warning

* Images:

  - :dudir:`image` (see also Images_ below)
  - :dudir:`figure` (an image with caption and optional legend)

* Additional body elements:

  - :dudir:`contents <table-of-contents>` (a local, i.e. for the current file
    only, table of contents)
  - :dudir:`container` (a container with a custom class, useful to generate an
    outer ``<div>`` in HTML)
  - :dudir:`rubric` (a heading without relation to the document sectioning)
  - :dudir:`topic`, :dudir:`sidebar` (special highlighted body elements)
  - :dudir:`parsed-literal` (literal block that supports inline markup)
  - :dudir:`epigraph` (a block quote with optional attribution line)
  - :dudir:`highlights`, :dudir:`pull-quote` (block quotes with their own
    class attribute)
  - :dudir:`compound <compound-paragraph>` (a compound paragraph)

* Special tables:

  - :dudir:`table` (a table with title)
  - :dudir:`csv-table` (a table generated from comma-separated values)
  - :dudir:`list-table` (a table generated from a list of lists)

* Special directives:

  - :dudir:`raw <raw-data-pass-through>` (include raw target-format markup)
  - :dudir:`include` (include reStructuredText from another file) -- in Sphinx,
    when given an absolute include file path, this directive takes it as
    relative to the source directory
  - :dudir:`class` (assign a class attribute to the next element) [1]_

* HTML specifics:

  - :dudir:`meta`
    (generation of HTML ``<meta>`` tags, see also :ref:`html-meta` below)
  - :dudir:`title <metadata-document-title>` (override document title)

* Influencing markup:

  - :dudir:`default-role` (set a new default role)
  - :dudir:`role` (create a new role)

  Since these are only per-file, better use Sphinx's facilities for setting the
  :confval:`default_role`.

.. warning::

   Do *not* use the directives :dudir:`sectnum`, :dudir:`header` and
   :dudir:`footer`.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
, ::

   .. function:: foo(x)
                 foo(y, z)
      :module: some.module.name

      Return a line of text input from the user.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


Images
------

reST supports an image directive (:dudir:`ref <image>`), used like so::

   .. image:: gnu.png
      (options)

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
.  For example, the file ``sketch/spam.rst`` could
refer to the image ``images/spam.png`` as ``../images/spam.png`` or
``/images/spam.png``.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
 (e.g. the ``_static`` directory for HTML output.)

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


Sphinx extends the standard docutils behavior by allowing an asterisk for the
extension::

   .. image:: gnu.*

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


Note that image file names should not contain spaces.

.. versionchanged:: 0.4
   Added the support for file names ending in an asterisk.

.. versionchanged:: 0.6
   Image paths can now be absolute.

.. versionchanged:: 1.5
   latex target supports pixels (default is ``96px=1in``).


Footnotes
---------

For footnotes (:duref:`ref <footnotes>`), use ``[#name]_`` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
::

   Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

   .. rubric:: Footnotes

   .. [#f1] Text of the first footnote.
   .. [#f2] Text of the second footnote.

You can also explicitly number the footnotes (``[1]_``) or use auto-numbered
footnotes without names (``[#]_``).


Citations
---------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
::

   Lorem ipsum [Ref]_ dolor sit amet.

   .. [Ref] Book or article reference, URL or whatever.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
 ``#``.

Here we take a look at some actual citations of famous papers such as [Chetty]_
in the American Economic Review or [Silver]_ in Nature.

.. [Chetty] Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


.. [Silver] Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


Substitutions
-------------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
::

   .. |name| replace:: replacement *text*

or this::

   .. |caution| image:: warning.png
                :alt: Warning!

See the :duref:`reST reference for substitutions <substitution-definitions>`
for details.

.. index:: ! pair: global; substitutions

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.



Comments
--------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
::

   .. This is a comment.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
::

   ..
      This whole indented block
      is a comment.

      Still in the comment.


.. _html-meta:

HTML Metadata
-------------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
::

   .. meta::
      :description: The Sphinx documentation builder
      :keywords: Sphinx, documentation, builder

will generate the following HTML output:

.. code:: html

   <meta name="description" content="The Sphinx documentation builder">
   <meta name="keywords" content="Sphinx, documentation, builder">

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
::

   .. meta::
      :keywords: backup
      :keywords lang=en: pleasefindthiskey pleasefindthiskeytoo
      :keywords lang=de: bittediesenkeyfinden

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
:

* ``pleasefindthiskey``, ``pleasefindthiskeytoo`` to *English* builds;
* ``bittediesenkeyfinden`` to *German* builds;
* ``backup`` to builds in all languages.

.. _metadata element: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta


Source encoding
---------------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.



Gotchas
-------

There are some problems one commonly runs into while authoring reST documents:

* **Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


* **No nested inline markup:** Something like ``*see :func:`foo`*`` is not
  possible.


.. rubric:: Footnotes

.. [1] When the default domain contains a :rst:dir:`class` directive, this
       directive will be shadowed.  Therefore, Sphinx re-exports it as
       :rst:dir:`rst-class`.