def memorizar():
    import ipywidgets as widgets
    from IPython.display import display, Math, Latex, clear_output

    button = widgets.Button(description="Borrar tabla")

    def on_button_clicked(b):
        clear_output()

    Tabla=widgets.Text(
            description='Memorize la tabla del:'
    )

    display(widgets.HTML('¿Cual tabla, del 1 al 10, desea memorizar?'))


    display(Tabla)
    def handle_submit(sender):
        N=Tabla.value
        for i in range(1,12):
            if i<11:
                display(widgets.HTML('{} x {} = {}'.format(N,i,int(N)*i)))

            if i==11:
                display(button)
                display(widgets.HTML('''y <b>practique</b> en la siguiente celda con <code>Shift+Enter</code></b>
                            '''))
                button.on_click(on_button_clicked)


    Tabla.on_submit(handle_submit) 
    #clear_output()
    return Tabla

def practicar(N):
    import ipywidgets as widgets
    from IPython.display import display, Math, Latex, clear_output

    display(widgets.HTML('<b>Practique aquí</b>'))
    error=False
    #N=Tabla.value
    tb=[];tb.append(0)
    for i in range(1,11):
        tb.append( widgets.Text(description='{} x {} ='.format(N,i)) )
        display(tb[i])

    button = widgets.Button( description="Comprobar")

    def on_button_clicked(b):
        error=False
        for i in range(1,11):
            if int(tb[i].value)!=int(N)*i:
                error=True
                display(widgets.HTML( '<h1>Mal!: <font color="red"> ' +N+' x {} = {}</font>,  no '.format(i,int(N)*i)+ tb[i].value+'</h1>'  ) )
        display(widgets.HTML( '<hr>' ) )
        if not error:
            display(widgets.HTML('''<h1>¡Felicitaciones!: sabes la tabla del {} </h1> 
                                    <h2> <font color="blue"> !Buen trabajo!</font></h2><hr>'''.format(N)))    

    display(button)
    button.on_click(on_button_clicked)    
