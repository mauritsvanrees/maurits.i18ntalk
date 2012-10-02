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

TODO


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

How to override existing translations.

Expected changes in the future.

Answering questions.
