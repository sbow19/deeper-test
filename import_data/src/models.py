import mongoengine as me

'''
    User document class
'''
class UserPreference(me.EmbeddedDocument):
    # DATE TIME FORMAT
    timezone=me.StringField()


class User(me.Document):
    username=me.StringField(required=True)
    password=me.StringField(required=True)
    roles=me.ListField(required=True)
    preferences=me.EmbeddedDocumentField(UserPreference)
    active=me.BooleanField(required=True)
    created_at=me.FloatField(require=True)

