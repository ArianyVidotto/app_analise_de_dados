import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados (assumindo que o arquivo CSV está no mesmo diretório que o script)
csv_file = 'seu_arquivo.csv'
df = pd.read_csv(csv_file)

def menu():
    print("Escolha uma opção:")
    print("1. Exibir estatísticas descritivas")
    print("2. Plotar gráfico de dispersão")
    print("3. Sair")

def exibir_estatisticas():
    print(df.describe())

def plotar_grafico():
    col_x = input("Digite o nome da coluna para o eixo X: ")
    col_y = input("Digite o nome da coluna para o eixo Y: ")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=col_x, y=col_y)
    plt.title('Gráfico de Dispersão')
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.show()

while True:
    menu()
    opcao = input("Opção: ")

    if opcao == '1':
        exibir_estatisticas()
    elif opcao == '2':
        plotar_grafico()
    elif opcao == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
