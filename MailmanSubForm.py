from AccessControl import ClassSecurityInfo
try:
    # try to have a translatable content type
    from Products.LinguaPlone.public import *
except:
    from Products.Archetypes.public import *
from DateTime import DateTime
from config import PROJECTNAME, defaultServer, defaultWebServer
from Products.ATContentTypes.configuration import zconf
from Products.ATContentTypes.content.base import ATCTContent


schema = BaseSchema + Schema((
    BooleanField('mmLabel',
                 widget=LabelWidget(
                    label='Mailman List Subscribe/Unsubscribe Form',
                    label_msgid='MailmanSubForm_label_mmLabel',
                    description="""
                        Sets up a form that may be used to attempt subscription to
                        or unsubscription from a Mailman list.
                        Actual subscribe/unsubscribe is handled by sending mail to
                        the list request address.
                    """,
                    description_msgid='MailmanSubForm_help_mmLabel',
                    i18n_domain='mailmansubform',
                    ),
                ),
    StringField('mmServer',
                searchable=0,
                required=1,
                default=defaultServer,
                widget=StringWidget(
                    label='Mailman List Server',
                    label_msgid='MailmanSubForm_label_mmServer',
                    description="""
                    The host name of your Mailman list server. Subscribe/Unsubscribe
                    requests will be sent to this server.
                    """,                
                    description_msgid='MailmanSubForm_help_mmServer',
                    i18n_domain='mailmansubform',
                    ),
                ),
    StringField('mmWebServer',
                searchable=0,
                required=1,
                default=defaultWebServer,
                validators=('isURL',),
                widget=StringWidget(
                    label='Mailman Web Server',
                    label_msgid='MailmanSubForm_label_mmWebServer',
                    description="""
                    The base URL of your Mailman list server. This should be the web address
                    that precedes "listinfo" in the list info page address.
                    """,                
                    description_msgid='MailmanSubForm_help_mmWebServer',
                    i18n_domain='mailmansubform',
                    ),
                ),
    StringField('mmListName',
                searchable=0,
                required=1,
                widget=StringWidget(
                    label='List Name',
                    label_msgid='MailmanSubForm_label_mmListName',
                    description="""
                    The name of your Mailman list.
                    """,                
                    description_msgid='MailmanSubForm_help_mmListName',
                    i18n_domain='mailmansubform',
                    ),
                ),
    StringField('mmFullNameReq',
        default='',
        vocabulary='_get_selection_vocab_fullname',
        enforceVocabulary=1,
        widget=SelectionWidget(
            label='Subscriber Names',
            label_msgid='MailmanSubForm_label_mmFullNameReq',
            description="""
                Do you wish to ask for, or require, subscriber names?
            """,
            description_msgid='MailmanSubForm_help_mmFullNameReq',
            i18n_domain='mailmansubform',
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
            label_msgid='MailmanSubForm_label_mmListIntro',
            description = """
                This text will display at the top of the subscribe/unsubscribe form.
                Use it to introduce your list.
            """,
            description_msgid='MailmanSubForm_help_mmListIntro',
            rows = 7,
            i18n_domain = "mailmansubform",
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
