import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import re

def gerar_qrcode():
    texto = entrada_texto.get("1.0", tk.END).strip()

    if not texto:
        messagebox.showwarning("Aviso", "Por favor, insira algum texto para gerar o QR Code")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    img.save("qrcode.png")

    exibir_qrcode("qrcode.png")


def exibir_qrcode(caminho_imagem):

    imagem= Image.open(caminho_imagem)

    imagem= imagem.resize((200, 200), Image.LANCZOS)

    imagem_tk = ImageTk.PhotoImage(imagem)

    label_imagem.config(image=imagem_tk)

    label_imagem.image = imagem_tk

def sanitize_filename(text):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', text)

def baixar_qrcode():
    texto = entrada_texto.get("1.0", tk.END).strip()

    if not texto:
        messagebox.showwarning("Aviso", "Por favor, insira algum texto para gerar o QR Code")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(texto)

    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    nome_arquivo = sanitize_filename(texto)[:50]

    caminho_arquivo = filedialog.asksaveasfilename(
        initialfile=nome_arquivo,
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")]
    )

    if caminho_arquivo:
        img.save(caminho_arquivo)

        messagebox.showinfo("Sucesso", f"O QR Code foi salvo em {caminho_arquivo}")


janela_principal = tk.Tk()

janela_principal.title("Gerador de QR Code")

janela_principal.configure(bg="white")

largura_janela = 600

altura_janela = 400

largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()

posicao_x = (largura_tela // 2) - (largura_tela // 2)
posicao_y = (altura_tela // 2) - (altura_janela // 2)

janela_principal.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

frame_entrada = tk.Frame(janela_principal, bg= "white")
frame_entrada.pack(pady=10)
label_entrada = tk.Label(frame_entrada,
                         text="Texto para QR Code:",
                         bg="white",
                         font=('Helvetica', 12))

label_entrada.pack()

entrada_texto = tk.Text(frame_entrada,
                      height=4,
                      width=50,
                      font=('Helvetica', 12))

entrada_texto.pack(pady=5)

frame_botoes = tk.Frame(janela_principal, bg="white")
frame_botoes.pack(pady=20)

botao_gerar = tk.Button(frame_botoes,
                        text="Gerar QR Code",
                        command=gerar_qrcode,
                        font=('Helvetica', 12))

botao_gerar.pack(side=tk.LEFT, padx=10)

botao_baixar = tk.Button(frame_botoes,
                        text="Baixar QR Code",
                        command=baixar_qrcode,
                        font=('Helvetica', 12))

botao_baixar.pack(side=tk.LEFT, padx=10)

label_imagem = tk.Label(janela_principal, bg="white")
label_imagem.pack(pady=10)

janela_principal.mainloop()