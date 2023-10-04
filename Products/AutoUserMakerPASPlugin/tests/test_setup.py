from Products.AutoUserMakerPASPlugin.testing import PluginTestCase
from Products.CMFPlone.utils import get_installer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID


class TestSetup(PluginTestCase):
    product_name = 'AutoUserMakerPASPlugin'

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.installer = get_installer(self.portal, self.request)

    def test_product_installed(self):
        self.assertTrue(self.installer.is_product_installed(self.product_name))


class TestUninstall(PluginTestCase):
    product_name = 'AutoUserMakerPASPlugin'

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.installer = get_installer(self.portal, self.request)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product(self.product_name)

    def test_product_uninstalled(self):
        self.assertFalse(self.installer.is_product_installed(self.product_name))
