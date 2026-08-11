from player import Player


def mostrar_menu():
    print("=" * 40)
    print("=      As profundezas de Moria ")
    print("=" * 40)
    print("1 - Novo Jogo")
    print("2 - Sair")


def iniciar_jogo():
    print("\nBem-vindo, aventureiro!")
    nome = input("Digite o nome do seu personagem: ")

    jogador = Player(nome)

    print(f"\nBem-vindo(a), {jogador.nome}!")
    print("Sua aventura começa agora...\n")

    while True:
        print("-" * 40)
        print("1 - Explorar")
        print("2 - Ver status")
        print("3 - Sair")
        print("-" * 40)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nVocê segue por um corredor escuro...")
            print("Ainda não há nada por aqui.\n")

        elif opcao == "2":
            jogador.mostrar_status()

        elif opcao == "3":
            print("\nAté a próxima aventura!")
            break

        else:
            print("\nOpção inválida!\n")


def main():
    while True:
        mostrar_menu()

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            iniciar_jogo()

        elif opcao == "2":
            print("Encerrando...")
            break

        else:
            print("\nOpção inválida!\n")


if __name__ == "__main__":
    main()