'''
Sistema de notificação inteligente
Lucas trabalha em um sistema de notificações que precisa enviar mensagens 
para usuários. No entanto, algumas notificações só devem ser enviadas se 
o usuário tiver ativado essa opção no sistema. Além disso, se o usuário
for VIP, ele deve receber uma notificação prioritária antes das demais.
Com base nesse cenário, crie um programa que simule o envio de notificações 
para três usuários. Cada usuário tem um status diferente:
    Ana: VIP (deve receber uma notificação prioritária antes das normais).
    João: Usuário comum, mas ativou as notificações.
    Carla: Usuária comum, mas desativou as notificações (não deve receber nada).
O programa deve exibir quais notificações foram enviadas e quais usuários 
não receberam nada.
'''
import asyncio

async def enviar_notificacao(usuario, mensagem, prioridade=False):
    if prioridade:
        print(f"Enviando notificação prioritária para {usuario}: {mensagem}")
    else:
        print(f"Enviando notificação para {usuario}: {mensagem}")

async def main():
    usuarios = {
        "Ana": {"vip": True, "notificacoes_ativadas": True},
        "João": {"vip": False, "notificacoes_ativadas": True},
        "Carla": {"vip": False, "notificacoes_ativadas": False}
    }

    tarefas = []
    for usuario, info in usuarios.items():
        if info["notificacoes_ativadas"]:
            if info["vip"]:
                tarefas.append(enviar_notificacao(usuario, "Você tem uma nova notificação!", prioridade=True))
            else:
                tarefas.append(enviar_notificacao(usuario, "Você tem uma nova notificação!"))
        else:
            print(f"{usuario} não recebeu nenhuma notificação.")

    await asyncio.gather(*tarefas)

asyncio.run(main())
