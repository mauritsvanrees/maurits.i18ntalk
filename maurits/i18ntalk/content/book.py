"""Definition of the Book content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from maurits.i18ntalk.interfaces import IBook
from maurits.i18ntalk.config import PROJECTNAME

# -*- Message Factory Imported Here -*-
i18ntalkMessageFactory = MessageFactory('maurits.i18ntalk')

BookSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.BooleanField(
        'favorite',
        storage=atapi.AnnotationStorage(),
        widget=atapi.BooleanWidget(
            label=_(u"Favorite"),
            description=_(u"This is one of my favorite books"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

BookSchema['title'].storage = atapi.AnnotationStorage()
BookSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(BookSchema, moveDiscussion=False)


class Book(base.ATCTContent):
    """Information about a book"""
    implements(IBook)

    meta_type = "Book"
    schema = BookSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    favorite = atapi.ATFieldProperty('favorite')


atapi.registerType(Book, PROJECTNAME)
