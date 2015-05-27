import tornado
from config import USERNAME, PASSWORD, HOST
from module.smtp.utils import Email, SimpleMail
from module.smtp.utils import QueMail


class EmailHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("templates/index.html")

    def post(self):
        qm = QueMail.get_instance()
        qm.send(Email(subject=self.get_argument('subject'), text=self.get_argument('message'), adr_to="ruddra90@gmail.com", adr_from="arnab.kumar@iappdragon.com"))
        # s = SimpleMail(USERNAME, PASSWORD, HOST, 25)
        # s.send_email(self.get_argument('message'), self.get_argument('subject'),
        #              self.get_argument('email').strip().split(','))
        self.render("templates/index.html")