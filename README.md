# Sobre este repositório

Este repositório foi criado para orientar os integrantes da equipe de competição [Robota UFSC](https://www.instagram.com/robota.ufsc/?hl=pt) na operação do robô UR3/CB3, carinhosamente apelidado de **O Garra**.

O objetivo deste material é documentar, de forma clara e prática, o processo necessário para operar o robô com **ROS 2** e **MoveIt 2**. Ao longo deste README, são apresentados:

- os passos de preparação do robô;
- o processo de conexão entre o notebook e o robô via cabo Ethernet;
- a configuração necessária no controlador;
- e a forma de iniciar o driver ROS 2 para controle externo.

---

# Preparando o robô

Para que o robô funcione corretamente com ROS 2, foram necessários quatro passos principais:

1. atualizar o software do robô;
2. estabelecer a conexão entre o notebook e o robô via cabo Ethernet;
3. configurar o **Host IP** e a **Porta** do controlador;
4. iniciar o programa de **controle externo** no robô.

## Atualização de software

As instruções oficiais para atualização do software podem ser consultadas nos links abaixo:

- [Download Center](https://www.universal-robots.com/articles/ur/documentation/download-center/)
- [Update Procedure](https://www.universal-robots.com/manuals/EN/HTML/SW5_20/Content/prod-serv-man/E-series/serv-man-update.htm)

> **Importante:** sempre que um update for instalado, ligue os motores do robô logo em seguida, como se fosse utilizá-lo normalmente. Isso é necessário para que a atualização de **firmware** também seja concluída corretamente. Esse cuidado é ainda mais importante quando for necessário realizar mais de uma atualização em sequência.

## Conectando o notebook ao robô

Primeiro, conecte um cabo Ethernet na parte inferior do CLP do robô e a outra extremidade no notebook.

O **robô** está configurado com o IP **192.168.0.141**. Essa informação pode ser verificada diretamente na IHM do robô, na tela inicial, acessando a seção **Sobre**.

No notebook, configure manualmente uma conexão de rede com os seguintes parâmetros:

- **IPv4:** Manual
- **Endereço IP:** `192.168.0.22`  
  > O último número pode ser alterado, desde que:
  > - seja diferente de `141`;
  > - esteja na mesma faixa de rede;
  > - e seja usado de forma consistente nas próximas configurações.
- **Máscara de rede:** `255.255.255.0`
- **Gateway:** `192.168.0.1`

## Configuração do Host IP e da porta do controlador

Para que o controlador do **O Garra** aceite comandos de movimento enviados pelo ROS 2, é necessário configurar corretamente o sistema de **External Control**.

Siga os passos abaixo:

1. Na IHM do robô, ligue o robô e faça sua inicialização normalmente.
2. Na tela principal, selecione **Programar Robô**.
3. Escolha **Programa Vazio**.  
   - Caso deseje utilizar um programa já existente, selecione **Carregar Programa** e abra o arquivo `external.urp`. Nesse caso, pule para o passo 6.
4. Dentro do programa, selecione **Estrutura** e depois **URCaps**.
5. Clique em **External Control**.  
   Após isso, será possível observar no lado esquerdo da IHM que o bloco **External Control** foi adicionado ao programa.
6. No topo da tela, vá para a seção **Instalação** e selecione **External Control** na barra lateral.
7. Verifique os campos de configuração:
   - **Host IP:** deve ser o mesmo IP configurado no notebook na seção [Conectando o notebook ao robô](#conectando-o-notebook-ao-robô);
   - **Custom Port:** deve ser mantido em **50002**.
8. Volte para a aba **Programa**. Na seção **Comando**, o IP atualizado deverá estar visível.

## Habilitando o controle externo

Após a configuração descrita acima, o robô estará pronto para receber comandos enviados pelo ROS 2.

Para isso, basta iniciar o programa configurado anteriormente:

- na IHM do robô, clique no botão **▶ Play**, localizado no canto inferior esquerdo da tela.

Com isso, o modo de **controle externo** será ativado, permitindo que o robô seja comandado pelo driver ROS 2.

---

## Observações finais

Antes de iniciar o driver ROS 2, confira se:

- o notebook está conectado ao robô via Ethernet;
- o IP do notebook está corretamente configurado;
- o **Host IP** no **External Control** corresponde ao IP do notebook;
- a porta configurada é **50002**;
- e o programa de controle externo está em execução na IHM.

Essas verificações evitam a maior parte dos problemas de conexão entre o notebook e o robô.

# Driver ROS2

```sh
ros2 launch ur_robot_driver ur_control.launch.py ur_type:=ur3 robot_ip:=192.168.0.141 launch_rviz:=true
```

```sh
ros2 launch ur_moveit_config ur_moveit.launch.py ur_type:=ur3 launch_rviz:=true
```