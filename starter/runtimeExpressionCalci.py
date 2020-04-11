# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

print("method1")
num=9
expr="a+aa+aaa+aaaa"
var2replace='a'
new_expr=expr.replace(var2replace,str(num))
print(expr,"replaced values are",new_expr,"calci value",eval(new_expr))

print("method2")
a = 9
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print(n1+n2+n3+n4)
