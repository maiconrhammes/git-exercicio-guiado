alunos = [
    {"nome": "Ana", "nota1": 7, "nota2": 8},
    {"nome": "Carlos", "nota1": 5, "nota2": 6},
    {"nome": "Bruna", "nota1": 9, "nota2": 10}
]

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def mostrar_relatorio():
    print("=== RELATORIO DE ALUNOS ===")
    for a in alunos:
        media = calcular_media(a["nota1"], a["nota2"])
        if media >= 7:
            status = "Aprovado"
        elif media >= 4:
            status = "Recuperacao"
        else:
            status = "Reprovado"

        print("Nome:", a["nome"])
        print("Nota 1:", a["nota1"])
        print("Nota 2:", a["nota2"])
        print("Media 1:", media)
        print("Status:", status)
        print("----------------------")

def main():
    mostrar_relatorio()

if __name__ == "__main__":
    main()
