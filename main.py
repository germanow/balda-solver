

class Field():

	ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'#Строка букв русского алфавита

	def __init__(self,size,word,slovar):
		if (size > 2) and (size % 2 != 0):
			self.size = size
		else:
			raise ValueError('Wrong size')
		self.mas = []
		for i in range(size):
			self.mas.append([])
			for j in range(size):
				self.mas[i].append(None)
		seredina = int((size-1)/2)
		if len(word) == size:
			for i in range(size):
				self.mas[seredina][i] = word[i]
		else:
			raise ValueError('Wrong word')
		self.slovar = slovar
		#Переменные для функции poisk
		self.slova = []
		self.slovo = []
		self.history = []
		#Переменная для анализа
		self.list_analys = []
	
	def proverka(self,slovo):
		#Проверка слова в словаре
		if self.slovar.count(slovo):
			self.slova.append((slovo,self.history))
		if self.slovar.count(slovo[::-1]):#Развёрнутое слово
			self.slova.append((slovo[::-1],self.history[::-1],'reversed'))

	def poisk(self,letter,i,j):
		#Поиск слов которые можно составить ткнув в точку i,j букву 
		#Слова лежат в self.slova в виде кортежа со словом и путём
		if (i < 0) or (j < 0):
			return 0
		if self.slovo:
			self.slovo += letter
		else:
			self.slovo = letter
		print(self.slovo)#debug
		self.history.append((i,j))
		self.proverka(self.slovo)
		try:
			if not self.history.count((i+1,j)) and self.mas[i+1][j]:#Верх
				self.poisk(self.mas[i+1][j],i+1,j)
		except IndexError:
			pass
		try:
			if not self.history.count((i,j-1)) and self.mas[i][j-1]:#Лево
				self.poisk(self.mas[i][j-1],i,j-1)
		except IndexError:
			pass
		try:
			if not self.history.count((i,j+1)) and self.mas[i][j+1]:#Право
				self.poisk(self.mas[i][j+1],i,j+1)
		except IndexError:
			pass
		try:
			if not self.history.count((i-1,j)) and self.mas[i-1][j]:#Низ
				self.poisk(self.mas[i-1][j],i-1,j)
		except IndexError:
			pass
		self.history = self.history[:-1]
		self.slovo = self.slovo[:-1]

	def analys(self):
		self.list_analys = []
		for i in range(self.size):
			for j in range(self.size):
				if not self.mas[i][j]:#Пустая клетка
					flag = False
					try:
						if self.mas[i+1][j]:#Верх
							flag = True
					except IndexError:
						pass
					try:
						if self.mas[i][j-1]:#Лево
							flag = True
					except IndexError:
						pass
					try:
						if self.mas[i][j+1]:#Право
							flag = True
					except IndexError:
						pass
					try:
						if self.mas[i-1][j]:#Низ
							flag = True
					except IndexError:
						pass
					if flag:
						for letter in self.ru:
							self.poisk(letter,i,j)
							if self.slova:
								self.list_analys.extend(self.slova)
							#Переменные для функции poisk
							self.slova = []
							self.slovo = []
							self.history = []



if __name__ == '__main__':
	slova = ['нота','раб','бар','прораб','ток','рок','док','тон','кот']
	f = Field(5,'батон',slova)
	# f.poisk('р',1,1)
	# print(f.slova)
	f.analys()
	print(f.list_analys)
