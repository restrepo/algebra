def exer_mult(expression):
    import sympy as sym
    from sympy import init_printing; init_printing() 
    from IPython.display import display, Math, Latex
    a, b, c, x, y, z = sym.symbols("a b c x y z")
    expression=str(expression)
    evexpr=sym.expand(eval(expression))
    print 'Expand the expression:'
    display(Math(str(expression).replace('**','^').replace('*','')))
    result=raw_input()
    if evexpr== eval(result): 
        print "Good job! Final result:"
        return eval(result)
    else:
        print('WRONG!!!\nRight result:')
        return sym.expand(eval(expression))
    
def jointerms(terms):
    rb='('
    for i in terms[0]:
        if i:
            rb=rb+i#'\red{%d}' %i        
    rb=rb+')('
    for i in terms[1]:
        if i:
            rb=rb+i        
    rb=rb+')'
    return rb
def exer_mult_step(expression):
    import re
    import sympy as sym
    from sympy import init_printing; init_printing() 
    from IPython.display import display, Math, Latex
    a, b, c, x, y, z = sym.symbols("a b c x y z")
    expression=str(expression)
    evexpr=sym.expand(eval(expression))
    print 'Expand the following expression step by step:'
    display(Math(str(expression).replace('**','^').replace('*','')))
    print 'Multiply ALL the monomials:'
    factor=re.split('\)\s*\*\s*\(',str(expression))
    refactor=[ re.split('\(|\)',factor[i])[1-i] for i in range(len(factor))]
    terms=[ re.split(':',re.sub('\s*(\+|\-)\s*',r':\1',refactor[i])) for i in range(len(refactor)) ]
    expandednr=''
    for i in range(len(terms[0])):
    #nci=''
        if terms[0][i]:
            nci=terms[0][i]
            terms[0][i]=r'{\color{red}{%s}}' %terms[0][i]
            for j in range(len(terms[1])):
            #ncj=''
                if terms[1][j]:
                    ncj=terms[1][j]
                    terms[1][j]=r'\color{red}{%s}' %terms[1][j]
        
                    l=jointerms(terms)
                    display(Math(l.replace('**','^').replace('*','')))
                    terms[1][j]=ncj
                    newterm=raw_input()
                    if re.search('^-',newterm):
                        newterm=newterm
                    else:
                        newterm='+'+newterm
                    expandednr=expandednr+newterm
                    expandednr=re.sub('^\+','',expandednr)
                
            terms[0][i]=nci  
        
    print 'Reduce the expression:' 
    display(Math(expandednr.replace('**','^').replace('*','')))
    result=raw_input()
    if evexpr== eval(result): 
        print "Good job!, final result:"
        return eval(result)
        
    else:
        print('WRONG!!!\nRight result:')
        return sym.expand(expression)
    
def exer_mult_step_old(expression):
    import re
    import sympy as sym
    from sympy import init_printing; init_printing() 
    from IPython.display import display, Math, Latex
    a, b, c, x, y, z = sym.symbols("a b c x y z")
    expression=str(expression)
    evexpr=sym.expand(eval(expression))
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
           