import tkinter as tk
from tkinter import messagebox
from components import baixar_publicacoes, baixar_stories

# Função para executar o processo de scraping e download
def executar_scraping():
    usuario = entrada_usuario.get()
    
    try:
        baixar_publicacoes(usuario)
        baixar_stories(usuario)
        messagebox.showinfo("Concluído", "O processo de scraping e download foi concluído com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Configuração da interface gráfica
app = tk.Tk()
app.title("Instagram Scraper")
app.geometry("500x300")
app.configure(bg='#F0F0F0')

# Estilos
estilo_fonte = ("Helvetica", 12)
estilo_fonte_titulo = ("Helvetica", 16, "bold")
cor_fundo = "#F0F0F0"
cor_borda = "#333333"
cor_fundo_botao = "#4CAF50"
cor_texto_botao = "#FFFFFF"

# Frame principal
frame_principal = tk.Frame(app, bg=cor_fundo, bd=2, relief="groove")
frame_principal.pack(padx=20, pady=20, fill="both", expand=True)

# Título
label_titulo = tk.Label(frame_principal, text="Instagram Scraper", font=estilo_fonte_titulo, bg=cor_fundo)
label_titulo.pack(pady=10)

# Instrução
label_instrucao = tk.Label(frame_principal, text="Digite o @ do usuário do Instagram:", font=estilo_fonte, bg=cor_fundo)
label_instrucao.pack(pady=5)

# Entrada de texto
entrada_usuario = tk.Entry(frame_principal, width=40, font=estilo_fonte, bd=2, relief="solid")
entrada_usuario.pack(pady=10)

# Botão de execução
botao_executar = tk.Button(frame_principal, text="Executar", font=estilo_fonte, bg=cor_fundo_botao, fg=cor_texto_botao, command=executar_scraping)
botao_executar.pack(pady=20)

# Rodapé
label_rodape = tk.Label(frame_principal, text="Desenvolvido por [Seu Nome]", font=("Helvetica", 10), bg=cor_fundo)
label_rodape.pack(side="bottom", pady=10)

app.mainloop()
