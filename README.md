# 🧮 Simulador de Autômato Finito Determinístico (AFD)

**Autor:** Ruam Marcos Maciel dos Santos  

---

## 📘 1. Sobre o Projeto

Este script em **Python** implementa e simula um **Autômato Finito Determinístico (AFD)**, permitindo validar se determinadas palavras pertencem a uma linguagem específica.

O autômato foi desenvolvido com base no **diagrama visual** incluído nos arquivos do projeto.

---

## ⚙️ 2. Como Executar

### **Requisitos**
- Python 3 instalado no sistema.

### **Passos para execução**
1. Abra um terminal ou prompt de comando.  
2. Navegue até o diretório onde o arquivo `AFD_reescrito.py` está salvo.  
3. Execute o comando abaixo:

```bash
python AFD_reescrito.py
```

---

## 🧾 3. Exemplo de Saída do Script

```
Iniciando simulação do AFD...
----------------------------------------
Palavra de entrada: 'babaaab'
  -> Estado de parada: 'q5'
  -> Resultado: Palavra ACEITA
----------------------------------------
Palavra de entrada: 'aabba'
  -> Estado de parada: 'q6'
  -> Resultado: Palavra ACEITA
----------------------------------------
Palavra de entrada: 'aaa'
  -> Estado de parada: 'q4'
  -> Resultado: Palavra ACEITA
----------------------------------------
Palavra de entrada: 'bbb'
  -> Estado de parada: 'q0'
  -> Resultado: Palavra REJEITA
----------------------------------------
Palavra de entrada: 'ababab'
  -> Estado de parada: 'q7'
  -> Resultado: Palavra ACEITA
----------------------------------------
Palavra de entrada: 'ababaaba'
  -> Estado de parada: 'q2'
  -> Resultado: Palavra REJEITA
----------------------------------------
```

---

## 🧩 Observação

O comportamento e as transições do autômato podem ser personalizados editando diretamente o código ou o arquivo de configuração correspondente ao diagrama visual fornecido.
