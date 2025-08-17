# analisador_linkedin.py  — versão “mais inteligente”
# Evy: aceita variações (com/sem acento e frases parecidas)

PALAVRAS_CHAVE = {
    "Python": ["python"],
    "SQL": ["sql"],
    "GitHub": ["github", "git hub"],
    "Cibersegurança": ["cibersegurança", "ciberseguranca", "segurança da informação"],
    "Análise de Sistemas": [
        "análise de sistemas", "analise de sistemas",
        "análise e desenvolvimento de sistemas", "ads"
    ],
}

def normalizar(texto: str) -> str:
    """Deixa tudo minúsculo e sem acentos para comparar melhor."""
    import unicodedata
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto

def analisar_perfil(caminho_arquivo: str = "perfil.txt"):
    # Tenta abrir o arquivo com o texto do seu perfil
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo_original = f.read()
    except FileNotFoundError:
        print("⚠️ Arquivo 'perfil.txt' não encontrado! Crie esse arquivo com seu texto do LinkedIn.")
        return

    conteudo = normalizar(conteudo_original)

    print("📝 Analisando perfil...\n")
    pontos = 0

    for chave, variantes in PALAVRAS_CHAVE.items():
        # normaliza cada variante para comparar com o texto normalizado
        variantes_norm = [normalizar(v) for v in variantes]
        if any(v in conteudo for v in variantes_norm):
            print(f"✅ Palavra-chave encontrada: {chave}")
            pontos += 1
        else:
            print(f"❌ Faltou mencionar: {chave}")

    print("\n⭐ Resultado final:")
    total = len(PALAVRAS_CHAVE)
    if pontos == total:
        print("Excelente! Seu perfil está bem otimizado 🚀")
    elif pontos >= total - 1:
        print("Muito bom! Falta pouco para ficar perfeito.")
    elif pontos >= 3:
        print("Bom, mas pode melhorar. Adicione mais termos estratégicos!")
    else:
        print("Perfil fraco, falta incluir várias palavras-chave importantes.")

if __name__ == "__main__":
    analisar_perfil()