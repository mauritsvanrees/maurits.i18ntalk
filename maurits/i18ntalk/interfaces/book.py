from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from maurits.i18ntalk import i18ntalkMessageFactory as _



class IBook(Interface):
    """Information about a book"""

    # -*- schema definition goes here -*-
    author = schema.TextLine(
        title=_(u"Author"),
        required=True,
        description=_(u"Author of this book"),
    )
#
    stars = schema.Int(
        title=_(u"Stars"),
        required=False,
        description=_(u"How well do you like this book? Use number 1 through 5."),
    )
#
