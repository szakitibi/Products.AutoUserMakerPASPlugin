"""Used in installing AutoUserMakerPASPlugin."""
from Products.CMFPlone.interfaces import INonInstallable
from plone import api
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import implementer
from zope.interface import alsoProvides
from zope.globalrequest import getRequest

from .Extensions import Install


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'Products.AutoUserMakerPASPlugin:uninstall',
        ]


def install(context):
    # context can be portal_setup, so make sure to get portal
    portal = api.portal.get()
    alsoProvides(getRequest(), IDisableCSRFProtection)
    Install.install(portal)  # adds plugin to acl_users


def uninstall(context):
    # context can be portal_setup, so make sure to get portal
    portal = api.portal.get()
    Install.uninstall(portal)  # removes plugin from acl_users
