# Sobre esse repositório

Este documento e repositório está direcionado aos integrantes da equipe de competição [Robota  UFSC](https://www.instagram.com/robota.ufsc/?hl=pt), para a orientar na operação do robô UR3 / CB3, carinhosamente apelidado de "O Garra".
Este repositório serve para que seja possivel operar O Garra com ROS2 e MoveIt2. Primeiramente estará documentado qual foi o processo para de preparação do robô, como foi estabelecido a conexão com entre um notebook e o robô, e como iniciar o ROS2 Driver.

# Preparando o Robô

Foram 4 processos que foram feitos para que o robô funcionasse com ROS2: fazer o update do software do robô, iniciar a conexão (via cabo Ethernet) entre o notebook e o robô, atualizar os Host IP e Port do controlador e, por fim, iniciar o programa com o controle externo.

## Update de Software

As informações oficiais para a realização dos updates podem ser encontrados nos seguintes links: [Download Center](https://www.universal-robots.com/articles/ur/documentation/download-center/) e [Update Procedure](https://www.universal-robots.com/manuals/EN/HTML/SW5_20/Content/prod-serv-man/E-series/serv-man-update.htm).

*É importante destacar a importancia de sempre que fizer update, ligar os motores do robô (como se você fosse operar, mover o robô) assim que instalar um update, para que seja feito também o update do firmeware. Especialmente se for necessário mais de um update seguido.*

## Conectando o Notebook

Primeiro, conecte um cabo Ethernet na parte inferior do CLP do robô, e a outra ponta no notebook.

O **robô** está configurado no IP **192.168.0.141**. Você pode verificar essa informação na IHM do robô (na tela inicial, selecione *sobre*).

Para configurar o notebook, vá nas configurações de rede do notebook e crie uma nova conexão com as seguintes informações:
- IPv4 - Manual;
- Endereço: 192.168.0.22 (o último número pode ser modificado, mas deve ser consistente com as próximas configurações e diferente de 141);
- Netmask: 255.255.255.0
- Gateway: 192.168.0.1

## Host IP e Port do Controlador 

Para que o controlador do O Garra aceite os comandos de movimento vindas do ROS2, é preciso configurar o sistema para identificar esses comandos. Para isso, siga os passos a seguir:

1. No IHM do robô, depois de ligar o robô, faça a sua inicialização;
2. Novamente na tela principal, selecione *Programar Robô";
3. Selecione *Programa Vazio* (Caso queira usar o já existente, selecione *Carregar Programa* e *external.urp*, e pule para o número 6);
4. Dentro do programa, selecione *Estrutura* e depois *URCaps*;
5. Clique em *External Control*. É possivel observar que no lado esquerdo da IHM o *Control* foi adicionado no programa;
6. No topo da tela, mude para a seção *Instalação* e em seguida selecione *External Control*. Aqui é possivel ver o Host IP e Port configurados para o controlador. O IP deve ser o mesmo que foi configurado para o laptop durante a seção [Conectando o Notebook](#conectando-o-notebook). O Custom port deve ser mantido em 50002.
7. Volte para o Programa, na seção *Comando* você deve ser capaz de ver o IP atualizado.

## Controle Externo

Para habilitar agora o robô para receber comandos do ROS2, você deve apenas iniciar o programa que foi configurado na seção anterior. Para fazer isso, clique no ▶︎ play no canto inferior esquerdo da IHM.

# Driver ROS2

```sh
ros2 launch ur_robot_driver ur_control.launch.py ur_type:=ur3 robot_ip:=192.168.0.141 launch_rviz:=true
```

```sh
ros2 launch ur_moveit_config ur_moveit.launch.py ur_type:=ur3 launch_rviz:=true
```