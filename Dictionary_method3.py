#!/usr/bin/python

# author: Evangelia Lypiridi
# Data preprocessing for AMR corpus. Dictionary for method 3.

import sys

for line in sys.stdin:
	line = line.strip()

	line = line.replace("-sentence","")
	line = line.replace("11 29","29 november")
	line = line.replace('"',"")
	line = line.replace("temporal","")
	line = line.replace("monetary","")
	line = line.replace(":li","")
	line = line.replace("dollar","$")
	line = line.replace("1  10","1 october")
	line = line.replace(" 10 7 2008 ","10 july 2008")
	line = line.replace("9 7 2008","9 july 2008")
	line = line.replace("13 7 2008","13 july 2008")
	line = line.replace("19 7 2008","19 august 2008")
	line = line.replace("17 7 2008","17 july 2008")
	line = line.replace("25 8 2008","25 august 2008")
	line = line.replace("26 9 2008","26 september 2008")
	line = line.replace("31 10 2008","31 october 2008")
	line = line.replace("31 10 2007","31 october 2007")
	line = line.replace("20 10 2008 ","20 october 2008")
	line = line.replace("23 10 2008 ","23 october 2008")
	line = line.replace("2008 9 3","3 september 2008")
	line = line.replace("26 8 2008 ","26 august 2008")
	line = line.replace("28 7 2008","28 july 2008")
	line = line.replace("2008 11 18","18 november 2008")
	line = line.replace("11 25 2008","25 november 2008")
	line = line.replace("2008 11 27","27 november 2008")
	line = line.replace("2003 10 3","3 october 2003")
	line = line.replace("12 2 2004","2 december 2004")
	line = line.replace("2 4 2012","2 april 2012")
	line = line.replace("20 3 2004","20 march 2004")
	line = line.replace("28 6 2004","28 june 2004")
	line = line.replace("4 3 2007","4 march 2007")
	line = line.replace("2008 2 15","15 february 2008")
	line = line.replace("2008 4 8","8 april 2008")
	line = line.replace("18 12 1995","18 december 1995")
	line = line.replace("2008 4 30","30 april 2008")
	line = line.replace("1999 4 10","4 april 1999")
	line = line.replace("1999 6 30","30 june 1999")
	line = line.replace("1999 6 25","25 june 1999")
	line = line.replace("2003 8 14","14 august 2003")
	line = line.replace("23 1 2007","23 january 2007")
	line = line.replace("2007 2 2","2 february 2007")
	line = line.replace("2002 2 2","2 february 2002")	
	line = line.replace("7 6 2007","7 june 2007")
	line = line.replace("8 6 2007","8 june 2007")
	line = line.replace("2007 5 14","14 may 2007")
	line = line.replace("8 31","31 august")
	line = line.replace("4 23","23 april")
	line = line.replace("4 24","24 april")
	line = line.replace("8 31","31 august")
	line = line.replace("2008 1 28","28 january 2008")
	line = line.replace("9 11 2010","9 november 2010")
	line = line.replace("8 31 1993","31 august 1993")
	line = line.replace("61 year","61 years old")
	line = line.replace("55 year","55 years old")
	line = line.replace("1956","in 1956")
	line = line.replace("1950","in 1950")
	line = line.replace("1978","in 1978")
	line = line.replace("2001","in 2001")
	line = line.replace("1988","in 1988")
	line = line.replace("2007","in 2007")
	line = line.replace("2006","in 2006")
	line = line.replace("1970","in 1970")
	line = line.replace("1991","in 1991")
	line = line.replace("1953","in 1953")
	line = line.replace("1/2","half")
	line = line.replace("1997","in 1997")
	print line

