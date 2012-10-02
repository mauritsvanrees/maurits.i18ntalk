Internationalization in your package
====================================

.. This may become the text of my talk.  Or the presentation that I
.. will show.  I might switch to KeyNote or whatever.  We'll see.

Maurits van Rees

Zest Software

Sample code:
https://github.com/mauritsvanrees/maurits.i18ntalk


What is internationalization?
-----------------------------

i18n means making the web interface appear translated in your local
language instead of the default English.

I will not talk about localization (l10n), which means making dates,
times and currency appear in the format preferred in your local
language.

This is also not about multilingual sites, sites that have content in
both English and Dutch.

.. Maybe add two screen shots, in English and Dutch, just to make it
.. really clear.


Procedure
---------

If you add new strings in your package, you need to follow these steps
each time:

1. Make strings translatable.

2. Extract those strings with i18ndude into a po file (portable object).

3. Translate the strings in the .po file.


Strings in templates
--------------------

::

  <html ...
        i18n:domain="maurits.i18ntalk">

    <span i18n:translate="">A simple message</span>

    <span i18n:translate="">Label:</span> <tal:block tal:content="some_content" />

    <p i18n:domain="plone" i18n:translate="">
      A message in the plone domain.
    </p>
  </html>

In the ``.pot/.po`` file it becomes this::

  #: browser/test.pt:3
  msgid "A simple message"
  msgstr "Een eenvoudige boodschap"


Dynamic content
---------------

::

  <p i18n:translate="">
    This book has
    <span i18n:name="stars" tal:content="context/getStars" />
    stars.
  </p>

  #: browser/test.pt:9
  msgid "This book has ${stars} stars."
  msgstr "Dit boek heeft ${stars} sterren."

If you forget the ``i18n:name`` you get this in your ``.po`` file::

  #: ./browser/bookview.pt:15
  msgid "This book has <span>${DYNAMIC_CONTENT}</span> stars."
  msgstr "Dit boek heeft <span>${DYNAMIC_CONTENT}</span> sterren."

And this translation does not show up.


Strings in Python
-----------------

TODO


Strings in GenericSetup
-----------------------

TODO


Strings in ZCML
---------------

TODO


The structure and contents of the locales directory.
----------------------------------------------------

::

  locales
  locales/yourdomain.pot
  locales/manual.pot
  locales/plone.pot
  locales/nl
  locales/nl/LC_MESSAGES
  locales/nl/LC_MESSAGES/yourdomain.po
  locales/nl/LC_MESSAGES/plone.po


Register the locales in zcml.
-----------------------------

::

  <configure
      xmlns="http://namespaces.zope.org/zope"
      xmlns:i18n="http://namespaces.zope.org/i18n">

   <i18n:registerTranslations directory="locales" />

  </configure>


Installing i18ndude.
--------------------

buildout.cfg::

  [i18ndude]
  recipe = zc.recipe.egg
  eggs = i18ndude


script to update the locales
----------------------------

update_locales.sh::

  #! /bin/sh

  DOMAIN="maurits.i18ntalk"

  # Synchronise the templates and scripts with the .pot.  All on one
  # line normally.  And notice the dot at the end, for the current
  # directory.
  i18ndude rebuild-pot --pot locales/${DOMAIN}.pot \
      --create ${DOMAIN} \
      --merge locales/manual.pot \
      .

  # Synchronise the resulting .pot with all .po files
  for po in locales/*/LC_MESSAGES/${DOMAIN}.po; do
      i18ndude sync --pot locales/${DOMAIN}.pot $po
  done

  # Same for the plone domain.
  for po in locales/*/LC_MESSAGES/plone.po; do
      i18ndude sync --pot locales/plone.pot $po
  done


buildout:cfg
------------

::

  [instance]
  recipe = plone.recipe.zope2instance
  locales = ${buildout:directory}/locales
  environment-vars =
      PTS_LANGUAGES en nl
      zope_i18n_allowed_languages en nl
      zope_i18n_compile_mo_files true

The locales option is there since Plone 4.2.1.

If you specify PTS_LANGUAGES and do *not* specify
zope_i18n_allowed_languages, then you will use about 50 MB more
memory.  So either specify them both or not at all.

Note that on Plone 3 the ``zope_i18n_*`` options have no effect.
Specifying PTS_LANGUAGES actually *increases* your memory usage by about
6 MB in Plone 3.3.  In Plone 3.1 it reduces it by about 7 MB.  If you
use add-ons, these numbers will increase.  I have seen a 30 MB difference.


Include the mo files
--------------------

``MANIFEST.in``::

  recursive-include collective *
  recursive-include docs *
  include *
  global-exclude *.pyc


Releasing a package
-------------------

easy_install or pip::

  easy_install zest.releaser zest.pocompile

buildout::

  [release]
  recipe = zc.recipe.egg
  eggs =
      zest.releaser
      zest.pocompile


Extra translations
------------------

Just add a file::

  your/package/locales/nl/LC_MESSAGES/plone.po


Overriding existing translations
--------------------------------

Order of loading::

  $ cat parts/instance/etc/site.zcml 
  <configure
    ...
    <!-- Load the configuration -->
    <include files="package-includes/*-configure.zcml" />
    <five:loadProducts />

1. locales = ${buildout:directory}/locales

2. zcml = your.package

3. Products alphabetically until and including Products.CMFPlone

4. packages with z3c.autoinclude

5. rest of the Products

6. i18n folders (done by PlacelessTranslationService)


Expected changes in the future.
-------------------------------

- No more ``i18n:translate="some_message_id"``.

- Babel instead of i18ndude?

- Sprint: support extracting zcml in i18ndude?
  Code: https://github.com/collective/i18ndude


Questions
---------

Was anything unclear?  Anything you have missed?
