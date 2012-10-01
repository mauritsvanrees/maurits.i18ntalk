from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from maurits.i18ntalk import i18ntalkMessageFactory as _



class IBook(Interface):
    """Information about a book"""

    # -*- schema definition goes here -*-
    favorite = schema.Bool(
        title=_(u"Favorite"),
        required=False,
        description=_(u"This is one of my favorite books"),
    )
#
