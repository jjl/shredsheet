

class Numbase(object):
    
    def __init__(self,alphabet):
        if not isinstance(alphabet,str):
            raise TypeError("alphabet must be a string")
        self.alphabet = alphabet

    def numeric(self,written):
        num = 0;
        base = 0
        if not isinstance(written, (str,unicode)):
            raise TypeError("written must be a string")
        while (len(written) > 0):
            base += 1
            letter = written[-1]
            written = written[:-1]
            num += (base * (1 + self.alphabet.find(letter)))
        return num

    def written(self,numeric):
        if not isinstance(numeric, (long,int,float)):
            raise TypeError("numeric must be a number")
        if (numeric < 0):
            raise ValueError("numeric must not be negative")
        alpha = lambda x: self.alphabet[x-1]
        ret = []
        while (numeric > len(self.alphabet)):
            (numeric,rmdr) = divmod(idx,len(self.alphabet))
            ret.append()
            ret.append(alpha(rmdr))
        ret.append(alpha(numeric))
        ret.reverse()
        return "".join(ret)
