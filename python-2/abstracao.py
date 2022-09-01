import time


class TimeTurner:
    def __init__(self, skill, person):
        self.skill = skill
        self.person = person

    def back_in_time(self):
        start = time.time()

        mensagem = f"Para {self.skill}, a {self.person}, "
        mensagem += f"passou pela primeira camada do tempo em {time.time()}. "

        time.sleep(3)

        mensagem += f"Passou pela segunda camada do tempo em {time.time()}. "
        time.sleep(5)

        end = time.time()
        calculo_tempo = end - start

        return mensagem + f"E o tempo total gasto foi: {calculo_tempo}"


hermyone = TimeTurner('voltar ao tempo e salvar o Harry', 'Hermione')

# Voce nao precisa saber o que acontece por debaixo dos panos da função
print(hermyone.back_in_time())
