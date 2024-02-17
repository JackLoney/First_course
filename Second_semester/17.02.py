#4
class MediaPlyer:
    def open(self, file):
        self.filename = file
    
    def play(self):
        print('Воспроизведение ' + str(self.filename))

media1 = MediaPlyer()
media2 = MediaPlyer()
media1.open('filemedia1')
media2.open('filemedia2')
media1.play()
media2.play()

#5
class Graph:
    def set_data(self, data):
        self.data = data
    
    def draw(self):
        words = str()
        for i in self.data:
            if i >= 0 and i <= 10:
                words = words + str(i) + ' '
        return print(words)

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()

#7
import sys
class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            k = 0
            for i in fields:
                setattr(StreamData, str(i), str(lst_values[k]))
                k += 1
            return print(True)
        else:
            return print(False)    

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res       

sr = StreamReader()
data, result = sr.readlines()


#9
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
    def select(self, a, b):
        sort_data = list()
        if b > len(self.lst_data):
            b = len(self.lst_data)
        for i in range(a, b):
            sort_data.append(self.lst_data[i])
        return print(sort_data)
    
    def insert(self, data):
        for i in data:
            st_data = i.strip().split()
            self.lst_data.append({key: value for key, value in zip(self.FIELDS, st_data)})


db = DataBase()
db.insert(lst_in)
db.select(1, 4)

#10
class Translator:
    Transl_dict = {}

    def add(self, eng, rus):
        Value_word = list()
        Value_word = self.Transl_dict.get(eng, [])
        Value_word.append(rus)
        self.Transl_dict[eng] = list(set(Value_word))
    
    def remove(self, eng):
        del self.Transl_dict[eng]

    def translate(self, eng):
        return print(self.Transl_dict[eng])
    
Tr = Translator()
Tr.add('go', 'идти')
Tr.add('come', 'приходит')
Tr.add('go', 'идти')
Tr.add('go', 'ходить')
Tr.add('home', 'дом')
Tr.add('go', 'ехать')
Tr.remove('come')
Tr.translate('go')