from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.CMFCorePermissions import ManagePortal
from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes, install_subskin

from cStringIO import StringIO

from Products.MailmanSubForm.config import *

def install(self):
    """Install MailmanSubForm: Install content types, skin layer, install the
    stylesheet, set up global properties, enable the portal factory and
    set up form controller actions for the widget actions
    """

    out = StringIO()

    print >> out, "Installing MailmanSubForm"

    # Install types
    classes = listTypes(PROJECTNAME)
    installTypes(self, out,
                 classes,
                 PROJECTNAME)
    print >> out, "Installed types"

    # Install skin
    install_subskin(self, out, product_globals)
    print >> out, "Installed skin"

    # Enable portal_factory
    factory = getToolByName(self, 'portal_factory')
    types = factory.getFactoryTypes().keys()
    if 'MailmanSubForm' not in types:
        types.append('MailmanSubForm')
        factory.manage_setPortalFactoryTypes(listOfTypeIds = types)

    print >> out, "Added MailmanSubForm to portal_factory"

    propsTool = getToolByName(self, 'portal_properties')
    siteProperties = getattr(propsTool, 'site_properties')
    navtreeProperties = getattr(propsTool, 'navtree_properties')

    # Add to default_page_types
    defaultPageTypes = list(siteProperties.getProperty('default_page_types'))
    if 'MailmanSubForm' not in defaultPageTypes:
        defaultPageTypes.append('MailmanSubForm')
    siteProperties.manage_changeProperties(default_page_types = defaultPageTypes)


    return out.getvalue()
