## Controller Python Script "mmSubForm_action"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=
##title=Process mmSubForm subscribe/unsubscribe
##
try:
    # use the translated object
    context = context.getTranslation()
except:
    # maybe no LinguaPlone installed ?
    pass

REQUEST=context.REQUEST

from Products.CMFPlone.utils import transaction_note
from Products.CMFCore.utils import getToolByName
from ZODB.POSException import ConflictError

##
## This may change depending on the called (portal_feedback or author)
state_success = "success"
state_failure = "failure"

plone_utils = getToolByName(context, 'plone_utils')
site_properties = getToolByName(context, 'portal_properties').site_properties


if REQUEST.has_key('subscribe'):
    rn = REQUEST.get('realname', None)
    ea = REQUEST.get('subemail', '')
    if rn:
      send_from_address = '"%s" <%s>' % (rn.strip().replace('"',''), ea.strip())
    else:
      send_from_address = ea
    message = 'subscribe'
    status_message = context.translate('Subscription request entered for ${address}',
                                       {'address': send_from_address})
    state.set(portal_status_message=status_message)
    state.set(subscribed='1')
    subject = "Subscription Request"
else:    
    send_from_address = REQUEST.get('unsubemail', '')
    message = 'unsubscribe'
    status_message = context.translate('Subscription cancellation request entered for ${address}',
                                       {'address': send_from_address})
    state.set(portal_status_message=status_message)
    state.set(unsubscribed='1')
    subject = "Subscription Cancellation Request"

envelope_from = site_properties.email_from_address

list_name = getattr(context, 'mmListName')
server_name = getattr(context, 'mmServer')
send_to_address = "%s-request@%s" % (list_name, server_name)
# fix encoding
send_to_address = send_to_address.encode('utf-8')

state.set(status=state_success) ## until proven otherwise

host = context.MailHost
#encoding = plone_utils.getSiteEncoding()
# above will cause secureSend to use base64 encoding, which Mailman won't comprehend
encoding = 'us-ascii'

try:
    result = host.secureSend(message, send_to_address, envelope_from, subject=subject, subtype='plain', charset=encoding, debug=False, From=send_from_address)
    # pass # we're testing
except ConflictError:
    raise
except: # TODO Too many things could possibly go wrong. So we catch all.
    exception = context.plone_utils.exceptionString()
    message = context.translate("Unable to send mail: ${exception}",
                                {'exception': exception})
    return state.set(status=state_failure, portal_status_message=message)

# state.setNextAction('redirect_to:string:mmSubForm_success')
return state
