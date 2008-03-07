# -*- coding: utf-8 -*-

from zope.component import getMultiAdapter
from zope.interface import implements

from Products.Five import BrowserView
from Products.MailmanSubForm.browser.interfaces import ICaptchaValidation

class CaptchaValidation(BrowserView):
    """
    Class to validate the captcha
    """
    implements(ICaptchaValidation)

    def validate(self):
        """
        Validate the entered text
        """
        context = self.context
        request = self.request
        view = getMultiAdapter((context, request), name='captcha')
        return view.verify(request.get('captcha', None))
