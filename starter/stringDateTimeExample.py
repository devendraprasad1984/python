from datetime import datetime


#http://www.tutorialspoint.com/python/python_str1ings.htm
date_object = datetime.strptime('Sep 6 2016  1:33PM', '%b %d %Y %I:%M%p')

print(date_object)

var1 = 'Hello World!'

print ("Updated str1ing :- "+ var1[:6] + 'Python')


print ("My name is %s and weight is %d kg!" % ('Zara', 21) )

para_str1 = """this is a long str1ing that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the str1ing, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str1)



str1 = "this is str1ing example....wow!!!";
sub = "i";
print ("str1.count(sub, 4, 40) : ", str1.count(sub, 4, 40))
sub = "wow";
print ("str1.count(sub) : ", str1.count(sub))


str11 = "this is str1ing example....wow!!!";
str12 = "exam";
print (str11.index(str12))
print (str11.index(str12, 10))
# print (str11.index(str12, 40))


str11 = "this is str1ing example....wow!!!"
str12 = "exam"
print (str11.find(str12))
print (str11.find(str12, 10))
print (str11.find(str12, 40))



str1 = u"this2009";  
print (str1.isnumeric())
str1 = u"23443434";
print (str1.isnumeric())


s = "-";
seq = ("a", "b", "c"); # This is sequence of str1ings.
print (s.join( seq ))


str1 = "this is str1ing example....wow!!!";
print (str1.swapcase())
str1 = "THIS IS str1ING EXAMPLE....WOW!!!";
print (str1.swapcase())


# from str1ing import maketrans   # Required to call maketrans function.
# import str1ing
intab = "aeiou"
outtab = "12345"
# trantab = maketrans(intab, outtab)
str1 = "this is str1ing example....wow!!!";
# print (str1.translate(trantab, 'xm'))


str1 = "this is str1ing example....wow!!!";
print("total characters in str1ing: "+str(len(str1)))
print (str1.zfill(40))
print (str1.zfill(50))
print("string repeat using *: "+("*"*10))


# usage of zfill in number foramtting and other formatting options
n = 4
print("using zfill: "+str(n).zfill(3))
print('%03d' % n)
print(format(4, '03')) # python >= 2.6
print('{0:03d}'.format(4))  # python >= 2.6
print('{foo:03d}'.format(foo=4))  # python >= 2.6
print('{:03d}'.format(4))  # python >= 2.7 + python3
print('{0:03d}'.format(4))  # python 3



