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
        self.imprimir()
        return self.M
    def cambiar_filas(self, fila1, fila2):
        fila1-=1
        fila2-=1
        self.M= self.M.elementary_row_op(op="n<->m",row1=fila1, row2=fila2)
        self.imprimir()
        return self.M
    def sumar_multiplo(self, fila1, fila2, factor):
        fila1-=1
        fila2-=1
        self.M= self.M.elementary_row_op(op="n->n+km",row1=fila1, row2=fila2, k=Rational(factor)) 
        self.imprimir()
        return self.M
    
def Vector(*args):
    return args

v1=Vector(1,0,0)
v2=Vector(0,1,0)
v3=Vector(0,0,1)
matriz= Matriz(v1,v2,v3)

def mf(fila, factor):
    global matriz
    matriz.multiplicar_fila(fila,factor)

def cf(fila1, fila2):
    global matriz
    matriz.cambiar_filas(fila1, fila2)

def cl(fila1, fila2, factor):
    global matriz
    matriz.sumar_multiplo(fila1, fila2, factor)
