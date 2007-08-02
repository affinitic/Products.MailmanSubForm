try: # New CMF
    from Products.CMFCore.permissions import setDefaultRoles
except: # Old CMF
    from Products.CMFCore.CMFCorePermissions import setDefaultRoles

# adjust these to your Mailman environment:
defaultServer    = "velocipede.dcn.davis.ca.us"
defaultWebServer = "http://mailman.dcn.org/"

PROJECTNAME = "MailmanSubForm"
product_globals=globals()
DEFAULT_ADD_CONTENT_PERMISSION = "Add MailmanSubForm"

setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner',))
