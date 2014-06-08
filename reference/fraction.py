"""Fraction - a Python class
Copyright 2000 by Mike Hostetler
Basic fraction class for Python. 
Updated 2002,2004 by Josh English

f=Fraction(n,d) - > (n,d are integers)
	Returns a fraction object with a given numerator and denominator
g=Fraction(i) - > (i is an integer)
	Returns a fraction object with a numerator of i and a denominator of 1
h=Fraction(d) - > (d is a float)
	Returns a fraction object, converting the float value to a fraction.

Currently fractions cannot be mixed (1 and 1/2 is 3/2, but you can get
the mixed number as a tuple), nor can the numerator of a fraction also 
be a fraction. The numerator and denominator must be integer values. The 
denominator must be a nonnegative integer. 
Some examples:
f = Fraction(1,-2)  will assign -1 to the numerator and 2 to the denominator.
f = Fraction(3) will assing 3 to the numerator and 1 to the denominator.
f = Fraction(-1.5) will assign -3 to the numerator and 2 to the denominator.

Fractions also work with the standard Python functions:
int(f) returns the integer portion of the fraction 
	f = Fraction(3,2)
	int(f) returns 1
float(f) returns the float decimal representation. This is equivalent of
	f.toDecimal()
pow(f,p) returns the fraction taken to the pth power.  
	
Other Functions defined here are:
gcd(a,b) Return the greatest common divisor of two integers

DecToFraction(x) Returns a fractional representation of a decimal x
"""

__author__ = "Josh English (english@spiritone.com)"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2005/03/11 08:22:42 $"
__copyright__ = "Copyright (c) 2005 Josh English"
__history__="""
	1.0 Initial Release
	1.1 Chanced a line in the DecToFraction function (suggested by 
			Mark Engelberg <mark.engelberg@alumni.rice.edu>)
		 Fraction now raises an error if passed non-number or complex types
	1.2 Fraction object can be used in exponentation
	"""


class FractionError(Exception): pass


def gcd(a,b):
	"""gcd(a,b) (a,b are integers)
	
	Returns the greatest common divisor of two integers.
	"""
	if b == 0: return a
	else: return gcd(b,a%b)

