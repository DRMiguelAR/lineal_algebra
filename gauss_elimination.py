import sympy
from sympy import *
from IPython.display import display, Math

def custom_latex_printer(exp,**options):
    from google.colab.output._publish import javascript
    url = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js?config=default"
    javascript(url=url)
    return printing.latex(exp,**options)
lp = custom_latex_printer
sympy.init_printing(use_latex="mathjax",latex_printer=custom_latex_printer)

class Matriz:
    def __init__(self, *args):
        if len(args)>1:
            self.M= sympy.Matrix(args)
        self.imprimir()
    def imprimir(self):
        display(self.M)
    def multiplicar_fila(self, fila, factor):
        fila-=1
        self.M= self.M.elementary_row_op(op="n->kn",row=fila,k=Rational(factor))
        return self.M
    def cambiar_filas(self, fila1, fila2):
        fila1-=1
        fila2-=1
        self.M= self.M.elementary_row_op(op="n<->m",row1=fila1, row2=fila2)
        return self.M
    def sumar_multiplo(self, fila1, fila2, factor):
        fila1-=1
        fila2-=1
        self.M= self.M.elementary_row_op(op="n->n+km",row1=fila1, row2=fila2, k=Rational(factor)) 
        return self.M
    
def Vector(*args):
    return args
