# Создать классы Dna и Rna, объекты которых обладают следующими свойствами:
# Могут быть инициализированы строкой, соответствующей последовательности ДНК и РНК, соответственно
# Позволяют определить GC состав последовательности с помощью метода gc()
# Позволяют создать комплеметнарную последовательность с помощью метода reverse_complement()
#
# Объекты класса Dna дополнительно позволяют:
# Создавать объект класса Rna, соответствующий результату транскрипции последовательности оригинального объекта с использованием метода transcribe()


class DNA ( ):
    def __init__(self , object):
        self.sequence = object
        self.length = len ( self.sequence )
        self.rna = self.transcribe ( )
        if set(self.sequence)-set('acgutACGUT') != set():
            raise Exception('"'+self.sequence+'" is inappropriate due to the presence of characters '
                            +str(set(self.sequence)-set('acguACGU')))

    def gc(self):
        self.counter_gc = 0
        for i in range ( 0 , self.length ):
            if (self.sequence[ i ] == 'C') or (self.sequence[ i ] == 'G'):
                self.counter_gc += 1
        self.___percent_gc___ = self.counter_gc * 100 / self.length
        return self.___percent_gc___

    def reverse_complement(self):
        self.complementary_sequence = {'A': 'T' , 'T': 'A' , 'C': 'G' , 'G': 'C','a': 't' , 't': 'a' , 'c': 'g' , 'g': 'c'}
        self.___complementary_pair___ = ' '
        for i in range ( 0 , self.length ):
            self.___complementary_pair___ += self.complementary_sequence[ self.sequence[ i ] ]

        return self.___complementary_pair___

    def transcribe(self):
        self.transcribe = {'A': 'T' , 'T': 'U' , 'C': 'G' , 'G': 'C' , 'U': 'U','a': 't' , 't': 'u' , 'c': 'g' , 'g': 'c' , 'u': 'u'}
        self.___transcribe_sequence___ = ''
        for i in range ( 0 , self.length ):
            self.___transcribe_sequence___ += self.transcribe[ self.sequence[ i ] ]

        return RNA ( self.___transcribe_sequence___ )


class RNA ( DNA  ):
    def __init__(self , object):
        self.sequence = object
        self.length = len ( self.sequence )



sequence1 = 'AGCTTAAAAA'
x = DNA ( sequence1 )
print ( 'GC %' , x.gc ( ) )
print ( 'Reverse' , x.reverse_complement ( ) )
print ( 'rna %' , x.rna )
# print ( 'Transcribe' , x.transcribe () )

# print ( 'Transcribe' , x.rna.transcribe ( x ) )

# print ( '\nRNA' )
y = RNA ( sequence1 )
print ( y.sequence )

print ( 'GC %' , y.gc ( ) )
# # print ( 'Reverse' , y.reverse_complement ( ) )
print ( 'Transcribe' , y.transcribe ( ) )
