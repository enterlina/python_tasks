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
        if set ( self.sequence ) - set ( 'acgutACGUT' ) != set ( ):
            raise Exception ( '"' + self.sequence + '" is inappropriate due to the presence of characters '
                              + str ( set ( self.sequence ) - set ( 'acguACGU' ) ) )

    def gc(self):
        self.counter_gc = 0
        for i in range ( 0 , self.length ):
            if (self.sequence[ i ] == 'C') or (self.sequence[ i ] == 'G'):
                self.counter_gc += 1
        self.percent_gc = self.counter_gc * 100 / self.length
        return self.percent_gc

    def reverse_complement(self):
        self.complementary_sequence = {'A': 'T' , 'T': 'A' , 'C': 'G' , 'G': 'C' , 'a': 't' , 't': 'a' , 'c': 'g' ,
                                       'g': 'c'}
        self.complementary_pair = ' '
        for i in range ( 0 , self.length ):
            self.complementary_pair += self.complementary_sequence[ self.sequence[ i ] ]

        return self.complementary_pair

    def transcribe(self):
        self.transcribe = {'A': 'T' , 'T': 'U' , 'C': 'G' , 'G': 'C' , 'U': 'U' , 'a': 't' , 't': 'u' , 'c': 'g' ,
                           'g': 'c' , 'u': 'u'}
        self.transcribe_sequence = ''
        for i in range ( 0 , self.length ):
            self.transcribe_sequence += self.transcribe[ self.sequence[ i ] ]

        return RNA ( self.transcribe_sequence )


class RNA ( DNA ):
    def __init__(self , object):
        self.sequence = object
        self.length = len ( self.sequence )



sequence1 = 'AGCTTAAAAA'

print ( '\nDNA' )
x = DNA ( sequence1 )
print ( x.sequence )
print ( 'GC %' , x.gc ( ) )
print ( 'Reverse' , x.reverse_complement ( ) )
print ( 'RNA' , x.rna.sequence )

# print ( 'Transcribe' , x.transcribe () )
# print ( 'Transcribe' , x.rna.transcribe ( x ) )

print ( '\nRNA' )

y = RNA ( sequence1 )
print ( y.sequence )
print ( 'GC %' , y.gc ( ) )
# print ( 'GC %' , y.transcribe( ) )
