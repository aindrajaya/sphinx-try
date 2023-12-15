Configuration Options
=====================

``nav_title``
   Set the name to appear in the left sidebar/header. If not provided, uses
   html_short_title if defined, or html_title.
``touch_icon``
   Path to a touch icon, should be 152x152 or larger.
``google_analytics_account``
   Set to enable google analytics.
``repo_url``
   Set the repo url for the link to appear.
``repo_name``
   The name of the repo. If must be set if repo_url is set.
``repo_type``
   Must be one of github, gitlab or bitbucket.
``base_url``
   Specify a base_url used to generate sitemap.xml links. If not specified, then
   no sitemap will be built.
``globaltoc_depth``
   The maximum depth of the global TOC; set it to -1 to allow unlimited depth.
``globaltoc_collapse``
   If true, TOC entries that are not ancestors of the current page are collapsed.
``globaltoc_includehidden``
   If true, the global TOC tree will also contain hidden entries.
``theme_color``
    The theme color for mobile browsers. Hex Color without the leading #.
``color_primary``
    Primary color. Options are
    red, pink, purple, deep-purple, indigo, blue, light-blue, cyan,
    teal, green, light-green, lime, yellow, amber, orange, deep-orange,
    brown, grey, blue-grey, and white.
``color_accent``
    Accent color. Options are
    red, pink, purple, deep-purple, indigo, blue, light-blue, cyan,
    teal, green, light-green, lime, yellow, amber, orange, and deep-orange.
``html_minify``
   Minify pages after creation using htmlmin.
``html_prettify``
   Prettify pages, usually only for debugging.
``css_minify``
   Minify css files found in the output directory.
``logo_icon``
   Set the logo icon. Should be a pre-escaped html string that indicates a
   unicode point, e.g., ``'&#xe869'`` which is used on this site. The code
   point refers to the `Material Icons <https://fonts.google.com/icons>`_ font.
   This set provides a reasonable set of utility icons. Most sites should not
   use ``logo_icon`` and instead should set ``html_logo`` in ``conf.py`` to
   point to a custom SVG icon. Note that ``logo_icon`` takes precedent over
   ``html_logo`` and so it should be left empty when using ``html_logo``.
``master_doc``
   Include the master document at the top of the page in the breadcrumb bar.
   You must also set this to true if you want to override the rootrellink block, in which
   case the content of the overridden block will appear
``nav_links``
   A list of dictionaries where each has three keys:

   - ``href``: The URL or pagename (str)
   - ``title``: The title to appear (str)
   - ``internal``: Flag indicating to use pathto to find the page.  Set to False for
     external content. (bool)
``heroes``
   A ``dict[str,str]`` where the key is a pagename and the value is the text to display in the
   page's hero location.
``version_dropdown``
   A flag indicating whether the version drop down should be included. You must supply a JSON file
   to use this feature.
``version_dropdown_text``
   The text in the version dropdown button
``version_json``
   The location of the JSON file that contains the version information. The default assumes there
   is a file versions.json located in the root of the site.
``version_info``
   A dictionary used to populate the version dropdown.  If this variable is provided, the static
   dropdown is used and any JavaScript information is ignored.
``table_classes``
   A list of classes to **not strip** from tables. All other classes are stripped, and the default
   table has no class attribute. Custom table classes need to provide the full style for the table.
``table_no_strip``
   A list of classes to deactivate the complete table handling by sphinx-material for this specific table,
   so that all set table classes are kept.
   Default value: ``no-sphinx-material-strip``.