class Fraction:
	"""f=Fraction(numerator,denominator)
	
	This class supports fractions and interactions between fractions, integers, and floats.
	"""
	def __init__ (self,num=0,denom=1):
		from types import FloatType,IntType,LongType
		if type(num)==FloatType:
			f = DecToFraction(num)
			self.numerator = f.numerator
			self.denominator = f.denominator
		else:
			if type(num) not in [IntType,LongType]: raise FractionError, "Numerator must be a number"
			if type(denom) not in [IntType,LongType]: raise FractionError, "Denoninator must be a number"
			self.numerator= num
			if denom > 0:
				self.denominator= denom
			else:
				self.numerator = -self.numerator
				self.denominator=-denom
		self._standardize()
		
	def _standardize(self):
		"""Fractions should have integer numerator and denominators, not decimals or floats"""
		ok = 0
		while not ok:
			try:
				if float(int(self.denominator))==float(self.denominator):
					ok = 1
				else:
					self.denominator *= 10
					self.numerator *= 10
			except:
				ok = 1
				self.numerator = int(self.numerator)
				self.denominator = int(self.denominator)
				
	def _fractionize(self,fract2):
		"Create a fraction representation of whatever we've been given"
		from types import IntType,FloatType
		if type(fract2)==IntType: 
			fract2 = Fraction(fract2*self.denominator,self.denominator)
		elif type(fract2)==FloatType: 
			fract2 = Fraction(fract2)
		elif isinstance(fract2,Fraction):
			#fract2 = fract2
			return fract2
		else:
			raise FractionError, "Can't turn object into a fraction"
		return fract2
			
	def __repr__(self):
		if self.denominator == 1:
			return "%s" % (self.numerator,)
		elif self.numerator == 0:
			return "0"
		else:
			return "%s/%s" %(self.numerator,self.denominator)
		
	def toString(self):
		return self.__repr__()

	def toDecimal(self):
		"""f.toDecimal() 
		
		Returns a float value representation of the fraction f.
		"""
		return float(self.numerator)/self.denominator

	def mixedNumber(self):
		"""f.mixedNumer()
		
		Returns a string representation of the fraction.
		If the numerator is 0, mixedNumber returns '0'
		If the fraction represents an integer (eg. 4/2), mixedNumber() returns the
			integer as a string
		If the numerator is negative, the negative sign will be placed in front of
			the whole number
		If the whole number is 0 (eg. 2/3 as 0 2/3), mixedNumber returns a string
			without a whole number.
		"""
		if self.numerator < 0:
			neg = 1
			self.numerator = -self.numerator
		else: neg = 0
		whln = self.numerator/self.denominator # whole number
		
		newn = self.numerator - whln*self.denominator
		if neg: # Put things back where they belong
			whln = -whln
			self.numerator = -self.numerator 
		if whln: 
			if newn:
				return str(whln)+" "+Fraction(newn,self.denominator).toString()
			else:
				return str(whln)
		else:
			return Fraction(newn,self.denominator).toString()
			
	def recip(self):
		"""f.recip()
		
		Returns the reciprocal of the fraction.
		"""
		return Fraction(self.denominator,self.numerator)
		
	def reduce(self):
		"""f.reduce() 
		
		Reduces f to it's simplest form. After calling reduce() the fraction's 
		numerator and denominator will not have a common divisor.
		"""
		divisor= gcd(self.numerator,self.denominator)
		if divisor > 1:
			if self.numerator < 0:
				neg =1
				self.numerator = -self.numerator
			else: neg = 0
			self.numerator = self.numerator/divisor
			if neg: self.numerator = -self.numerator
			self.denominator= self.denominator/divisor

	def __add__(self,fract2):
		fract2 = self._fractionize(fract2)
		sum = Fraction()
		sum.numerator = (self.numerator*fract2.denominator)+(fract2.numerator*self.denominator)
		sum.denominator = (self.denominator*fract2.denominator)
		if sum.numerator > 0:
			sum.reduce()
		else:
			sum.numerator = -1*sum.numerator
			sum.reduce()
			sum.numerator = -1*sum.numerator
		return sum

	def __sub__(self,fract2):
		fract2 = self._fractionize(fract2)
		negative= Fraction(-1*fract2.numerator,fract2.denominator)
		return self + negative

	def __mul__(self,fract2):
		fract2 = self._fractionize(fract2)
		product = Fraction()
		product.numerator = self.numerator*fract2.numerator
		product.denominator = self.denominator*fract2.denominator
		if product.denominator < 0:
			product.denominator = -1*product.denominator
			product.reduce()
			product.numerator = -1*product.numerator
		elif product.numerator < 0:
			product.numerator = -1*product.numerator
			product.reduce()
			product.numerator = -1*product.numerator
		else:
			product.reduce()
		return product

	def __div__(self,fract2):
		fract2 = self._fractionize(fract2)
		return self * fract2.recip()

	def __iadd__(self,fract2):
		fract2 = self._fractionize(fract2)
		return self + fract2

	def __isub__(self,fract2):
		fract2 = self._fractionize(fract2)
		return self - fract2

	def __imul__(self,fract2):
		fract2 = self._fractionize(fract2)
		return self * fract2

	def __idiv__(self,fract2):
		fract2 = self._fractionize(fract2)
		return self / fract2

	def __radd__(self,fract2):
		fract2 = self._fractionize(fract2)
		return self + fract2

	def __rsub__(self,fract2):
		fract2 = self._fractionize(fract2)
		return fract2 - self

	def __rmul__(self,fract2):
		fract2 = self._fractionize(fract2)
		return self * fract2

	def __rdiv__(self,fract2):
		fract2 = self._fractionize(fract2)
		return fract2 / self
		
	def __eq__(self,fract2):
		fract2 = self._fractionize(fract2)
		return (self.numerator*fract2.denominator)==(self.denominator*fract2.numerator)
	
	def __cmp__(self,fract2):
		fract2 = self._fractionize(fract2)
		return cmp((self.numerator*fract2.denominator),(self.denominator*fract2.numerator))

	def __neg__(self):
		t= Fraction(self.numerator*-1,self.denominator)
		t.reduce()
		return t
		
	def __float__(self):
		return self.toDecimal()
	
	def __int__(self):
		if self.numerator < 0:
			res = -(-self.numerator/self.denominator)
		else:
			res = self.numerator/self.denominator
		return res
		
	def tuple(self):
		"""f.tuple() 
		
		Returns the numerator and denominator of the fraction as a tuple.
		"""
		return (self.numerator,self.denominator)
		
	def __pow__(self,p):
		if p < 0:
			return Fraction(pow(self.denominator,-p),pow(self.numerator,-p))
		else:
			return Fraction(pow(self.numerator,p),pow(self.denominator,p))
	
	def __rpow__(self,p):
		return pow(p,self.toDecimal())
	
	def __abs__(self):
		return Fraction(abs(self.numerator),self.denominator)
		
	def mixedTuple(self):
		"""f.mixedTuple()
		
		Returns the results of f.mixedNumber() as a tuple of three integers.
		"""
		if self.numerator < 0:
			neg = 1
			self.numerator = -self.numerator
		else: neg = 0
		whln = self.numerator/self.denominator # whole number
		
		newn = self.numerator - whln*self.denominator
		if neg: # Put things back where they belong
			whln = -whln
			self.numerator = -self.numerator
		return (whln,newn,self.denominator)


	
