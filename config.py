from Products.CMFCore.CMFCorePermissions import setDefaultRoles

PROJECTNAME = "MailmanSubForm"
product_globals=globals()
DEFAULT_ADD_CONTENT_PERMISSION = "Add MailmanSubForm"

setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner',))