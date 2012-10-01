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
