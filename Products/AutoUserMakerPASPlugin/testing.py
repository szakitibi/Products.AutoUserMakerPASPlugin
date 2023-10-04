from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing.bbb import PloneTestCase


class ProductsAutousermakerpaspluginLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import Products.AutoUserMakerPASPlugin
        self.loadZCML(package=Products.AutoUserMakerPASPlugin)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'Products.AutoUserMakerPASPlugin:default')


AUTOUSERMAKERPASPLUGIN_FIXTURE = ProductsAutousermakerpaspluginLayer()


AUTOUSERMAKERPASPLUGIN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(AUTOUSERMAKERPASPLUGIN_FIXTURE,),
    name='ProductsAutousermakerpaspluginLayer:FunctionalTesting'
)


class PluginTestCase(PloneTestCase):
    """ Base class for AutoUserMakerPASPlugin tests """

    layer = AUTOUSERMAKERPASPLUGIN_FUNCTIONAL_TESTING
