import glob
import os
import sys 

# Altere esta variável para o caminho da pasta onde estão os seus 800+ arquivos
PASTA_HTML = "arquivos" 

# Nome do arquivo final que será criado
ARQUIVO_SAIDA = "consolidado.txt"

DELIMITADOR = "\n\n=================== novo arquivo ===================\n\n"


ENCODING_PADRAO = 'utf-8'


def consolidar_arquivos():
    """
    Função principal que encontra, lê e consolida os arquivos HTML.
    """
    
    padrao_busca = os.path.join(PASTA_HTML, "*.html")
    
    lista_arquivos_html = glob.glob(padrao_busca)
    
    lista_arquivos_html.sort()

    total_arquivos = len(lista_arquivos_html)

    if total_arquivos == 0:
        print(f"Atencao: Nenhum arquivo .html foi encontrado na pasta '{PASTA_HTML}'.")
        print("Verifique se o caminho em 'PASTA_HTML' está correto.")
        return

    print(f"Iniciando a consolidacao...")
    print(f"Encontrados {total_arquivos} arquivos HTML para processar.")

    try:

        with open(ARQUIVO_SAIDA, 'w', encoding=ENCODING_PADRAO) as f_saida:
            
            for i, caminho_arquivo in enumerate(lista_arquivos_html):
                
                nome_arquivo = os.path.basename(caminho_arquivo)
                print(f"Processando ({i + 1}/{total_arquivos}): {nome_arquivo}")

                if i > 0:
                    f_saida.write(DELIMITADOR)
                
                try:
                    with open(caminho_arquivo, 'r', encoding=ENCODING_PADRAO, errors='ignore') as f_entrada:
                        
                        conteudo_html = f_entrada.read()
                        
                        f_saida.write(conteudo_html)
                
                except Exception as e_leitura:
                    print(f"  -> ERRO ao ler o arquivo {nome_arquivo}: {e_leitura}")
                    f_saida.write(f"\n!! ERRO AO PROCESSAR O ARQUIVO {nome_arquivo}: {e_leitura} !!\n")

        # Fim do loop
        print(f"\n--- SUCESSO! ---")
        print(f"Todos os arquivos foram consolidados em '{ARQUIVO_SAIDA}'.")

    except FileNotFoundError:
        print(f"\n--- ERRO CRÍTICO ---")
        print(f"A pasta de origem '{PASTA_HTML}' não foi encontrada.")
        print("Por favor, verifique o caminho e tente novamente.")
    
    except Exception as e_escrita:
        print(f"\n--- ERRO CRÍTICO ---")
        print(f"Ocorreu um erro ao escrever o arquivo de saída: {e_escrita}")

if __name__ == "__main__":
    consolidar_arquivos()