from google.appengine.ext import ndb

class Message(ndb.Model):
    message_text = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    broj = ndb.IntegerProperty()
    checked = ndb.BooleanProperty()
    tekst = ndb.TextProperty()
    decimalni = ndb.FloatProperty()