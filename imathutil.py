def gcd ( m, n ):
	try:
		if m % n == 0:
			return n
		else:
			return gcd ( n, m%n )
	except ZeroDivisionError:
		return None
	except TypeError:
		return None

if __name__ == "__main__":
	print "%s: %d" % ( "gcd (10, 20)", gcd (10, 20) )
	print "%s: %d" % ( "gcd (20, 10)", gcd (20, 10) )
	print "%s: %d" % ( "gcd (0, 10)", gcd (0, 10) )
	print "%s: %s" % ( "gcd (10, 0)", gcd (10, 0) )
	print "%s: %d" % ( "gcd (-20, 10)", gcd (-20, 10) )
	print "%s: %d" % ( "gcd (10, -20)", gcd (10, -20) )
