#! /bin/sh

DOMAIN="maurits.i18ntalk"

# Synchronise the templates and scripts with the .pot.  All on one
# line normally.  And notice the dot at the end, for the current
# directory.
i18ndude rebuild-pot --pot locales/${DOMAIN}.pot \
    --merge locales/manual.pot \
    --create ${DOMAIN} \
   .

# Synchronise the resulting .pot with all .po files
for po in locales/*/LC_MESSAGES/${DOMAIN}.po; do
    i18ndude sync --pot locales/${DOMAIN}.pot $po
done
