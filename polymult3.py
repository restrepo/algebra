def fix_text(text,**kwargs):
    import re
    level=1
    try:
        level=kwargs['level']
    except:
        pass

    vars='abcxyz' #TODO: check sympy for defined symbols
    if level==0: # replace x vy *
        text=text.replace('x','*') 
        
    text=re.sub('([0-9])([{}])'.format(vars),r'\1*\2',text)
    text=re.sub('([0-9])(\()'.format(vars),r'\1*\2',text)

    return text

def fix_latex_output(text,**kwargs):
    '''
    The input text can be a string or a synmpy object.
    A sympy object accept str conersion!
    '''
    text=fix_text(text,**kwargs)
    level=1
    try:
        level=kwargs['level']
    except:
        pass

    text=str(text).replace('**','^')
    if level==0:
        text=text.replace('*',r'\times ')
    return text


def check_result(expression,result,**kwargs):
    import subprocess
    import sympy as sym
    from sympy import init_printing; init_printing() 
    from IPython.display import display, Math, Latex, HTML

    level=1
    try:
        level=kwargs['level']
    except:
        pass
    
    if level==0:
        a, b, c, y, z = sym.symbols("a b c y z")
    else:
        a, b, c, x, y, z = sym.symbols("a b c x y z")


    expression=fix_text(expression,**kwargs)
    result=fix_text(result,**kwargs)

    tex_expr=fix_latex_output(expression,**kwargs)
    display(HTML(r'<hr><b>Comprobando</b>'))
    #print('Comprobando: ',end='')
    display(Math( tex_expr  ))
    display(HTML(r'<hr>'))
    right_result=sym.expand(  expression.replace('^','**') )
    if right_result==sym.expand( result.replace('^','**') ):
        display(Math(r'{\huge\text{ ¡Correcto!}}, \large\text{  ¡buen trabajo!}'))
        display(Math(  fix_latex_output( str(right_result),**kwargs ) ))
        try:
            kk=subprocess.Popen('aplay good.wav'.split(),stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE).communicate()
        except:
            pass

        return right_result
    else:
        display(Math(r'{\large\text{ Mal}}, \large\text{ el resultado correcto es:}'))
        display(Math(  fix_latex_output( str(right_result),**kwargs ) ))
        try:
            kk=subprocess.Popen('aplay error.wav'.split(),stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE).communicate()
        except:
            pass

        return right_result
    


def operacion(**kwargs):
    '''
    Options:
     level=N
     N=0: x and ^ are accepted.
     N=1: ^ is accepted
    '''
    import re
    import subprocess
    import sympy as sym
    from sympy import init_printing; init_printing() 
    from IPython.display import display, Math, Latex
    level=1
    try:
        level=kwargs['level']
    except:
        pass
    
    if level==0:
        a, b, c, y, z = sym.symbols("a b c y z")
    else:
        a, b, c, x, y, z = sym.symbols("a b c x y z")
        
    display(Math(r'\large\text{ Escriba una operación:}'))
    expression=input()

    tex_expr=fix_latex_output(expression,**kwargs)
    display(Math(  tex_expr  ))
    display(Math(r'\large\text {Escriba el resultado:}'))
    result=input()

    return check_result(expression,result,**kwargs)
    

def operacion_widget(level=1):
    import ipywidgets as widgets
    from IPython.display import display, Math, Latex # Used to display widgets in the notebook

    #display(Math(r'\large\text{ Escriba una operación:}'))
    expression=widgets.Text(
        #description='Esciba una operación:'
        )
    result    =widgets.Text(
        #description='Escriba el resultado:'
        )
    display( widgets.HTMLMath(
        #value=r"Some math and <i>HTML</i>: \(x^2\) and $$\frac{x+1}{x-1}$$",
        #placeholder='Some HTML',
        description='Escriba una <b>operación:<b/>',
    ) )
    display(expression)
    #display(Math(r'\large\text {Escriba el resultado:}'))
    display( widgets.HTMLMath(
        value=r"y pulse <code>Enter</code>",
        #placeholder='Some HTML',
        description='Escriba el <b>resultado:<b/>',
    ) )
    display(result)
    def handle_submit(sender):
        check_result(expression.value,result.value,level=level)

    return result.on_submit(handle_submit)    

def exer_mult(expression):
    import sympy as sym
    from sympy import init_printing; init_printing() 
    from IPython.display import display, Math, Latex
    a, b, c, x, y, z = sym.symbols("a b c x y z")
    expression=str(expression)
    evexpr=sym.expand(eval(expression.replace('^','**')))
    print ('Expand the expression:')
    display(Math(str(expression).replace('**','^').replace('*','')))
    result=input()
    if evexpr== eval(result.replace('^','**')): 
        print ("Good job! Final result:")
        return eval(result)
    else:
        print('WRONG!!!\nRight result:')
        return sym.expand(eval(expression.replace('^','**')))
    
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
    evexpr=sym.expand(eval(expression.replace('^','**')))
    print ('Expand the following expression step by step:')
    display(Math(str(expression).replace('**','^').replace('*','')))
    print ('Multiply ALL the monomials:')
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
                    newterm=input()
                    if re.search('^-',newterm):
                        newterm=newterm
                    else:
                        newterm='+'+newterm
                    expandednr=expandednr+newterm
                    expandednr=re.sub('^\+','',expandednr)
                
            terms[0][i]=nci  
        
    print ('Reduce the expression:' )
    display(Math(expandednr.replace('**','^').replace('*','')))
    result=input()
    if evexpr== eval(result.replace('^','**')): 
        print ("Good job!, final result:")
        return eval(result.replace('^','**'))
        
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
    print ('Expand the following expression step by step:')
    display(Math(str(expression).replace('**','^').replace('*','')))
    print ('Multiply ALL the monomials:')
    factor=re.split('\)\s*\*\s*\(',str(expression))
    refactor=[ re.split('\(|\)',factor[i])[1-i] for i in range(len(factor))]
    terms=[ re.split(':',re.sub('\s*(\+|\-)\s*',r':\1',refactor[i])) for i in range(len(refactor)) ]
    expandednr=''
    for i in terms[0]:
        for j in terms[1]:
            if i and j: #mo empty strings
                print ( '(%s)*(%s)' %(i,j) )
                newterm=input()
                if re.search('^-',newterm):
                    newterm=newterm
                else:
                    newterm='+'+newterm
                expandednr=expandednr+newterm
                expandednr=re.sub('^\+','',expandednr)
    print ( 'Reduce the expression:' )
    display(Math(expandednr.replace('**','^').replace('*','')))
    result=input()
    if evexpr== eval(result): 
        print ( "Good job!, final result:")
        return eval(result)
        
    else:
        print('WRONG!!!\nRight result:')
        return sym.expand(expression)
           
