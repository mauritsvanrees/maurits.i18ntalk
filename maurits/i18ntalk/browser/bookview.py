from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from maurits.i18ntalk import i18ntalkMessageFactory as _


class BookView(BrowserView):
    """
    Book browser view
    """

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')
