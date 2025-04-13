# keylogger-spyware 🕵️

![Badge de Status](https://img.shields.io/badge/status-Desenvolvido-purple)

> Computacionalmente falando, um spyware é um script que espiona o teclado da vítima. Em nosso caso, vamos espionar o teclado, usando um script em python.
 
<br>

## 🧩 Arquitetura
O projeto segue a seguinte arquitetura.

``` text
📁 src
├── 📁 repositories
│   └── 📝 keylogger_repository.py  # funções com interações com o buffer.txt
│  
├── 📁 services
│   └── 📄 keylogger_service.py  # funções 
│  
└── 📝 main.py
```
<br>

## 📦 Bibliotecas
Vale o destaque da library <a href='https://pypi.org/project/pynput/'> pyinput </a> que fornece métodos para monitorar o teclado do target. 

<br>

## 🚀 Executando o projeto
Para executar o projeto basta instalar a dependência e depois executar o arquivo main.py

```bash
  pip install -r requirements.txt && python3 ./main.py
```

<br>

## 📞 Contato

- **Pedro Fernandes** - <a href="https://www.instagram.com/umpreto.dev/">umpreto.dev</a>
- **Email** - umpret.dev@gmail.com
- **LinkedIn** - <a href="https://www.linkedin.com/in/pedro-fernandes-b72a8516b/">Pedro Fernandes</a>
---

Feito com ❤️ por Umpreto.dev
