# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solutions

## Grupo 77

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/natanael-fernandes-4a0054194/">Natanael Fernandes</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Kaio Rocha</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Gilenisson Santos</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Felipe Lofrano</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Jonattas Felipe</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Sabrina Otoni</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">André Godoi</a>


## 📜 Descrição

O sistema opera via linha de comando (CLI) e oferece um CRUD completo:
- **Cadastro de Culturas:** Registro de novos plantios com cálculos automáticos de área e insumos.
- **Listagem:** Visualização detalhada de todos os dados cadastrados (ID, Tipo, Área, Total de Insumos).
- **Atualização:** Permite editar informações de registros existentes.
- **Exclusão:** Remoção de registros do banco de dados.
- **Persistência:** Salvamento automático e carregamento de dados via arquivo CSV (`csv_handler.py`).


## 📁 Estrutura de pastas

- `src/main.py`: Ponto de entrada da aplicação e controle do loop principal.
- `src/model/crop.py`: Definição da classe `Crop` (Modelo de dados).
- `src/farm_math_handler.py`: Lógica matemática para cálculos de área e insumos específicos por cultura.
- `src/csv_handler.py`: Gerenciamento de leitura e escrita no arquivo de dados.
- `src/input_handler.py` & `src/menus.py`: Interface de usuário e validação de entradas.
- `src/RScripts`: scripts de execução R.

## 🔧 Como executar o código


Este projeto utiliza o **UV**, uma ferramenta moderna para gerenciamento de **Python, ambientes virtuais e dependências**.

O UV simplifica a configuração do ambiente e evita problemas comuns de versões do Python e instalação de pacotes.

---

### 1️⃣ Instalar o UV

Primeiro, instale o **UV** seguindo a documentação oficial:

🔗 https://docs.astral.sh/uv/getting-started/

Após instalar, verifique se o comando está disponível:

```bash
uv --version
```

### 2️⃣ Executar o projeto

Com o UV instalado, execute o projeto com:

```bash
uv run main.py
```

O `uv run` irá automaticamente:

- Criar um ambiente virtual se necessário
- Instalar as dependências do projeto
- Executar o arquivo main.py

## ✅ Pronto!

Se tudo estiver configurado corretamente, o projeto será executado no terminal.


## 🗃 Histórico de lançamentos

* 0.0.1 - 24/03/2026


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


