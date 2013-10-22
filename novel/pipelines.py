import os
import hashlib
import smtplib
from smtplib import SMTPException
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

def sendMail(title, link_text, link):
    # send mail
    username = # 'email@gmail.com'
    password = # 'password'

    sender = # 'email@gmail.com'
    receivers = # 'email@gmail.com'
    headers = ["From: " + sender,
               "Subject: %s Updated !" % title ,
               "To: " + receivers,
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
    headers = "\r\n".join(headers)
    body = """
    %s at %s
    """ % (link_text, link)

    try:
        server = # smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(sender, receivers, headers + "\r\n\r\n" + body)
        server.quit()
    except SMTPException:
       print "Error: unable to send email"

class NovelPipeline(object):
    def __init__(self):
        self.url_cache = dict()

    def process_item(self, item, spider):
        title = item['title'].pop().encode("utf-8")
        link_text = item['link_text'].pop().encode("utf-8")
        link = item['link'].pop().encode("utf-8")

        content = "%s@%s@%s\n" % (title, link_text, link)
        filename = hashlib.sha224(content).hexdigest() + ".cache"

        if os.path.exists(filename):
            raise DropItem("Duplicate item found: %s" % item)

        with open(filename, 'w') as f:
            f.write(content)
        sendMail(title, link_text, link)
        return item

if __name__ == '__main__':
    sendMail("Test", "Test link", "http://big5.zongheng.com/chapter/251393/5370766.html")