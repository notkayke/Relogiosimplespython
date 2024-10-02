from tkinter import *
from time import strftime

def atualizar_relogio():
    horario_atual = strftime("%H:%M:%S %p")
    data_atual = strftime("%d/%m/%Y")
    rotulo_relogio.config(text=horario_atual)
    rotulo_data.config(text=data_atual)
    rotulo_relogio.after(1000, atualizar_relogio)

janela = Tk()
janela.title("Relógio Digital Simples")
janela.geometry("300x100")
janela.attributes("-topmost", True)

rotulo_relogio = Label(
    janela,
    font=("Arial", 40, "bold"),
    background="black",
    foreground="green"
)
rotulo_relogio.pack(anchor="center")

rotulo_data = Label(
    janela,
    font=("Arial", 20, "bold"),
    background="black",
    foreground="green"
)
rotulo_data.pack(anchor="center")

atualizar_relogio()

janela.mainloop()
