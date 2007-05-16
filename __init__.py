from Globals import package_home
from Products.CMFCore import utils, CMFCorePermissions, DirectoryView
from Products.CMFPlone.PloneUtilities import ToolInit
from Products.Archetypes.public import *
from Products.Archetypes import listTypes
from Products.Archetypes.utils import capitalize

# Get configuration data, permissions
from Products.MailmanSubForm.config import *

# Register skin directories so they can be added to portal_skins
skin_globals=globals()
DirectoryView.registerDirectory('skins', skin_globals)
DirectoryView.registerDirectory('skins/MailmanSubForm', skin_globals)

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
