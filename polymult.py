def exer_mult(expression):
    import sympy as sym
    from sympy import init_printing; init_printing() 
    from IPython.display import display, Math, Latex
    a, b, c, x, y, z = sym.symbols("a b c x y z")
    evexpr=sym.expand(eval(expression))
    print 'Expand the expression:'
    display(Math(str(expression).replace('**','^').replace('*','')))
    result=raw_input()
    if evexpr== eval(result): 
        print "Good job! Final result:"
        return eval(result)
    else:
        print('WRONG!!!\nRight result:')
        return sym.expand(expression)
    
def exer_mult_step(expression):
    import re
    import sympy as sym
    from sympy import init_printing; init_printing() 
    from IPython.display import display, Math, Latex
    a, b, c, x, y, z = sym.symbols("a b c x y z")
    evexpr=sym.expand(eval(expression))
    expression=str(expression)
    print 'Expand the following expression step by step:'
    display(Math(str(expression).replace('**','^').replace('*','')))
    print 'Multiply ALL the monomials:'
    factor=re.split('\)\s*\*\s*\(',str(expression))
    refactor=[ re.split('\(|\)',factor[i])[1-i] for i in range(len(factor))]
    terms=[ re.split(':',re.sub('\s*(\+|\-)\s*',r':\1',refactor[i])) for i in range(len(refactor)) ]
    expandednr=''
    for i in terms[0]:
        for j in terms[1]:
            if i and j: #mo empty strings
                print '(%s)*(%s)' %(i,j)
                newterm=raw_input()
                if re.search('^-',newterm):
                    newterm=newterm
                else:
                    newterm='+'+newterm
                expandednr=expandednr+newterm
                expandednr=re.sub('^\+','',expandednr)
    print 'Reduce the expression:' 
    display(Math(expandednr.replace('**','^').replace('*','')))
    result=raw_input()
    if evexpr== eval(result): 
        print "Good job!, final result:"
        return eval(result)
        
    else:
        print('WRONG!!!\nRight result:')
        return sym.expand(expression)
           