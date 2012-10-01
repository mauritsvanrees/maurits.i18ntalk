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



buildout:cfg: compiling mo files at startup and registering an extra locales directory.

Releasing a package with compiled files, using zest.pocompile and MANIFEST.in.

How to add extra translations.

How to override existing translations.

Expected changes in the future.

Answering questions.
