class sintaxys_try:

#diferentes casos para aplicar el TRY

	def suma(self, num1,num2):
		try:
			if num1<0:
				raise Exception ('quiero este if')
		except:
			return 'No aplica el if'

		else:
			return num1+num2
	
	def multipli(self, num1, num2):

		try:
			if not type(num1) is int:
				raise TypeError('solo integers') #levantame este mensaje

		except TypeError:
			return ('no puedo hacer la opercion')
		else:
			return num2*num1


	def divid(self,num2,num1):
		try: #este es el mas sencillito
			return num2/num1
		except ZeroDivisionError:
			return'Mensaje de error'
		except TypeError:
			return 'Tipea otro error'

		#else:
		
		#	pass
		finally:# cuando hay un finally se ejecuta siempre lo que él contenga
			print('Pase lo que pase este se ejecuta')
		

total = sintaxys_try() #creo mi objeto con el cual hago traigo los metodos que quiero utilizar

#print(total.divid(4,0))
#print(total.multipli(2,'a'))
print(total.suma(-1,2))