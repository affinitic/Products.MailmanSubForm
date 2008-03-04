#!/usr/bin/make
#
# Makefile for mailmansubform
#
# $Id: Makefile 6656 2007-02-12 18:27:14Z laz $
PYTHON=/opt/python2.4.3/bin/python2.4
ZOPE_HOME="/usr/lib/zope2.9.6"
SOFTWARE_HOME="/usr/lib/zope2.9.6/lib/python"
PYTHONPATH:=$(PYTHONPATH):$(SOFTWARE_HOME)

translations: extract-translations update-translations

.PHONY: extract-translations
extract-translations:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) i18nextract -d mailmansubform -o i18n -p .

.PHONY: update-translations
update-translations:
	msgcat -s i18n/generated.pot i18n/mailmansubform.pot -o i18n/mailmansubform-generated.pot
	msgmerge -U i18n/mailmansubform-fr.po i18n/mailmansubform-generated.pot
	msgmerge -U i18n/mailmansubform-nl.po i18n/mailmansubform-generated.pot
	msgmerge -U i18n/mailmansubform-de.po i18n/mailmansubform-generated.pot
	msgmerge -U i18n/mailmansubform-it.po i18n/mailmansubform-generated.pot
