# Создать классы Dna и Rna, объекты которых обладают следующими свойствами:
# Могут быть инициализированы строкой, соответствующей последовательности ДНК и РНК, соответственно
# Позволяют определить GC состав последовательности с помощью метода gc()
# Позволяют создать комплеметнарную последовательность с помощью метода reverse_complement()
#
# Объекты класса Dna дополнительно позволяют:
# Создавать объект класса Rna, соответствующий результату транскрипции последовательности оригинального объекта с использованием метода transcribe()


class RNA (str ):
    def __init__(self , object):
        self.sequence = object
        self.length = len ( self.sequence )
        if set ( self.sequence ) - set ( 'acgutACGUT' ) != set ( ):
            raise Exception ( '"' + self.sequence + '" ERROR: sequence with wrong letters '
                              + str ( set ( self.sequence ) - set ( 'acgutACGUT' ) ) )

    def gc(self):
        counter_gc = 0
        for i in range ( self.length ):
            if (self.sequence[ i ] == 'C') or (self.sequence[ i ] == 'G'):
                counter_gc += 1
        percent_gc = counter_gc * 100 / self.length
        return percent_gc

    def reverse_complement(self):
        complementary_sequence = {'A': 'U' , 'U': 'A' , 'C': 'G' , 'G': 'C' , 'a': 'u' , 'u': 'a' , 'c': 'g' ,
                                       'g': 'c'}
        complementary_pair = list (
            '' + complementary_sequence[ self.sequence[ i ] ] for i in range ( self.length ) )
        return ''.join ( complementary_pair[::-1] )


class DNA ( RNA ):
    def __init__(self , object):
        self.sequence = object
        self.length = len ( self.sequence )
        self.rna = self.transcribe ( )

    def reverse_complement(self):
        complementary_sequence = {'A': 'T' , 'T': 'A' , 'C': 'G' , 'G': 'C' , 'a': 't' , 't': 'a' , 'c': 'g' ,
                                  'g': 'c'}
        complementary_pair = list (
            '' + complementary_sequence[ self.sequence[ i ] ] for i in range ( self.length ) )
        return ''.join ( complementary_pair[::-1] )

    def transcribe(self)->RNA:
        transcribe = {'A': 'U' , 'T': 'A' , 'C': 'G' , 'G': 'C' ,  'a': 'u' , 't': 'a' , 'c': 'g' ,
                           'g': 'c' }

        transcribe_sequence = list (''+transcribe[ self.sequence[ i ] ]  for i in range (  self.length ))

        return RNA ( ''.join (transcribe_sequence[::-1]) )




# print ( '\nDNA' )
#
# sequence1 = 'TAGC'
# x = DNA ( sequence1 )
# print ( x.sequence )
# print ( 'GC %:' , x.gc ( ) )
# print ( 'Reverse:' , x.reverse_complement ( ) )
# print ( 'DNA->RNA:' , x.transcribe () )
#
#
# print ( '\nRNA' )
#
# sequence2 = 'AUCG'
# y = RNA ( sequence2 )
# print ( y.sequence )
# print ( 'GC %:' , y.gc ( ) )
# print ( 'Reverse:' , y.reverse_complement ( ) )

