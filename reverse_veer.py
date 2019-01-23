import sys
import textwrap

code = sys.argv[1]
reversed_string = code[::-1]
length = len(code)
hex_encoded_string = reversed_string.encode('hex')
split_string = textwrap.wrap(hex_encoded_string, 8)

print 'reversed_string:\n' + reversed_string
print 'length\n' + str(length)
print 'hex_encoded_string\n' + hex_encoded_string
print 'hex encoded string split by 4 bytes\n'
for item in split_string:
	print '0x'+item
