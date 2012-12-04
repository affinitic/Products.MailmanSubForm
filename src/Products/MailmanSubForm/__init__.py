from AccessControl import allow_module
from Products.CMFCore import utils
from Products.Archetypes.public import *
from Products.Archetypes import listTypes

from Products.CMFCore import permissions as CMFCorePermissions
from Products.CMFPlone.utils import ToolInit


# Get configuration data, permissions
from Products.MailmanSubForm.config import *
from zope.i18nmessageid import MessageFactory
MailmanSubFormMessage = MessageFactory("mailmansubform")

def initialize(context):

    # Import the type, which results in registerType() being called
    import MailmanSubForm

    # initialize the content, including types and add permissions
    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)

    allow_module('Products.MailmanSubForm.MailmanSubFormMessage')
