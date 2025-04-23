<div align="justify">
# Coordinación de Robots ABB IRB 120 – Simulación y Ejecución Real

## Introducción

Este proyecto aborda la coordinación de dos manipuladores **ABB IRB 120** en dos fases complementarias: primero, mediante simulación en **RobotStudio** para validar la lógica de estación y los movimientos planificados; y después, en un entorno real donde los robots ejecutan la misma rutina comunicándose a través de sockets. El objetivo principal es garantizar que ambos robots cooperen de forma sincronizada para levantar, desplazar y depositar una caja sin interrumpir el flujo de acción ni generar colisiones.

## Simulación en RobotStudio

![image](https://github.com/user-attachments/assets/9500abc6-e0b8-4c03-bf8e-bdc068a76703)

La fase de simulación se implementó creando tres **comportamientos progresivos** en RobotStudio. En el primero, cada IRB 120 recorre de manera independiente una trayectoria rectangular sobre una mesa. En el segundo, se añade una **ventosa inteligente** en el extremo de cada robot y se desarrolla la **lógica de estación** con señales digitales. El tercer comportamiento orquesta la apilación de doce piezas, alternando la orientación en cada nivel, aplicando lógica de estación avanzada y movimientos lineales en RAPID para asegurar un agarre y colocación libres de colisiones. Toda la coordinación y las rutinas RAPID se verificaron exhaustivamente en RobotStudio antes de saltar al hardware real.

## Ejecución en Entorno Real

![image](https://github.com/user-attachments/assets/68311aee-7090-4371-9ecd-a13a9a19801f)

Para trasladar la coordinación al mundo real, se desarrolló un controlador central en **Python** `socket_PC.py` que establece dos conexiones **socket** con las direcciones IP de cada robot. Utilizando `select()`, el servidor Python escucha confirmaciones de finalización de tarea de uno de los robots y, de inmediato, envía el comando de inicio al otro, alternando así los movimientos de elevación y descenso de la caja. En el lado de los robots, cada IRB 120 ejecuta un programa en **RAPID** que crea un **socket servidor**, espera el mensaje de arranque con `SocketReceive` y al finalizar su rutina responde con `SocketSend`. Este intercambio determinista de mensajes garantiza que ninguno de los dos controladores independientes avance sin la confirmación del compañero, logrando una sincronización precisa en el laboratorio.

## Validación Híbrida

Durante la puesta en marcha real, una de las unidades presentó problemas técnicos, por lo que se adoptó un esquema híbrido: el robot 1 operaba físicamente en el laboratorio y el robot 2 se simulaba en RobotStudio, manteniendo intacto el mismo flujo de mensajes TCP/IP. Gracias a este enfoque, fue posible demostrar la robustez del protocolo de comunicación y la adaptabilidad de la lógica de estación antes de completar la integración de ambos robots reales.

## Conclusiones

La combinación de simulación avanzada y pruebas en hardware real ha confirmado la viabilidad de la **coordinación multirobot** basada en sockets y RAPID. El uso de RobotStudio permitió depurar la lógica de estación y los movimientos sin riesgo físico, mientras que la transición al entorno real evidenció la eficacia del intercambio de mensajes mediante `SocketSend` y `SocketReceive` para asegurar una ejecución segura, sincronizada y libre de colisiones. Este proyecto sienta las bases para arquitecturas colaborativas más complejas en entornos industriales, donde múltiples manipuladores deben trabajar de forma simultánea y confiable.

</div>
