# ⏱️ Delayed Shutdown

Um pequeno projeto em Python que lê um arquivo com um tempo definido, exibe um timer regressivo no terminal e desliga o computador automaticamente.  
Funciona em **Windows, Linux e macOS**.  



## 📝 Funcionalidades

- Procura arquivos com prefixo específico (`DTF-`) em pastas padrão do usuário 📂  
- Extrai o tempo do path do arquivo ⏳  
- Mostra contagem regressiva no terminal 🖥️  
- Permite **cancelar o desligamento com CTRL+C** a qualquer momento ✋  
- Desliga o PC automaticamente quando o timer chega a 0 🔌  



## ⚙️ Como usar

1. Coloque um arquivo com prefixo `DTF-` em alguma das seguintes pastas (`Documents`, `Downloads`, `Music`, etc.)  
   - Exemplo de nome: `DTF-1h2m5s.exe` -> Desliga em 1 hora, 2 minutos e 5 segundos.
2. Execute o projeto:  
```
python __main__.py
```  
3. O timer vai começar a contagem regressiva 
4. Para cancelar, pressione **CTRL+C**



## 👷‍♂️ Buildar

Se quiser um executável, basta clonar o repositório com o comando…

```
git clone https://github.com/Murice-Netto/delay-shutdown.git
```

> **🪜 Depois, tenha o pyinstaller instalado na sua máquina. Caso não tenha, instale com o seguinte comando:**

```
pip install pyinstaller
```

> **🪜 Depois, basta usar o comando (dentro da pasta do projeto):**

```
pyinstaller --icon .\assets\icon.ico --onefile --name DTF-2h .\__main__.py
```

Esse comando criara um executável do seu sistema operacional na pasta `dist/`. Basta executar ele que o sistema funcionará da mesma exata forma!


## 🛠️ Estrutura do projeto

```
project/
│
├─ __main__.py        # Fluxo principal do programa
├─ timer.py           # Timer e desligamento
├─ utils.py           # Funções auxiliares
└─ README.md          # Este arquivo
```



## 📄 Licença

MIT License
