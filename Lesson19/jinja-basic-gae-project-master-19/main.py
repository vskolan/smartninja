#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Message

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


class MessageListHandler(BaseHandler):
    def get(self):
        poruke_ucitane = Message.query().fetch()
        parametri_za_proslijediti = {"messages" : poruke_ucitane}

        return self.render_template("message_list.html", params=parametri_za_proslijediti)

class MessageDetailsHandler(BaseHandler):
    def get(self, message_id):
        poruka_ucitana = Message.get_by_id(int(message_id))
        parametri_za_proslijediti = {"message" : poruka_ucitana}

        return self.render_template("message_details.html", params=parametri_za_proslijediti)

class ResultHandler(BaseHandler):
    def post(self):
        result = self.request.get("some_text")

        msg = Message(message_text=result, checked=True, tekst="aaaaaaaaaaaaaaaaadddddddddddddsaaaaaaaa", decimalni=1.25)
        msg.put()

        return self.write(result)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/result', ResultHandler),
    webapp2.Route('/message-list', MessageListHandler),
    webapp2.Route('/message/<message_id:\d+>', MessageDetailsHandler),
], debug=True)