import tornado.ioloop
import tornado.web
import time

# Port
HTTP_PORT = 2048

# REST endpoints
class TimestampHandler(tornado.web.RequestHandler):

	def compute_etag(self):
		return None

	def set_default_headers(self):
		self.set_header("Cache-control", "no-cache")
		self.set_header("Expires", "-1")
		self.set_header("Pragma", "no-cache")
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Content-Type", "application/json; charset=UTF-8")

	def get(self):
		print 'Got request.'
		self.write(str(time.time())) # Unique response every time request is made


backend = tornado.web.Application([
    (r"/timestamp/", TimestampHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path': './'}),
], autoreload=True)

if __name__ == "__main__":
	print 'Test backend was started'

	backend.listen(HTTP_PORT)
	tornado.ioloop.IOLoop.instance().start()