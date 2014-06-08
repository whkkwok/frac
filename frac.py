from imathutil import gcd

#Define exceptions
class fracNoneError(Exception): pass

"""Valid construction instances
1)	frac ( integer, 1, 0 )
2)	frac ( integer, integer, 0 )
3)	frac ( integer, integer, integer )
4)	frac ( float, 1, 0 )
5)	frac ( frac, 1, 0 )
6)	frac ( frac, frac, 0 )

* mixed number
* improper fraction

Efforts made for matching frac.tuple () and frac.num (). At the time of writing, all internal methods for manipulating
frac.numerator is directly accessed, whereas for returning frac.numerator, frac.num () is used.
"""

class frac:
	def __init__ ( self, numerator, denominator=1, carrier=0 ):
		"""Constructor
		"""
		if numerator == None:
			self.numerator,  self.denominator, self.rawnum, self.rawden, self.rawcar = None, None, None, None, None
		else:
			self.rawnum, self.rawden, self.rawcar = numerator, denominator, carrier
			if isinstance ( numerator, float ):
				from string import find
				numeratorStg = str ( numerator )
				chkCarrier = lambda car : int ( ( car, '0' ) [ car == '' ] )
				chkSign = lambda sig : ( 1, - 1 )[ sig < 0 ]
				carrier = chkCarrier ( numeratorStg [ 0:find ( numeratorStg, ".") ] )
				numeratorStg = numeratorStg [ find ( numeratorStg, ".")+1: len ( numeratorStg ) ]
				numerator = int ( numeratorStg ) * chkSign ( numerator )
				denominator = 10 ** len ( numeratorStg )			
			try:
				numerator += carrier * denominator
			except TypeError:
				numerator = None
			g = gcd ( numerator, denominator )
			if g != None:
				self.numerator = numerator / g
				self.denominator = denominator / g
			else:
				self.numerator,  self.denominator, self.rawnum, self.rawden, self.rawcar = None, None, None, None, None

	def num ( self ):
		n, d = self.numerator, self.den ()	
		if n == None or d == None:
			return n	
		if d == 1:
			return n
		elif abs ( n ) > abs ( d ):
			try:
				w = divmod ( n,d )
			except ZeroDivisionError:
				return "None (caused by ZeroDivisionError)"
			return frac ( w[1], d ).num ()
		else:
			return n		

	def den ( self ):
		return self.denominator

	def car ( self ):
		n, d = self.numerator, self.den ()
		if n == None or d == None:
			return n
		if abs ( n ) > abs ( d ):
			if d != 1:
				try:
					w = divmod ( n, d )
				except ZeroDivisionError:
					return "None (caused by ZeroDivisionError)"			 
				return w[0]
			else:
				return 0
		elif abs ( n ) == abs ( d ):
			return 0
		else:
			return int ( float ( self ) )

	def tuple ( self ):
		if ( self.numerator == None) or ( self.denominator == None ):
			return ( None, None )
		elif ( abs ( self.numerator ) > abs ( self.denominator ) ):
			if self.denominator == 1:
				return ( self.numerator, self.denominator )
			w = divmod ( self.numerator, self.denominator )
			return ( w[0], frac ( w[1], self.denominator ).tuple() )
		else:
			return ( self.numerator, self.denominator )

	def compare ( self, other ):
		other, null = self.__castFraction ( other )
		plainFmt = lambda obj: ( obj.toString(), str ( obj.numerator ) )[obj.denominator == 1]
		uniq = lambda plain, raw: ("%s;r%s" % (plain, raw),	"%s" % (plain))[plain==raw]
		if self == null or other == null:
			return None
		if self > other:
			cmpbose = "%s is greater than %s" % ( uniq (plainFmt (self), self.rawString ()),  uniq (plainFmt (other), other.rawString ()) )
			return ( '>', cmpbose )
		if self == other:
			if id ( self ) == id ( other ):
				return ( '==', 'Self comparsion, i.e., identical' )
			cmpbose = "%s and %s are identical" % ( uniq (plainFmt (self), self.rawString ()),  uniq (plainFmt (other), other.rawString ()) )
			return ( '==', cmpbose )			
		if self < other:
			cmpbose = "%s is less than %s" % ( uniq (plainFmt (self), self.rawString ()),  uniq (plainFmt (other), other.rawString ()) )
			return ( '<', cmpbose )			

	def rawString ( self ):
		if ( self.numerator == None ) and ( self.denominator == None ):
			return "None"	
		elif str (self.rawden) == "1" and str (self.rawcar) == "0":
			return "%s" % ( str (self.rawnum) )
		elif str (self.rawcar) == "0":
			return "%s/%s" % ( str (self.rawnum), str (self.rawden) )			
		else:
			return "%s(%s/%s)" % ( str (self.rawcar), str (self.rawnum), str (self.rawden) )
		
	def tofloatString ( self, decPlaces=4 ):
		"""tofloatString
		Returns the frac with the specified decimal places, or 4 dp by default
		"""
		try:
			formatStg = "%%.%df" % ( decPlaces )
		except TypeError:
			formatStg = "%.8f"
		try:
			return formatStg % ( float (self.numerator ) / float ( self.denominator ) )
		except TypeError:
			return None

	def __float__ ( self ):
		return float ( self.numerator ) / float ( self.denominator )

	def __pow__ ( self, pwr ):
		fracpwr, null = self.__castFraction ( pwr )
		if isinstance ( pwr, frac ):
			if self == null or pwr == null:
				raise fracNoneError, "either base number or power is 'None'"
				return
		else:
			if fracpwr == null:
				raise fracNoneError, "either base number or power is 'None'"
				return
		if self != abs ( self ) and ( isinstance ( pwr, frac ) and abs ( self.denominator) > 1 ):
			raise ValueError, "negative number cannot be raised to a fractional power"
			return
		if isinstance ( pwr, frac ):
			decPwr = float ( pwr.numerator) / float ( pwr.denominator )
			return pow ( float ( self.numerator ), decPwr ) / pow ( float ( self.denominator ), decPwr )
		if isinstance ( pwr, float ):
			return pow ( float ( self.numerator ), pwr ) / pow ( float ( self.denominator ), pwr )			
		if isinstance ( pwr, int ):	 
			if pwr >= 0:
				return frac ( pow ( self.numerator, pwr ), pow ( self.denominator, pwr ) )
			else:
				fracNewNumerator = frac ( 1, pow ( self.numerator, abs ( pwr )) )
				fracNewDenominator = frac ( 1, pow ( self.denominator, abs ( pwr )) )
				return fracNewNumerator / fracNewDenominator

	def __rpow__ ( self, pwr ):
		if pwr == None or self == frac (None) or ( isinstance ( pwr, frac ) and pwr == frac ( None) ):
			raise fracNoneError, "either base number or power is 'None'"
			return
		if pwr != abs ( pwr ) and abs ( self.denominator) > 1:
			raise ValueError, "negative number cannot be raised to a fractional power"
			return		
		return pow (pwr, float ( self.numerator) / float ( self.denominator ) )

	def toString ( self ):
		return str ( self )

	def __str__ ( self ):
		if self.denominator == 1:
			return "%d" % ( self.numerator )
		elif ( self.numerator == None ) and ( self.denominator == None ):
			return "%s (of type %s)" % ( "None", frac.__name__ )			
		elif ( self.numerator == self.denominator ):
			return "%d" % ( "1" )
		elif ( abs ( self.numerator ) > abs ( self.denominator ) ):
			try:
				w = divmod ( self.numerator, self.denominator )
			except ZeroDivisionError:
				return "None (caused by ZeroDivisionError)"
			return "%d(%s)" % ( w[0], frac ( w[1], self.denominator ) )
		else:
			return "%d/%d" % ( self.numerator, self.denominator )

	def __neg__ ( self ):
		if self == frac ( None ):
			return self
		if isinstance ( self.rawnum, float ):	
			return frac ( self.rawnum * -1, self.rawden, self.rawcar )
		if isinstance ( self.rawnum, int ):
			if float ( self ) < 0:
				return frac ( abs ( self.numerator ), abs ( self.denominator ) )
			else:
				return frac ( abs ( self.numerator ) * -1, abs ( self.denominator ) )			 
		"""Unit Test
			Data: knownRawStringValues, ('-frac ( 3.0 )', -3.0)
			Test: testrawString
			Rationale: 	Using raw form of constructor's parameters to avoid the loss of the original format due to 
						the inplicit conversion to integer type for self.numerator and self.denominator
		"""

	def recip ( self ):
		if self.numerator == None and self.den () == None and self.rawnum == 0 and self.rawden == 1:
			self.denominator, self.numerator = self.rawden, self.rawnum
		elif self.numerator == 0 and self.den () == 1:
			self.numerator = None
			self.denominator = None
		else:
			~self
		
	def __invert__ ( self ):
		self.denominator, self.numerator = self.numerator, self.denominator

	def __div__ ( self, other ):
		other, null = self.__castFraction ( other )	
		if self == null or other == null:
			return null
		~other
		return self * other
	def __rdiv__ ( self, other ):
		other, null = self.__castFraction ( other )	
		if self == null or other == null:
			return null
		return other / self					 
	def __mul__ ( self, other ):
		other, null = self.__castFraction ( other )	
		if self == null or other == null:
			return null		
		return frac ( self.numerator * other.numerator, self.denominator * other.denominator )
	__rmul__ = __mul__
	def __add__ ( self, other ):
		other, null = self.__castFraction ( other )	
		if self == null or other == null:
			return null
		return frac ( self.numerator * other.denominator + other.numerator * self.denominator,
			self.denominator * other.denominator )
	__radd__ = __add__
	def __sub__ ( self, other ):
		other, null = self.__castFraction ( other )	
		if self == null or other == null:
			return null
		other = -other
		return self + other
	def __rsub__ ( self, other ):
		other, null = self.__castFraction ( other )	
		if self == null or other == null:
			return null
		return other - self		
	def __cmp__ ( self, other ):
		if ( self.numerator != None ) and ( other.numerator == None ):
			return abs(self.numerator)+1	# bypass the special meaning of 0 being True
		if ( self.numerator == None ) and ( other.numerator == None ):
			return 0			
		diff = ( self.numerator * other.denominator - self.denominator * other.numerator )
		return diff
	def __int__ ( self ):
		if self == frac ( None ):
			return self
		if self.denominator == 1:
			return self.numerator
		else:
			return self.numerator / self.denominator
	def __abs__ ( self ):
		return frac ( abs ( self.numerator ), abs ( self.denominator ) )
	def __castFraction ( self, operand ):	
		null = frac ( None )
		if isinstance ( operand, frac ):
			if operand == null:
				return ( null, null )
			else:
				return ( operand, null )
		else:
			if isinstance ( operand, int ):
				return ( frac ( operand ), null )
			elif isinstance ( operand, float ):
				"""Unit Test
					Data: knownPowValidInputValues, ('frac ( 1,2 )', '-2.0', 'pow (0.5, -2.0)')
					Test: testpowValidInput
					Rationale: 	Although the constructor already handles the "float" type parameter, for robustness' sake adding this
								checking will ensure the pow () working properly.
				"""			
				return ( frac ( operand ), null )
			else:
				return ( null, null )

def main ():
	import pdb
	pdb.set_trace ()
	e = -frac ( 3.0 )
	if __debug__:
		e.tuple
		float ( e)
	
def info(object, spacing=10, collapse=1):
	"""Print methods and doc strings.	    
	Takes module, class, list, dictionary, or string."""
	methodList = [method for method in dir(object) if callable(getattr(object, method))]
	processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
	print "\n".join(["%s %s" % (method.ljust(spacing), processFunc(str(getattr(object, method).__doc__))) for method in methodList])
				
if __name__ == "__main__":
	main ()