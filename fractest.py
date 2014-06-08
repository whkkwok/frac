import frac
import unittest
import re

class KnowValues (unittest.TestCase):

	"""Check for constructor and print functions, fraction construction with valid values
	"""
	knownGoodValues = (	('frac ( 1, 2 )', '1/2'),			('frac ( 1, 1 )', '1'),					('frac ( 20, 30 )', '2/3'),			('frac ( -2, 5 )', '-2/5'),
							('frac ( 5, -10 )', '-1/2'),			('frac ( -8, -16 )', '1/2'),				('frac ( 3 )', '3'),					('frac ( 0 )', '0'),
							('frac ( -16 )', '-16'),				('frac ( .25 )', '1/4'),					('frac ( 0.8 )', '4/5'),				('frac ( 1.75 )', '1(3/4)'),
							('frac ( -.6 )', '-3/5'),			('frac ( -0.125 )', '-1/8'),			('frac ( -1.5 )', '-2(1/2)'),		('frac ( -3, 2 )', '-2(1/2)'),
							('frac ( -2.375 )', '-3(5/8)'),		('frac ( 3, 5, 2 )', '2(3/5)'),			('frac ( -3, 5, 2 )', '1(2/5)'),		('frac ( 3, -5, 2 )', '1(2/5)'),
							('frac ( 3, 5, -2 )', '-2(3/5)'),		('frac ( 3, 5, 0 )', '3/5'),				('frac ( 3, )', '3'),				('frac ( 9/10 )', '0' ))
								
	def testnewfrac ( self ):
		"""newfrac: __init__ () and toString () should give known result with known input"""
		for fracTup, fracEquiv in self.knownGoodValues:
			frac1 = eval ( 'frac.'+fracTup )
			self.assertEqual ( fracEquiv, frac1.toString () )				

	"""Check for constructor and print functions, fraction construction with invalid values
	"""
	knownBadValues = (	("frac ( 'a' )", 'None (of type frac)'),			("frac ( 'a', 'a' )", 'None (of type frac)'),
							("frac ( 'a', 'a', 'a' )", 'None (of type frac)'),		("frac ( None )", 'None (of type frac)'),
							("frac ( None, None )", 'None (of type frac)'),	("frac ( None, None, None )", 'None (of type frac)'),
							("frac ( 4, 'ab' )", 'None (of type frac)'),		("frac ( 4, 'ab', None )", 'None (of type frac)'),
							("frac ( 3, 0, 5 )", 'None (of type frac)'),		("frac ( 3, 0, )", 'None (of type frac)'),
							("frac ( 4, 0 )", 'None (of type frac)'),			("frac ( 4, 'ab', 0 )", 'None (of type frac)') )

	def testnewfracBadInput ( self ):
		"""newfracBadInput: __init__ () and toString () should give known result with known input"""
		for fracTup, fracEquiv in self.knownBadValues:
			frac1 = eval ( 'frac.'+fracTup )
			self.assertEqual ( fracEquiv, frac1.toString () )

	"""Check for getters
	"""
	knownGetterValues = (	('frac ( 2, 3 )', ( 2, 3, 0 ), 'frac ( 2, 3, 0 )'),		('frac ( 1 )', ( 1,1, 0 ), 'frac ( 1, 1, 0 )'),
								('frac ( -16 )', ( -16, 1, 0 ), 'frac ( -16, 1, 0 )'),	('frac ( -3,3 )', ( -1, 1, 0 ), 'frac ( -1, 1, 0 )'),
								('frac ( -3, 4 )', ( -3, 4, 0 ), 'frac ( -3, 4, 0 )'),	('frac ( 3.0 )', ( 3, 1, 0 ), 'frac ( 3, 1, 0 )'),
								('frac ( 3,7,2 )', ( 3, 7, 2 ), 'frac ( 17, 7, 0 )'),	('frac ( -3,7,-2 )', ( 4, 7, -3 ), '-frac ( 17, 7, 0 )') )

	def testgetters ( self ):
		"""num (), den (), car () should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTup1, tupRes, fracTup2  in self.knownGetterValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) )
			frac2 = eval ( r.sub ( 'frac.frac', fracTup2 ) )			
			self.assertEqual ( (frac1.num (), frac1.den (), frac1.car () ), tupRes )			
			self.assertEqual ( frac1.toString (), frac2.toString () )

	"""Negate checking frac vs frac
	"""
	knownNegfrac_vs_fracValues = (	('-frac ( 3,4 )', 'frac ( -3,4 )'),	('-frac ( 3,4 )', 'frac ( 3,-4 )'),
										('frac ( 3,4 )', 'frac ( -3,-4 )'),	('-(-frac ( 3,2 ))', 'frac ( 3,2 )'),
										('frac ( -1.5 )', 'frac ( -3,2 )') )

	def testnegfrac_vs_frac ( self ):
		"""negfrac_vs_frac should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTup1, fracTup2 in self.knownNegfrac_vs_fracValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) )
			frac2 = eval ( r.sub ( 'frac.frac', fracTup2 ) )
			self.assertEqual ( frac1.toString (), frac2.toString () )

	"""Negate checking frac vs integer
	"""
	knownNegfrac_vs_intValues = (	('-frac ( 2 )', -2),				('frac ( 3 )', 3),
										('frac ( -2 )', -2),				('frac ( 3.0 )', 3),
										('-frac ( 3.0 )', -3))

	def testnegfrac_vs_int ( self ):
		"""negfrac_vs_int should give known result with known input"""
		r = re.compile ( 'frac' )		
		for fracTup1, expRes in self.knownNegfrac_vs_intValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) )
			self.assertEqual ( int (frac1), expRes )
		for fracTup1, expRes in self.knownNegfrac_vs_intValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) )
			self.assertEqual ( int (frac1), expRes )

	"""Comparison checking
	"""
	knownCmpValues = (	('frac ( None )', 'frac ( 3,2 )', None),		('frac ( 3,2 )', 'frac ( None )', None),
							('frac ( None )', 'frac ( None )', None),		('frac ( 2,3 )', 'frac ( 3,2 )', '<'),
							('frac ( 2,3 )', 'frac ( 2,3 )', '=='),			('frac ( 2,3 )', 'frac ( 1,4 )', '>'),
							('frac ( 2,3 )', 'frac ( -1.5 )', '>') )		
		
	def testcomparefrac ( self ):
		"""comparefrac should give known result with known input"""
		for fracTup1, fracTup2, result in self.knownCmpValues:
			frac1 = eval ( 'frac.'+fracTup1 )
			frac2 = eval ( 'frac.'+fracTup2 )
			if result != None:					
				self.assertEqual ( frac1.compare ( frac2 )[0], result )
			else:
				self.assertEqual ( frac1.compare ( frac2 ), result )				

	"""Check for float ()
	"""
	knownFloatValues = ( ('frac ( -30, 4 )', -7.5),		('frac ( 1,2,-2 )', -1.5),				('-frac ( 1,2, -2)', 1.5),
						      ('-frac ( 3,4 )', -0.75),		('frac ( 2.375 )', 2.375 ), 			('frac ( 1,2, 2)', 2.5) )
	
	def testfloat ( self ):
		"""float() should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTup1, expRes in self.knownFloatValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) ) 
			self.assertAlmostEqual ( float ( frac1 ),  expRes )

	"""Check for tofloatString ()
	"""
	knownFloatStringValues = (	('frac ( 9/10 )', '0.0000'),
									('frac ( 20, 7)', '2.8571') )

	def testtofloatString ( self ):
		"""tofloatString() should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTup1, expRes in self.knownFloatStringValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) ) 
			self.assertEqual ( frac1.tofloatString (),  expRes )

	"""Check for tuple ()
	"""
	knownTupleValues = (	('frac ( 9/10 )', 'frac ( 0 )', (0, 1)),			('frac ( 0.9 )', 'frac ( 9/10.0 )', (9, 10)),
							('frac ( 20, 7)', 'frac ( 60, 70, 2 )', (2, (6, 7))) )

	def testtuple ( self ):
		"""tuple() should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTup1, fracTup2, tupleValue in self.knownTupleValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) )
			frac2 = eval ( r.sub ( 'frac.frac', fracTup2 ) )
			self.assertEqual ( frac1.tuple (), frac2.tuple () )
			self.assertEqual ( frac1.tuple () [0], tupleValue [0] )
			self.assertEqual ( frac1.tuple () [1], tupleValue [1] )
			
	"""Check for pow () for valid inputs
	"""
	knownPowValidInputValues = (	('2', 'frac ( 1,2 )', 'pow (2, 0.5)'),			('1.5', 'frac ( 1,2 )', 'pow (1.5, 0.5)'),
										('3', 'frac ( 1,4 )', 'pow (3, 0.25)'),			('frac ( 2,3 )', 'frac ( 2,3 )', 'pow (2.0/3.0, 2.0/3.0)'),
										('frac ( 1,2 )', '0', 'pow (0.5, 0)'),			('3', 'frac ( -2 )', 'pow (3, -2)'),
										('4.8', 'frac ( 1,3 )', 'pow (4.8, 1.0/3.0)'),	('4.8', '-frac ( 1,3 )', 'pow (4.8, -1.0/3.0)'),
										('frac ( 1,2 )', '2', 'pow (0.5, 2)'),			('frac ( 1,2 )', '-2', 'pow (0.5, -2)'),
										('frac ( 1,2 )', '-2.0', 'pow (0.5, -2.0)'),		('frac ( 1,2 )', 'frac (-2)', 'pow (0.5, -2)'),																	('frac ( 1,2 )', '-frac(2)', 'pow (0.5, -2)'),		('frac ( 2,3 )', 'frac ( -1,2 )', 'pow (2.0/3.0, -	1.0/2.0)'),
										('frac ( 1,2 )', '2.0', 'pow (0.5, 2.0)'),		('frac ( 1,2 )', 'frac ( 1,2 )', 'pow (0.5, 0.5)') )
		
	def testpowValidInput ( self ):
		"""pow() should give valid known result with known input"""
		"""1/2 1/2 <type 'instance'> <type 'instance'>
		AssertionError: 0.70710678118654746 != 0.70710678118654757 within 16 places"""
		r = re.compile ( 'frac' )
		for fracBase, fracPow, expRes in self.knownPowValidInputValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracBase ) )
			frac2 = eval ( r.sub ( 'frac.frac', fracPow ) )
#			print frac1, frac2, type ( frac1), type ( frac2) 	
			res = pow ( frac1, frac2)
			if isinstance ( res, frac.frac ):
				self.assertAlmostEqual ( float ( res ),  eval ( expRes ) )			
			else:
				self.assertAlmostEqual ( res,  eval ( expRes ) )

	"""Check for pow () for invalid inputs
	"""
	knownPowBadInputValues = (	('frac ( 1,2 )', 'None'),			('frac ( 2,3 )', 'frac ( None )') )
	knownrPowBadInputValues = ( ('None', 'frac ( 1,4 )'),			('None', 'frac ( None )'),
									  ('3', "frac ( 'a' )") )	

	def testpowInvalidInput ( self ):
		"""pow() should raise exceptions with bad input"""
		self.assertRaises ( ValueError, pow, -3, frac.frac ( 1,4 ))
		r = re.compile ( 'frac' )
		for fracBase, fracPow, in self.knownPowBadInputValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracBase ) )
			frac2 = eval ( r.sub ( 'frac.frac', fracPow ) )
#			print frac1, frac2, type ( frac1), type ( frac2) 	
			self.assertRaises ( frac.fracNoneError, pow, frac1, frac2 )
		for fracBase, fracPow, in self.knownrPowBadInputValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracBase ) )
			frac2 = eval ( r.sub ( 'frac.frac', fracPow ) )
#			print frac1, frac2, type ( frac1), type ( frac2) 	
			self.assertRaises ( frac.fracNoneError, pow, frac1, frac2 )

	"""Check for recip ()
	"""
	knownReciprocalValues = (	('frac ( 1, 2 )', 'frac ( 2 )'),			('frac ( 3,4 )', 'frac ( 4,3 )'),
									('-frac ( 3, 4 )', 'frac ( -4,3 )' ),		('frac ( 1.5 )', 'frac ( 2,3 )'),
									('frac ( 3,5,1 )', 'frac ( 5,8 )' ),		('frac ( 0 )', 'frac ( None )'))

	def testrecipValues ( self ):
		"""recip() should give known result `Value` with known input"""
		r = re.compile ( 'frac' )
		for fracTup1, fracTup2 in self.knownReciprocalValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) )
			frac2 = eval ( r.sub ( 'frac.frac', fracTup2 ) )
			frac1.recip ()			
			self.assertEqual ( frac1.toString (),  frac2.toString ())

	knownReciprocalTwiceValues = (	('frac ( 1, 2 )'),			('frac ( 3,4 )'),
										('-frac ( 3, 4 )' ),		('frac ( 1.5 )'),
										('frac ( 3,5,1 )' ),		('frac ( 0 )'))

	def testrecipClosure ( self ):
		"""recip() should give known `ORIGINAL` value with known input"""
		r = re.compile ( 'frac' )
		for fracTup1 in self.knownReciprocalTwiceValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) )
			frac2 = frac.frac ( frac1.numerator, frac1.den () )
			frac1.recip ()
			frac1.recip ()			
			self.assertEqual ( frac1.toString (),  frac2.toString ())

	"""Check for int ()
	"""
	knownIntValues = (	('frac ( -3, 1)', -3),			('frac ( -3, 4 )', -1),
							('frac ( 3, 4 )', 0 ),			('frac ( -6, 4)', -2) )

	def testintValue ( self ):
		"""int() should give known result `Value` with known input"""
		r = re.compile ( 'frac' )
		for fracTup1, expRes in self.knownIntValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) )
			self.assertEqual ( int (frac1),  expRes)	

	def testintType ( self ):
		"""int() should give known result `Type` with known input"""
		r = re.compile ( 'frac' )
		for fracTup1, expRes in self.knownIntValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) )
			self.assertEqual ( type ( int (frac1)),  type ( expRes))

	"""Check for abs ()
	"""
	knownAbsValues = (	('frac ( -3.0 )', 3),					('-frac ( 3 )', 3),
							('frac ( 30, 4 )', '7(1/2)'),			('-frac ( 30, 3 )', 10),
							('-frac ( -30, 4 )', '7(1/2)'),			('-frac ( 30, -4 )', '7(1/2)'),
							('-frac ( -30, -4 )', '7(1/2)'),
							('frac ( -30, 4 )', '7(1/2)' ),			('frac ( 30, -4)', '7(1/2)') )

	def testabs ( self ):
		"""abs() should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTup1, expRes in self.knownAbsValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) )
			self.assertEqual ( abs (frac1).toString (), str ( expRes ))

	"""Check for rawString ()
	"""
	knownRawStringValues = (	('frac ( 3.0 )', 3.0),					('frac ( 9/10 )', '0'),
									('-frac ( 3.0 )', -3.0),				('-frac ( -3.0 )', 3.0),
									('frac ( 30, 4 )', '30/4'),				('-frac ( 30, 3 )', '-10'),
									('frac ( -30, 3 )', '-30/3' ),			('frac ( 30, -3 )', '30/-3') )							

	def testrawString ( self ):
		"""rawString() should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTup1, expRes in self.knownRawStringValues:
			frac1 = eval ( r.sub ( 'frac.frac', fracTup1 ) )
			self.assertEqual ( frac1.rawString (), str ( expRes ))

	"""Check for arithmetic
	"""
	knownArithResultValues = (
					( 'frac ( 3, 8 )', 'frac ( 4, 6 )', 
						{ 'X+Y': '1(1/24)', 'Y+X': '1(1/24)' },				{ 'X-Y': '-7/24', 'Y-X': '7/24' } ,
						{ 'X*Y': '1/4', 'Y*X': '1/4' } ,						{ 'X/Y': '9/16', 'Y/X': '1(7/9)' }  ),
					( 'frac ( 3 )', 'frac ( 4 )', 
						{ 'X+Y': '7', 'Y+X': '7' },							{ 'X-Y': '-1', 'Y-X': '1' } ,
						{ 'X*Y': '12', 'Y*X': '12' } ,						{ 'X/Y': '3/4', 'Y/X': '1(1/3)' }  ),
					( 'frac ( 3 )', 'frac ( None )', 
						{ 'X+Y': 'None', 'Y+X': 'None' },					{ 'X-Y': 'None', 'Y-X': 'None' } ,
						{ 'X*Y': 'None', 'Y*X': 'None' } ,					{ 'X/Y': 'None', 'Y/X': 'None' }  ),	
					( 'frac ( 3 )', 'frac ( - 2 )', 
						{ 'X+Y': '1', 'Y+X': '1' },							{ 'X-Y': '5', 'Y-X': '-5' } ,
						{ 'X*Y': '-6', 'Y*X': '-6' } ,							{ 'X/Y': '-2(1/2)', 'Y/X': '-2/3' }  ),
					( '2', 'frac ( 4, 6 )', 
						{ 'X+Y': '2(2/3)', 'Y+X': '2(2/3)' },				{ 'X-Y': '1(1/3)', 'Y-X': '-2(2/3)' } ,
						{ 'X*Y': '1(1/3)', 'Y*X': '1(1/3)' } ,				{ 'X/Y': '3', 'Y/X': '1/3' }  ) )

	def testadd_X_Y ( self ):
		"""add_X_Y should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTupX, fracTupY, dictAdd, dictSub, dictMul, dictDiv  in self.knownArithResultValues:
			fracX = eval ( r.sub ( 'frac.frac', fracTupX ) )
			fracY = eval ( r.sub ( 'frac.frac', fracTupY ) )
			add_fracX_fracY = fracX + fracY
			self.assertEqual ( add_fracX_fracY.toString ().split ()[0], dictAdd ['X+Y'] )

	def testadd_Y_X ( self ):
		"""add_Y_X should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTupX, fracTupY, dictAdd, dictSub, dictMul, dictDiv  in self.knownArithResultValues:
			fracX = eval ( r.sub ( 'frac.frac', fracTupX ) )
			fracY = eval ( r.sub ( 'frac.frac', fracTupY ) )
			add_fracY_fracX = fracY + fracX
			self.assertEqual ( add_fracY_fracX.toString ().split ()[0], dictAdd ['Y+X'] )			

	def testsub_X_Y ( self ):
		"""sub_X_Y should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTupX, fracTupY, dictAdd, dictSub, dictMul, dictDiv  in self.knownArithResultValues:
			fracX = eval ( r.sub ( 'frac.frac', fracTupX ) )
			fracY = eval ( r.sub ( 'frac.frac', fracTupY ) )
			sub_fracX_fracY = fracX - fracY
			self.assertEqual ( sub_fracX_fracY.toString ().split ()[0], dictSub ['X-Y'] )

	def testsub_Y_X ( self ):
		"""sub_Y_X should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTupX, fracTupY, dictAdd, dictSub, dictMul, dictDiv  in self.knownArithResultValues:
			fracX = eval ( r.sub ( 'frac.frac', fracTupX ) )
			fracY = eval ( r.sub ( 'frac.frac', fracTupY ) )
			sub_fracY_fracX = fracY - fracX
			self.assertEqual ( sub_fracY_fracX.toString ().split ()[0], dictSub ['Y-X'] )

	def testmul_X_Y ( self ):
		"""mul_X_Y should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTupX, fracTupY, dictAdd, dictSub, dictMul, dictDiv  in self.knownArithResultValues:
			fracX = eval ( r.sub ( 'frac.frac', fracTupX ) )
			fracY = eval ( r.sub ( 'frac.frac', fracTupY ) )
			mul_fracX_fracY = fracX * fracY
			self.assertEqual ( mul_fracX_fracY.toString ().split ()[0], dictMul ['X*Y'] )

	def testmul_Y_X ( self ):
		"""mul_Y_X should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTupX, fracTupY, dictAdd, dictSub, dictMul, dictDiv  in self.knownArithResultValues:
			fracX = eval ( r.sub ( 'frac.frac', fracTupX ) )
			fracY = eval ( r.sub ( 'frac.frac', fracTupY ) )
			mul_fracY_fracX = fracY * fracX
			self.assertEqual ( mul_fracY_fracX.toString ().split ()[0], dictMul ['Y*X'] )

	def testdiv_X_Y ( self ):
		"""div_X_Y should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTupX, fracTupY, dictAdd, dictSub, dictMul, dictDiv  in self.knownArithResultValues:
			fracX = eval ( r.sub ( 'frac.frac', fracTupX ) )
			fracY = eval ( r.sub ( 'frac.frac', fracTupY ) )
			div_fracX_fracY = fracX / fracY
			self.assertEqual ( div_fracX_fracY.toString ().split ()[0], dictDiv ['X/Y'] )

	def testdiv_Y_X ( self ):
		"""div_Y_X should give known result with known input"""
		r = re.compile ( 'frac' )
		for fracTupX, fracTupY, dictAdd, dictSub, dictMul, dictDiv  in self.knownArithResultValues:
			fracX = eval ( r.sub ( 'frac.frac', fracTupX ) )
			fracY = eval ( r.sub ( 'frac.frac', fracTupY ) )
			div_fracY_fracX = fracY / fracX
			self.assertEqual ( div_fracY_fracX.toString ().split ()[0], dictDiv ['Y/X'] )

if __name__ == "__main__":
	unittest.main ()

""" Case 1
>>> cmp ( frac (None), frac (3,2))
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
  File "frac.py", line 126, in __cmp__
    diff = ( self.numerator * other.denominator - self.denominator * other.numer
ator )
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
>>> cmp ( frac(3,2), frac (None))
1
"""