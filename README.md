# ⏱️ Python Shutdown Timer

Um pequeno projeto em Python que lê um arquivo com um tempo definido, exibe um timer regressivo no terminal e desliga o computador automaticamente.  
Funciona em **Windows, Linux e macOS**.  

---

## 📝 Funcionalidades

- Procura arquivos com prefixo específico (`DTF-`) em pastas padrão do usuário 📂  
- Extrai o tempo do nome do arquivo ⏳  
- Mostra contagem regressiva no terminal 🖥️  
- Permite **cancelar o desligamento com CTRL+C** ✋  
- Desliga o PC automaticamente quando o timer chega a 0 🔌  

---

## ⚙️ Como usar

1. Coloque um arquivo com prefixo `DTF-` nas pastas padrão (`Documents`, `Downloads`, `Music`, etc.)  
   - Exemplo de nome: `DTF-1h2m5s.txt`  
2. Execute o projeto:  
```
python main.py
```  
3. O timer vai começar a contagem regressiva ⏱️  
4. Para cancelar, pressione **CTRL+C** ✋  

---

## 🛠️ Estrutura do projeto

```
project/
│
├─ main.py        # Fluxo principal do programa
├─ timer.py       # Timer e desligamento
├─ utils.py       # Funções auxiliares
└─ README.md      # Este arquivo
```

---

## 🚀 Próximos passos

- Adicionar suporte a múltiplos arquivos com tempos diferentes  
- Criar interface gráfica simples 🖌️  
- Transformar em executável (.exe) para facilitar uso 💻  

---

## 📄 Licença

MIT License
