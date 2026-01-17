# 📁 Script Auto Varrer HTML

Um script Python simples e eficiente para **consolidar múltiplos arquivos HTML** em um único arquivo texto, facilitando a análise, backup ou processamento em lote.

## 🚀 Funcionalidades

- ✅ **Busca automática** por todos os arquivos `.html` em uma pasta
- 📋 **Consolidação ordenada** de arquivos (ordenação alfabética)
- 🛡️ **Tratamento de erros robusto** para arquivos corrompidos
- 📊 **Progresso em tempo real** durante o processamento
- 🔤 **Suporte completo a UTF-8** para caracteres especiais
- 📄 **Delimitadores claros** entre arquivos no resultado final

## 📂 Estrutura do Projeto

```
script-auto-varrer-html/
├── 📁 arquivos/          # Pasta com arquivos HTML (configurável)
│   └── 01.html          # Exemplos de arquivos HTML
├── 📄 script.py         # Script principal
├── 📄 consolidado.txt   # Arquivo gerado (resultado)
└── 📖 README.md         # Este arquivo
```

## ⚙️ Configuração

Antes de executar o script, ajuste as variáveis no início do arquivo `script.py`:

```python
# Caminho para a pasta com arquivos HTML
PASTA_HTML = "arquivos"

# Nome do arquivo de saída
ARQUIVO_SAIDA = "consolidado.txt"
```

## 🔧 Como Usar

### 1. Preparar o ambiente

```bash
# Clone ou baixe este repositório
git clone <url-do-repositorio>
cd script-auto-varrer-html
```

### 2. Organizar arquivos

- Coloque seus arquivos `.html` na pasta `arquivos/` (ou altere `PASTA_HTML` no script)
- Certifique-se de que os arquivos estão acessíveis

### 3. Executar o script

```bash
python script.py
```

### 4. Verificar resultado

- O arquivo `consolidado.txt` será criado no mesmo diretório
- Cada arquivo HTML será separado por delimitadores claros

## 📋 Exemplo de Saída

```
<!DOCTYPE html>
<html>
<head>
    <title>Primeiro Arquivo</title>
</head>
<body>
    <h1>Conteúdo do primeiro HTML</h1>
</body>
</html>

=================== novo arquivo ===================

<!DOCTYPE html>
<html>
<head>
    <title>Segundo Arquivo</title>
</head>
<body>
    <h1>Conteúdo do segundo HTML</h1>
</body>
</html>
```

## 🛠️ Requisitos

- **Python 3.6+** (funciona com versões mais recentes)
- **Bibliotecas padrão**: `glob`, `os`, `sys` (já incluídas no Python)

## 📊 Recursos Técnicos

### Tratamento de Erros

- ✅ Arquivos inacessíveis ou corrompidos são registrados mas não interrompem o processo
- ✅ Mensagens de erro detalhadas para diagnóstico
- ✅ Continuidade garantida mesmo com falhas pontuais

### Encoding e Compatibilidade

- 🔤 **UTF-8** como padrão para suporte internacional
- 🛡️ Parâmetro `errors='ignore'` para arquivos com encoding problemático
- 🌐 Compatível com caracteres especiais e acentos

### Performance

- ⚡ Processamento eficiente mesmo com centenas de arquivos
- 💾 Uso otimizado de memória (leitura arquivo por arquivo)
- 📈 Indicador de progresso em tempo real

## ⚠️ Considerações Importantes

1. **Tamanho dos arquivos**: Para muitos arquivos grandes, considere processar em lotes
2. **Encoding**: Arquivos com encoding não-UTF-8 podem ter caracteres mal formatados
3. **Espaço em disco**: O arquivo consolidado pode ser grande dependendo do volume
4. **Memória**: Arquivos HTML muito grandes podem consumir memória significativa

## 📝 Log de Execução

O script fornece feedback detalhado:

```
Iniciando a consolidacao...
Encontrados 15 arquivos HTML para processar.
Processando (1/15): index.html
Processando (2/15): about.html
...
--- SUCESSO! ---
Todos os arquivos foram consolidados em 'consolidado.txt'.
```

---

**💡 Dica**: Para processar arquivos muito grandes, considere executar o script em partes ou ajustar as configurações de memória do Python.
