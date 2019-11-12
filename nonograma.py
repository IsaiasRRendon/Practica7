# Nonograma


import pygtk
pygtk.require('2.0')
import gtk
import random

jugador_on = 0

class Nonograma:
    # Funcion que checa si el nonograma fue completado con exito
    def callback(self, widget, valor_correcto_celda, total_on):
        
        global jugador_on
    
        valor_celda_jugador = (0, 1)[widget.get_active()]

        if valor_celda_jugador == valor_correcto_celda:
            # Incrementa jugador cuando checa una celda
            if valor_celda_jugador == 1:
                jugador_on += 1
        else:
            # Decrementa jugador cuando no se checa una celda
            if valor_correcto_celda == 1 and valor_celda_jugador == 0:
                jugador_on -= 1

        # Mensaje de completado
        if jugador_on == total_on:
            dialog = gtk.MessageDialog(
                parent         = self.window,
                flags          = gtk.DIALOG_DESTROY_WITH_PARENT,
                type           = gtk.MESSAGE_INFO,
                buttons        = gtk.BUTTONS_OK,
                message_format = "Has completado el Nonograma con exito\n\nTerminar dando click en 'OK'\n\nSaludos!\n"
            )

            dialog.set_title('Felicidades')
            dialog.connect('respuesta', lambda dialog, respuesta: gtk.main_quit())
    
            dialog.show()

        return jugador_on

    # Cierra el programa
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    # Dibuja los widgets
    def __init__(self, grid):

        total_on  = 0
        jugador_on = 0
        cuenta_actual     = 0
        cuenta_actual_col = []
        cuenta_actual_ren = []
        total_cuentas_col    = []
        total_cuentas_ren    = []

        # Cicla todas las celdas
        for i in range(10):
            cuenta_actual = 0

            # Cicla todas las celdas en un renglon
            for j in grid[i]:

                # Incrementa los contadores
                if j == 1:
                    cuenta_actual += 1
                    total_on      += 1
                # Agrega el total a la lista y empieza de nuevo
                else:
                    if cuenta_actual != 0:
                        cuenta_actual_ren.append(cuenta_actual)

                    cuenta_actual = 0

            # Guarda la cuenta si la celda final no es cero
            if cuenta_actual != 0:
                cuenta_actual_ren.append(cuenta_actual)

            total_cuentas_ren.append(cuenta_actual_ren)
            cuenta_actual_ren = []
            cuenta_actual     = 0

            # Cicla todas las celdas en una columna
            for j in range(10):
                # Incrementa los contadores
                if grid[j][i] == 1:
                    cuenta_actual += 1
                # Agrega el total a la lista y empieza de nuevo
                else:
                    if cuenta_actual != 0:
                        cuenta_actual_col.append(cuenta_actual)

                    cuenta_actual = 0

            # Guarda la cuenta si la celda final no es cero
            if cuenta_actual != 0:
                cuenta_actual_col.append(cuenta_actual)

            total_cuentas_col.append(cuenta_actual_col)
            cuenta_actual_col = []

        