def DecToFraction(x): 
	"""DecToFraction(x) (x is a float value)
		Returns a fraction object based on a decimal.
		(Mark Engelberg)
	"""
	x = float(x)
	ipart = int(x)
	fpart = x-ipart
	f = Fraction()
	if fpart:
	# want to get it perfect if denominator is less than 10000
		for d in xrange(1,10000):
			testint = fpart * d
			if testint == int(testint):
				f = Fraction(int(testint),d)
				break
		if f == 0:
			y = eval(str(1.0/fpart))
			fpart = eval(str(fpart))
			p = len(str(fpart))-2
            #print p,ipart,fpart,y
			if p < 6:
				fp =fpart*pow(10,p)
				f = Fraction(int(fp),int(pow(10,p)))
			else:
				y *= 10000
				f = Fraction(10000,int(y))
	f.reduce()
	f+=ipart
	return f


def DecToFractionOld(x):
	"""DecToFraction(x) (x is a float value)
	
	Returns a fraction object based on a decimal.
	"""
	x = float(x)
	ipart = int(x)
	fpart = x-ipart
	if fpart:
		#y = 1.0/fpart
		y=eval(str(1.0/fpart))
		p = len(str(fpart))-2
		#print p,ipart,fpart,y
		if p < 6:
			fp =fpart*pow(10,p)
			f = Fraction(int(fp),int(pow(10,p)))
		else:
			y *= 10000
			f = Fraction(10000,int(y))
	else:
		f = Fraction()
	f.reduce()
	f+=ipart
	return f
	

if __name__=='__main__':
	print '-'*40
	print "Testing Fractions"
	f = Fraction(20,9)
	g = Fraction(14,-6)
	print "F=",f,f.toDecimal(),f.mixedNumber()
	print "G=",g,g.toDecimal(),g.mixedNumber()
	print "Tests"
	print "f==g:",f==g
	print "f==f:",f==f
	print "f==20/9 (as fraction):",f==Fraction(20,9)
	print "f==20/9 (as float):",f==20.0/9
	print "f<g:",f<g
	print "f>g:",f>g
	print "f<=g:",f<=g
	print "f>=g:",f>=g
	print "f!=g:",f!=g
	print "f-g:",f-g
	print "f+g:",f+g
	print "g+1:",g+1
	print "g+1.5:",g+1.5
	print "-f:",-f
	print "fg:",f*g
	print "g*2:",g*2
	print "3+f:",3+f
	print "4-g:",4-g
	print "2*g:",2*g
	print "g/2:",g/2
	print "2/g:",2/g
	print "int(g):",int(g)
	print "float(g):",float(g)
	print "g.tuple():",g.tuple()
	print "pow(f,-1):",pow(f,-1)
	print "pow(g,2):",pow(g,2)
	print "pow(g,-2):",pow(g,-2)
	print "pow(g,-3):",pow(g,-1)
	print "pow(2,f):",pow(2,f)
	f+=1
	print "f+=1:",f,f.toDecimal()
	f*=2
	print "f*=2:",f,f.toDecimal()
	f+=1.5
	print "f+=1.5",f,f.toDecimal()
	x= 2.1
	h = DecToFraction(x)
	print "H=DecToFrac(%s)=" % (x,) ,h
	print "H as mixed:",h.mixedNumber()
	i = Fraction(2.5)
	print "I=Fraction(2.5):",i
	print "I as tuple:",i.tuple()
	print "I as mixed tuple:",i.mixedTuple()
	
	

