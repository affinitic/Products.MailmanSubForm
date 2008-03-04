## Controller Validator "mmSubForm_validate"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=
##title=Mailman Sub Form Validator
##
reg_tool=context.portal_registration
request = context.REQUEST

if request.get('subscribe'):
    subemail = request.get('subemail', None)
    if subemail and reg_tool.isValidEmail(subemail):
        pass
    else:
        if subemail:
            state.setError('subemail', 'You did not enter a valid e-mail address.', 'invalid_email')
        else:
            state.setError('subemail', 'You did not enter an e-mail address.', 'invalid_email')
    if getattr(context, 'mmFullNameReq', '') == 'mmfn_required':
        if not request.get('realname', None):
            state.setError('realname', 'You did not enter a name.', 'invalid_realname')

if request.get('unsubscribe'):
    unsubemail = request.get('unsubemail', None)
    if unsubemail and reg_tool.isValidEmail(unsubemail):
        pass
    else:
        if unsubemail:
            state.setError('unsubemail', 'You did not enter a valid e-mail address.', 'invalid_email')
        else:
            state.setError('unsubemail', 'You did not enter an e-mail address.', 'invalid_email')

if state.getErrors():
    return state.set(status='failure', portal_status_message='Please correct the indicated errors.')
else:
    return state
