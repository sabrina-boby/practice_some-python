
class apple:
	def call(self):
		print("you can call")
	def message(self):
	    print("you can send message")	


class samsung(apple):

	def picture(self):
	    print("you can take picture")    


s=samsung()
s.call()
s.message()
s.picture()
