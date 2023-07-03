"""Used in installing AutoUserMakerPASPlugin."""
from plone import api
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
from zope.globalrequest import getRequest

from .Extensions import Install


def install(context):
    # context can be portal_setup, so make sure to get portal
    portal = api.portal.get()
    alsoProvides(getRequest(), IDisableCSRFProtection)
    Install.install(portal)  # adds plugin to acl_users


def uninstall(context):
    # context can be portal_setup, so make sure to get portal
    portal = api.portal.get()
    Install.uninstall(portal)  # removes plugin from acl_users
