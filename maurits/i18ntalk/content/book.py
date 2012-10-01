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
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Author"),
            description=_(u"Author of this book"),
        ),
        required=True,
    ),


    atapi.IntegerField(
        'stars',
        storage=atapi.AnnotationStorage(),
        widget=atapi.IntegerWidget(
            label=_(u"Stars"),
            description=_(u"How well do you like this book? Use number 1 through 5."),
        ),
        validators=('isInt'),
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
    author = atapi.ATFieldProperty('author')

    stars = atapi.ATFieldProperty('stars')

    my = atapi.ATFieldProperty('my')


atapi.registerType(Book, PROJECTNAME)
