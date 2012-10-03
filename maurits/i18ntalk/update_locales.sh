#! /bin/sh

DOMAIN="maurits.i18ntalk"
I18NDUDE="../../bin/i18ndude"

# Rebuild the .pot file using the current messages from templates,
# scripts, xml.  And merge with manual.pot.  All on one line normally.
# Notice the dot at the end, for the current directory.
$I18NDUDE rebuild-pot --pot locales/${DOMAIN}.pot \
    --create ${DOMAIN} \
    --merge locales/manual.pot \
    .

# Synchronise the resulting .pot with all .po files
for po in locales/*/LC_MESSAGES/${DOMAIN}.po; do
    $I18NDUDE sync --pot locales/${DOMAIN}.pot $po
done

# Same for the plone domain.
for po in locales/*/LC_MESSAGES/plone.po; do
    $I18NDUDE sync --pot locales/plone.pot $po
done
