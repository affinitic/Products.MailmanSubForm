from AccessControl import ClassSecurityInfo
from Products.Archetypes.public import *
from DateTime import DateTime
from config import PROJECTNAME
from Products.ATContentTypes.configuration import zconf
from Products.ATContentTypes.content.base import ATCTContent


# adjust these to your Mailman environment:
defaultServer    = "velocipede.dcn.davis.ca.us"
defaultWebServer = "http://mailman.dcn.org/"

schema = BaseSchema + Schema((
    BooleanField('mmLabel',
                 widget=LabelWidget(
                    label='Mailman List Subscribe/Unsubscribe Form',
                    description="""
                        Sets up a form that may be used to attempt subscription to
                        or unsubscription from a Mailman list.
                        Actual subscribe/unsubscribe is handled by sending mail to
                        the list request address.
                    """,
                    ),
                ),
    StringField('mmServer',
                searchable=0,
                required=1,
                default=defaultServer,
                widget=StringWidget(
                    label='Mailman List Server',
                    description="""
                    The host name of your Mailman list server. Subscribe/Unsubscribe
                    requests will be sent to this server.
                    """,                
                    ),
                ),
    StringField('mmWebServer',
                searchable=0,
                required=1,
                default=defaultWebServer,
                validators=('isURL',),
                widget=StringWidget(
                    label='Mailman Web Server',
                    description="""
                    The base URL of your Mailman list server. This should be the web address
                    that precedes "listinfo" in the list info page address.
                    """,                
                    ),
                ),
    StringField('mmListName',
                searchable=0,
                required=1,
                widget=StringWidget(
                    label='List Name',
                    description="""
                    The name of your Mailman list.
                    """,                
                    ),
                ),
    StringField('mmFullNameReq',
        default='',
        vocabulary='_get_selection_vocab_fullname',
        enforceVocabulary=1,
        widget=SelectionWidget(
            label='Subscriber Names',
            description="""
                Do you wish to ask for, or require, subscriber names?
            """,
            ),
        ),
#    StringField('mmSubPolicy',
#        default='',
#        vocabulary='_get_selection_vocab_spolicy',
#        enforceVocabulary=1,
#        widget=SelectionWidget(
#            label='Subscription Policy',
#            description="""
#                What's your subscription approval policy? This information is used
#                to determine the policy message accompanying the form. This is the
#                "subscribe_policy" setting on the "Privacy options/Subscription rules"
#                page of your Mailman administration settings.
#            """,
#            ),
#        ),
    TextField('mmListIntro',
        searchable=1,
        default="""
            <p>Use the forms below to either subscribe or unsubscribe.</p>
        """,
        validators = ('isTidyHtmlWithCleanup',),
        default_content_type = zconf.ATDocument.default_content_type,
        default_output_type = 'text/x-html-safe',
        allowable_content_types = zconf.ATDocument.allowed_content_types,
        widget = RichWidget(
            label = "List Introduction",
            description = """
                This text will display at the top of the subscribe/unsubscribe form.
                Use it to introduce your list.
            """,
            rows = 7,
            i18n_domain = "plone",
            allow_file_upload = False,
        ),
    ),
    ))

schema['description'].schemata = 'default'
schema['description'].widget.description = """
    A short summary of the item. Note that there is a rich-text list intro field
    at the end of this form.
    """
schema.moveField('mmLabel', pos='top')

class MailmanSubForm(ATCTContent):
    """A Subscribe/Unsubscribe form for a Mailman list"""

    schema = schema

    # Standard content type setup
    portal_type = meta_type = 'MailmanSubForm'
    archetype_name = 'Mailman Subscription Form'
    content_icon = 'MailmanSubForm_icon.png'
    typeDescription= 'A Subscribe/Unsubscribe form for a Mailman list'

    # Make sure we get title-to-id generation when an object is created
    _at_rename_after_creation = True

    default_view   = 'mmSubForm_view'
    immediate_view = 'mmSubForm_view'
    suppl_views    = ()

    security       = ClassSecurityInfo()

    def _get_selection_vocab_fullname(self):
        return DisplayList((
            ('','Not Requested'),
            ('mmfn_optional','Optional'),
            ('mmfn_required','Required'),
            ))

    def _get_selection_vocab_spolicy(self):
        return DisplayList((
            ('','Confirm (subscriber must respond to test message)'),
            ('mmsp_approval','Require approval (but no confirm)'),
            ('mmsp_canda','Confirm and approve'),
            ))


registerType(MailmanSubForm, PROJECTNAME)
