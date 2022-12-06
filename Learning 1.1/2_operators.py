from cgi import print_form


a =1
b=99
 #Airthmetic Operators(+,-,/,*)
print("SUM IS ", a+b)
print("SUB IS ", a-b)
print("MUL IS ", a*b)
print("DIV IS ", a/b)

#Assignment Opeartors(=,+=,-=,/=,*=)
A= 5
A+=1
A-=2
A/=2
A*=5
print(round(A))

#Comparison Operators(return boolen (True/False)
i = 22>22
i = 22<22
i = 22==22
i = 22>=22
i = 22<=22
i = 22!=22
print(i)
 
#Logical Operators
bool1 = True
boll2= False
print("THe value of bool1 and bool2 is ",(bool1 and boll2))
print("THe value of bool1 or bool2 is ",(bool1 or boll2))
print("THe value of  not boll2 is ",(not boll2))