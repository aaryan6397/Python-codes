#1,4,9,16,25,36,----- ,2500 without terms --> pending
#1,8,27,64,125,----- ,27000 without terms --> pending
#4,-8,12,-16,20,-24,----- ,-800,804 without terms


# wrost code ever becuse extra variable is used to store the value of x and sign which is not a good practice.
x=4
sign=1
while(x<=804):
    print(x*sign, end= ",")
    sign = sign*-1
    x = x + 4

#easy solution in the way of if else statement
x = 4
while(x<=804):
    if(x%8==0):
        print(-x,end=",")
    else:
        print(x,end=",")
    x = x+4

#output
#4,-8,12,-16,20,-24,28,-32,36,-40,44,-48,52,-56,60,-64,68,-72,76,-80,84,-88,92,-96,100,-104,108,-112,116,-120,124,-128,132,-136,140,-144,148,-148,156,-160,164,-168,172,-172,180,-184,188,-188,196,-200,204,-204,212,-216,220,-220,228,-232,236,-236,244,-248,252,-252,260,-264,268,-268,276,-280,284,-284,292,-296,300,-300,...804