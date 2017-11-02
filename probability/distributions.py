import math

def binomialcoeffecient(n, k):
    return (math.factorial(n)/(math.factorial(k)*math.factorial((n - k))))

def expectationvaluebin(n, p):
    return n*p

def variancebin(n, p, stand):
    sigma = n*p*(1-p)
    if stand == True:
        return math.sqrt(sigma)
    else:
        return sigma

def expectationvalue(klist, plist):
    return sum([i*plist[klist.index(i)] for i in klist])

def variance(mu, klist, plist, stand):
    sigma = sum([(i - mu)**2*plist[klist.index(i)] for i in klist])
    if stand == True:
        return math.sqrt(sigma)
    else:
        return sigma

class Distribution:
    

    def __init__(self, n, p, m = 0, o = 0):
        self.n = n
        self.p = p
        self.m = m
        self.o = o
        self.distribution = ''
        self.value = [] 

    def binomial(self, k):
            self.distribution = 'binomial'
            return (binomialcoeffecient(self.n, k)*math.pow((self.p), k)
            *math.pow((1 - self.p), (self.n - k)))

    def hypergeometric(self, k):
            self.distribution = 'hypergeometric'
            print(self.o)
            return ((binomialcoeffecient(self.m, k)
            *binomialcoeffecient(self.n - self.m, self.o - k))
            /binomialcoeffecient(self.n, self.o))

    def cumulativ(self, b=0, a=0):
         if self.distribution == 'binomial':
            return sum(list(map(self.binomial, [i for i in range(a, b + 1)])))
         if self.distribution == 'hypergeometric':
            return sum(list(map(self.hypergeometric, [i for i in range(a, b + 1)])))

    def values(self):
        print(self.distribution)
        if self.distribution == 'binomial':
            self.value = [(k, self.binomial(k)) for k in range(self.n + 1)]
        elif self.distribution == 'hypergeometric':
            self.value = [(k, self.hypergeometric(k)) for k in range(self.n + 1)]


    def stdnormal(self, k, klist, plist):
        z = ((k - expectationvalue(klist, plist))/
        variance(expectationvalue(klist, plist), klist, plist, True))
        if z < 0:
            z = abs(z)
            z001 = 1 - (z % 0.1)
            z01 = 1 - z - z001
        else:
            z001 = (z % 0.1) / 0.1 
            z01 = z - z001
        f = open('./stdnormdist.csv', 'r')
        rows = csv.reader(f)
        for element in rows[0]:
            if element == z001:
                indexz001 = element.index(z001)
        for row in rows:
            for element in row:
                if z1 == element:
                    z = row[indexz001] 
        if negative:
            return 1 - z
        else:
            return z

    def st(self, alpha, side):
        alpha = alpha / 100
        if self.value == None:
                self.values()
        if side == 0:
            a = alpha/2
            b = 1 - a/2
            for i in range(len(self.value) - 1):
                if self.value[i][1] > a:
                    a = self.values[i][0]
                if self.value[i][1] > b:
                    b = self.value[i][0]
                    break
            return [a, b]

        elif side == 1:
            for i in range(len(self.value) - 1):
                if self.value[i][1] > 1 - alpha:
                    a = self.value[i][0]
                    break 
                return a 
        else:
            for i in range(len(self.value) - 1):
                if self.value  > alpha:
                    a = self.value[i - 1][0] 
            return a

            

