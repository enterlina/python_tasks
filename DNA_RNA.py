

class DNA ( ):

    def __init__(self):

        print ( "Enter Sequence" )
        self.sequence = input ( )
        # self.sequence = 'AGCTTAAAAA'
        self.length = len ( self.sequence )
        self.rna = self.RNA ( )

    def gc(self):
        self.counter_gc = 0
        for i in range ( 0 , self.length ):
            if (self.sequence[ i ] == 'C') or (self.sequence[ i ] == 'G'):
                self.counter_gc += 1
        self.___percent_gc___ = self.counter_gc*100 / self.length
        return self.___percent_gc___

    def reverse_complement(self):
        self.complementary_sequence = {'A': 'T' , 'T': 'A' , 'C': 'G' , 'G': 'C'}
        self.___complementary_pair___ = ' '
        for i in range ( 0 , self.length ):
            self.___complementary_pair___ += self.complementary_sequence[ self.sequence[ i ] ]

        return self.___complementary_pair___

    class RNA ( ):
        def transcribe(self , DNA):
            self.length = DNA.length
            self.sequence = DNA.sequence
            self.transcribe = {'A': 'T' , 'T': 'U' , 'C': 'G' , 'G': 'C'}
            self.___transcribe_sequence___ = ''
            for i in range ( 0 , self.length ):
                self.___transcribe_sequence___ += self.transcribe[ self.sequence[ i ] ]
            return self.___transcribe_sequence___


class RNA ( DNA ):
    pass

    # def transcribe(self):
    #     self.transcribe = {'A': 'T' , 'T': 'U' , 'C': 'G' , 'G': 'C'}
    #     self.___transcribe_sequence___ = ''
    #     for i in range ( 0 , self.length ):
    #         self.___transcribe_sequence___ += self.transcribe[ self.sequence[ i ] ]
    #     return self.___transcribe_sequence___


print ( '\nDNA' )
x = DNA ( )

print ( 'GC %' , x.gc ( ) )
print ( 'Reverse' , x.reverse_complement ( ) )

print ( 'Transcribe' , x.rna.transcribe ( x ) )

print ( '\nRNA' )
y = RNA ( )
print ( 'GC %' , y.gc ( ) )
print ( 'Reverse' , y.reverse_complement ( ) )
print ( 'Transcribe' , y.rna.transcribe ( x ) )
