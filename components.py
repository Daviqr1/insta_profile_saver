import os
import instaloader
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

INSTAGRAM_USER = os.getenv('INSTAGRAM_USER')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

# Função para criar pastas se não existirem
def criar_pasta(nome):
    if not os.path.exists(nome):
        os.makedir(nome)

# Função para configurar o instaloader e fazer login
def configurar_instaloader():
    L = instaloader.Instaloader()
    try:
        L.login(INSTAGRAM_USER, INSTAGRAM_PASSWORD)
    except instaloader.exceptions.BadCredentialsException:
        print("Credenciais inválidas! Verifique seu usuário e senha.")
        raise
    except Exception as e:
        print(f"Ocorreu um erro durante o login: {e}")
        raise
    return L

# Função para baixar publicações usando instaloader
def baixar_publicacoes(perfil):
    L = configurar_instaloader()
    posts = instaloader.Profile.from_username(L.context, perfil).get_posts()
    criar_pasta('publicacoes')
    for post in posts:
        L.download_post(post, target='publicacoes')

# Função para baixar stories usando instaloader
def baixar_stories(perfil):
    L = configurar_instaloader()
    profile = instaloader.Profile.from_username(L.context, perfil)
    criar_pasta('stories')
    for story in L.get_stories(userids=[profile.userid]):
        for item in story.get_items():
            L.download_storyitem(item, target='stories')
