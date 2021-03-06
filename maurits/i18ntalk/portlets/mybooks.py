import logging

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from zope import schema
from zope.formlib import form
from zope.i18n import translate
from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from maurits.i18ntalk import i18ntalkMessageFactory as _

__ = MessageFactory("plone")
logger = logging.getLogger('portletlogger')


class IMyBooks(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    maximum = schema.Int(
        title=_(u"Number of books"),
        description=_(u"Maximum number of books to show"),
        required=True,
        default=5)


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IMyBooks)

    # Set default values for the configurable parameters here
    maximum = 5

    def __init__(self, maximum=5):
        self.maximum = maximum

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return __(u"My Books")


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('mybooks.pt')

    def books(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        books = catalog(portal_type='Book', sort_on='created', sort_order='reverse')
        return books[:self.data.maximum]

    def title(self):
        # Log a translated message, just for the fun of it.
        msg = _("My books portlet is displayed.")
        translation = translate(msg, context=self.request)
        logger.info(translation)
        # And return a title.
        return _(u"My latest books")

    def book_message(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        books = len(catalog(portal_type='Book'))
        return _(u"There are ${books} books in total.",
                 mapping={'books': books})


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IMyBooks)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IMyBooks)
