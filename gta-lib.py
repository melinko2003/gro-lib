#!/bin/python
# Grow Tent Area Library

import argparse

parser = argparse.ArgumentParser(description='grow tent air sizing')
parser.add_argument('-l', '--length', type=int, required=False, help='Lenth of Tent')
parser.add_argument('-w', '--width', type=int, required=False, help='Width of Tent')
parser.add_argument('-t', '--height', type=int, required=False, help='Height of Tent')
parser.add_argument('-c', '--chart', action='store_true', required=False, help='Outputs default size chart')
parser.add_argument('-v', '--verbose', action='store_true', required=False, help='Outputs default size chart')

args = parser.parse_args()

def surface_area(length,width,height):
	return length * width * height

def data_tent(ttype,length,width,height,verbosity):
	if verbosity is True:
		print(ttype + " Tent: " + str(length) + " x " + str(width) + " x " + str(height) + " is " + str(surface_area(length,width,height)) + 
		"sqft | CFM min: " + str(surface_area(length,width,height)*1.33) + " Max: " + str(surface_area(length,width,height)*2 ) + 
		fan_size((surface_area(length,width,height)*2),verbosity))
	else:
		print(ttype + "," + str(length) + "," + str(width) + "," + str(height) + "," + str(surface_area(length,width,height)) + ","	+ 
		str(surface_area(length,width,height)*1.33) + "," + str(surface_area(length,width,height)*2)  + "," + fan_size((surface_area(length,width,height)*2),verbosity))

def fan_size(sqft,verbosity):
	if sqft <= 206:
		if verbosity is True:
			return " | Fan & Filter: 4 in" 
		else:
			return "4,4"
	if sqft > 206 and sqft <= 350:
		if verbosity is True:
			return " | Fan & Filter: 6 in" 
		else:
			return "6,6"
	if sqft > 350 and sqft <= 740:
		if verbosity is True:
			return " | Fan & Filter: 8 in" 
		else:
			return "8,8"
	if sqft > 740 :
		amt = round((sqft / 740),5)
		if sqft%740 == 0:
			amt = str(amt).split('.')
		else:
			amt = str(amt + 1).split('.')
 		if verbosity is True:
			return " | Fan & Filter: " + str(amt[0]) + "x8 in" 
		else:
			return str(amt[0]) + "x8," + str(amt[0]) + "x8"


def size_chart(verbosity):

	for i in range(1,11):
		if ( i < 3 ):
			for x in range(4,7):
				data_tent('Box',i,i,x,verbosity)
				if ( i == 1):
					for y in range(2,6):
						data_tent('Lodge',i,x,y,verbosity)
				if ( i == 2):
					for y in range(4,7):
						data_tent('Rectangle',i,x,y,verbosity)
		else:
			for x in range(5,9):
				data_tent('Box',i,i,x,verbosity)

if args.chart is True :
	size_chart(args.verbose)
	exit(0)

if args.length is True:
	print "Length is empty"
	exit(1)
elif args.width is True:
	print "Width is empty"
	exit(1)
elif args.height is True:
	print "Height is empty"
	exit(1)
else:
	data_tent('user', args.length, args.width, args.height, args.verbose)
