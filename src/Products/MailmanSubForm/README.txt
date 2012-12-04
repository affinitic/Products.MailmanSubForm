MailmanSubForm

A Plone content type (Archetypes/ATCT-based) that provides basic subscribe/unsubscribe
forms for a Mailman list. It communicates with Mailman via mail to list-request@server.

Developed by Steve McMahon, steve@dcn.org, originally for the Davis Community Network, www.dcn.org.
Much of the ATContentTypes and Archetypes setup boilerplate copied from Martin Aspeli's excellent RichDocument.
Initial version, February, 2006.

MailmanSubForm is released under the GNU General Public Licence, version 2.
Please see http://gnu.org for more details.

Installation

  Edit MailmanSubForm.py to specify default Mailman host name and web server.

  Install in the usual way, using the QuickInstaller.


Captcha feature (contact: laurent.lasudry@affinitic.be)

  If you want to use the captcha feature, you will need to install
  the collective.captcha package.


Originally tested with Mailman 2.1.5, Plone 2.1.2 and Archetypes 1.3.7-final.
Now tested with Plone 2.5.4, Plone 3 and Plone 4.
