import hashlib
import binascii

if str != bytes:

	# Python 3.x

	def ord(c):

		return c

	def chr(n):

		return bytes( (n,) )


__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

__b58base = len(__b58chars)

def b58encode(v):

  """ encode v, which is a string of bytes, to base58.

  """



  long_value = 0

  for (i, c) in enumerate(v[::-1]):

    long_value += (256**i) * ord(c)



  result = ''

  while long_value >= __b58base:

    div, mod = divmod(long_value, __b58base)

    result = __b58chars[mod] + result

    long_value = div

  result = __b58chars[long_value] + result



  # Bitcoin does a little leading-zero-compression:

  # leading 0-bytes in the input become leading-1s

  nPad = 0

  for c in v:

    if c == '\0': nPad += 1

    else: break



  return (__b58chars[0]*nPad) + result



def b58decode(v):#, length):

  """ decode v into a string of len bytes

  """

  long_value = 0

  for (i, c) in enumerate(v[::-1]):

    long_value += __b58chars.find(c) * (__b58base**i)



  result = bytes()

  while long_value >= 256:

    div, mod = divmod(long_value, 256)

    result = chr(mod) + result

    long_value = div

  result = chr(long_value) + result



  nPad = 0

  for c in v:

    if c == __b58chars[0]: nPad += 1

    else: break



  result = chr(0)*nPad + result

  # if length is not None and len(result) != length:
  #
  #   return None

  result = binascii.hexlify(result)[2:-10].decode("utf-8")

  return result

# private_key_WIF='PkPEAoUzAxMYKQEDZdH3qS3r8mBQAxSEqW8Y3sqRegLjoHhqBnhf'
# private_key = b58decode(private_key_WIF)
# print(private_key)
#616d6f41414149725377575774535548547549557a59454e7839497a68454641624b675375424772484b424761694d76693343426e674e71707274776a586d764b4935542b317649732b2f2b4b716d7a37486c795a46384e48413062557575567a673d3d
#print("616d6f41414149725377575774535548547549557a59454e7839497a68454641624b675375424772484b424761694d76693343426e674e71707274776a586d764b4935542b317649732b2f2b4b716d7a37486c795a46384e48413062557575567a673d3d".decode('hex'))
