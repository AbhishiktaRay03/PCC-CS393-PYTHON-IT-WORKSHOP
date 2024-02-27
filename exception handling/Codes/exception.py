class CustomError(Exception):
	def __init__(self,message):
		self.message=message
def division(a ,b):
	try:
		if b==0:
			raise CustomError("ZERODIVISION")
		result=a/b
		return result
	except CustomError as ce:
		print (ce)
res=division(12,2)
print(res)
division(4,0)
