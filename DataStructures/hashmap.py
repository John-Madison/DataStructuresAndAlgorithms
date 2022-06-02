class HashMap:
	
	def __init__(self, table_size = 10000):
		self.table_size = table_size
		self.table = [[] for _ in range(table_size)]
		self.count = 0 

	def table_index(self, key):
		return hash(key) % self.table_size

	def find(self, key):
		table_loc = self.table_index(key)
		for idx, (curr_key, _) in enumerate(self.table[table_loc]):
			if curr_key == key:
				return (table_loc, idx)
		return None

	def contains_key(self, key):
		return  self.find(key) != None

	def get(self, key):
		loc = self.find(key)
		if not loc:
			raise KeyError
		table_idx, list_idx =  loc

		return self.table[table_idx][list_idx][1]

	def put(self, key, value):
		loc = self.find(key)
		if loc is None:
			self.table[self.table_index(key)].append((key, value))
			self.count +=1
		else:		
			self.table[loc[0]][loc[1]] = ((key, value))

	def remove(self, key):
		loc = self.find(key)
		if not loc:
			raise KeyError
		del self.table[loc[0]][loc[1]]
		self.count -= 1

	def length(self):
		return self.count
