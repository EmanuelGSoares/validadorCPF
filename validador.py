from tkinter import *

def somarPrimeiroNumero(cpf):
    cpfSomado = 0
    ctrl = 1
    for i in cpf[:9]:
        cpfSomado += (int(i) * ctrl)
        ctrl += 1
    restoSomaPN = cpfSomado % 11
    if (restoSomaPN == 10):
        restoSomaPN = 0
    return restoSomaPN

def somarSegundoNumero(cpf):
    cpfSomado = 0
    ctrl = 0
    for i in cpf[:10]:
        cpfSomado += (int(i) * ctrl)
        ctrl += 1
    restoSomaSN = cpfSomado % 11
    if (restoSomaSN == 10):
        restoSomaSN = 0
    return restoSomaSN


def resultadoFinal(cpf):

    global labelTroca

    if labelTroca:
        labelTroca.destroy()

    if (not cpf.isnumeric()):
        labelTroca = Label(window, fg=cor1, text=f"O CPF {cpf} não é numérico!")
    elif (len(cpf) < 11):
        labelTroca = Label(window, fg=cor1, text=f"O CPF {cpf} é Inválido (curto)!")
    elif (len(cpf) > 11):
        labelTroca = Label(window, fg=cor1, text=f"O CPF {cpf} é Inválido (longo)!")
    elif (somarPrimeiroNumero(cpf) == int(cpf[9]) and somarSegundoNumero(cpf) == int(cpf[10])):
        labelTroca = Label(window, fg=cor0, text=f"O CPF {cpf} é Válido!")
    else:
        labelTroca = Label(window, fg=cor1, text=f"O CPF {cpf} é Inválido!")
    labelTroca.grid(column=0, row=3, padx=(100,0), pady=5)
    

def enviar():
    cpf = cpfInput.get()
    resultadoFinal(cpf)



cor0 = "#59b356"  
cor1 = "#f04141"
labelTroca = None


################# Criando a janela principal ##############

window = Tk()
window.resizable(0, 0)
window.title("Validador de CPF")
window.geometry("400x200")
window.resizable(False, False)


label1 = Label(window, text="Validador de CPF")
label1.grid(column=0, row=1, padx=(100,0), pady=(10,5))

label2 = Label(window, text="Digite o CPF (sem pontos e traço)")
label2.grid(column=0, row=2, padx=(100,0), pady=5)

cpfInput = Entry(window, width=20,)
cpfInput.grid(column=0, row=4, sticky=NSEW, padx=(100,0), pady=(10))

botaoEnviar = Button(window, text="Validar", command=enviar)
botaoEnviar.grid(column=0, row=5, padx=(50,0), pady=(20))

botaoSair = Button(window, text="Sair", command=exit)
botaoSair.grid(column=0, row=5, padx=(150,0))


window.mainloop()