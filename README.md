# Sobre esse repositório

Este documento e repositório está direcionado aos integrantes da equipe de competição [Robota  UFSC](https://www.instagram.com/robota.ufsc/?hl=pt), para a orientar na operação do robô UR3 / CB3, carinhosamente apelidado de "O Garra".
Este repositório serve para que seja possivel operar O Garra com ROS2 e MoveIt2. Primeiramente estará documentado qual foi o processo para de preparação do robô, como foi estabelecido a conexão com entre um notebook e o robô, e como iniciar o ROS2 Driver.

# Preparando o Robô

Foram 4 processos que foram feitos para que o robô funcionasse com ROS2: fazer o update do software do robô, iniciar a conexão (via cabo Ethernet) entre o notebook e o robô, atualizar os IP e Host do controlador e, por fim, iniciar o programa com o controle externo.

## Update de Software

As informações oficiais para a realização dos updates podem ser encontrados nos seguintes links: [Download Center](https://www.universal-robots.com/articles/ur/documentation/download-center/) e [Update Procedure](https://www.universal-robots.com/manuals/EN/HTML/SW5_20/Content/prod-serv-man/E-series/serv-man-update.htm).

*É importante destacar a importancia de sempre que fizer update, ligar os motores do robô (como se você fosse operar, mover o robô) assim que instalar um update, para que seja feito também o update do firmeware. Especialmente se for necessário mais de um update seguido.*

## Conectando o Notebook

Primeiro, conecte um cabo Ethernet na parte inferior do CLP do robô, e a outra ponta no notebook.

O **robô** está configurado no IP **192.168.0.141**. Você pode verificar essa informação na IHM do robô (na tela inicial, selecione *sobre*).

Para configurar o notebook, vá nas configurações de rede do notebook e crie uma nova conexão com as seguintes informações:
- IPv4 - Manual;
- Endereço: 192.168.0.22 (o último número pode ser modificado, mas deve ser consistente com as próximas configurações e diferente de 141);

## IP e Host do Controlador 

