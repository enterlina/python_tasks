# Создать классы Dna и Rna, объекты которых обладают следующими свойствами:
# Могут быть инициализированы строкой, соответствующей последовательности ДНК и РНК, соответственно
# Позволяют определить GC состав последовательности с помощью метода gc()
# Позволяют создать комплеметнарную последовательность с помощью метода reverse_complement()
#
# Объекты класса Dna дополнительно позволяют:
# Создавать объект класса Rna, соответствующий результату транскрипции последовательности
# оригинального объекта с использованием метода transcribe()

class DNA ( ):
    # dna_sequence = 'AGCTTAAAAA'

    def __int__(self):

        # print ( "Enter DNA" )
        # self.dna_sequence = input ( )
        self.sequence = 'AGCTTAAAAA'
        self.length = len ( self.sequence )
        self.rna = self.RNA ( )

    def gc(self):
        self.counter_gc = 0
        for i in range ( 0 , self.length ):
            if (self.sequence[ i ] == 'C') or (self.sequence[ i ] == 'G'):
                self.counter_gc += 1
        self.___percent_gc___ = self.counter_gc / self.length
        return self.___percent_gc___

    def reverse_complement(self):
        self.complementary_sequence = {'A': 'T' , 'T': 'A' , 'C': 'G' , 'G': 'C'}
        self.___complementary_pair___ = ' '
        for i in range ( 0 , self.length ):
            self.___complementary_pair___ += self.complementary_sequence[ self.sequence[ i ] ]

        return self.___complementary_pair___

    class RNA:
        def transcribe(self):
            self.transcribe = {'A': 'T' , 'T': 'U' , 'C': 'G' , 'G': 'C'}
            self.___transcribe_sequence___ = ''
            for i in range ( 0 , self.length ):
                self.___transcribe_sequence___ += self.transcribe[ self.sequence[ i ] ]
            return self.___transcribe_sequence___


# class RNA ( DNA ):
#     def transcribe(self):
#         self.transcribe = {'A': 'T' , 'T': 'U' , 'C': 'G' , 'G': 'C'}
#         self.___transcribe_sequence___ = ''
#         for i in range ( 0 , self.length ):
#             self.___transcribe_sequence___ += self.transcribe[ self.sequence[ i ] ]
#         return self.___transcribe_sequence___


print ( '\nDNA' )
x = DNA ( )
x.__int__ ( )
print ( x.gc ( ) )
print ( x.reverse_complement ( ) )

print ( x.rna.transcribe ( ) )

# print ( '\nRNA' )
# y = RNA ( )
# y.__int__ ( )
# print ( y.gc ( ) )
# print ( y.reverse_complement ( ) )
# print ( y.transcribe ( ) )
