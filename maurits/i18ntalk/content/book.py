"""Definition of the Book content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from maurits.i18ntalk.interfaces import IBook
from maurits.i18ntalk.config import PROJECTNAME

# -*- Message Factory Imported Here -*-
from maurits.i18ntalk import i18ntalkMessageFactory as _

BookSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'author',
        widget=atapi.StringWidget(
            label=_(u"Author"),
            description=_(u"Author of this book"),
        ),
        required=True,
    ),


    atapi.IntegerField(
        'stars',
        widget=atapi.IntegerWidget(
            label=_(u"Stars"),
            description=_(u"How well do you like this book? Use number 1 through 5."),
        ),
        validators=('isInt'),
        schemata='starschema',
    ),


))

schemata.finalizeATCTSchema(BookSchema, moveDiscussion=False)


class Book(base.ATCTContent):
    """Information about a book"""
    implements(IBook)

    meta_type = "Book"
    schema = BookSchema


atapi.registerType(Book, PROJECTNAME)
