# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName


def install(context):
    """Install MailmanSubForm: Install content types, skin layer, install the
    stylesheet, set up global properties, enable the portal factory and
    set up form controller actions for the widget actions
    """
    if context.readDataFile('mailmansubform_various.txt') is None:
        return
    portal = context.getSite()
    propsTool = getToolByName(portal, 'portal_properties')
    siteProperties = getattr(propsTool, 'site_properties')

    # Add to default_page_types
    defaultPageTypes = list(siteProperties.getProperty('default_page_types'))
    if 'MailmanSubForm' not in defaultPageTypes:
        defaultPageTypes.append('MailmanSubForm')
    siteProperties.manage_changeProperties(default_page_types=defaultPageTypes)
