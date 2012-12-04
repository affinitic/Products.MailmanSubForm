# -*- coding: utf-8 -*-

from zope.interface import Interface

class ICaptchaValidation(Interface):
    """
    Class to validate the captcha
    """

    def validate(self):
        """
        Validate the entered text
        """
