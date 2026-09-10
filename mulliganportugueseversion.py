import random
random.seed(42)

def comprar_mao(deck):
    deck = deck.copy()
    random.shuffle(deck)
    return deck[:7], deck[7:]


def contar_terras(mao):
    return mao.count(0)


def criar_deck():
    deck = [0] * 24 + [1] * 12 + [2] * 12 + [3] * 8 + [4] * 4
    assert len(deck) == 60
    return deck


def jogavel(mao, resto):
    mao = mao.copy()
    resto = resto.copy()
    mana = 0

    for turno in range(1, 4):
        if turno > 1:
            mao.append(resto.pop(0))

        if 0 in mao:
            mao.remove(0)
            mana += 1

        custos = sorted([x for x in mao if x > 0])

        if not custos:
            return False

        if custos[0] > mana:
            return False

        mao.remove(custos[0])

    return True


def simular(n=10000, minimo=2, maximo=5):
    deck = criar_deck()
    falsos_positivos = 0
    falsos_negativos = 0

    for _ in range(n):
        mao, resto = comprar_mao(deck)

        terras = contar_terras(mao)
        heuristica = minimo <= terras <= maximo
        oracle = jogavel(mao, resto)

        if heuristica and not oracle:
            falsos_positivos += 1

        if not heuristica and oracle:
            falsos_negativos += 1

    return falsos_positivos / n * 100, falsos_negativos / n * 100


for minimo in range(1, 4):
    for maximo in range(3, 7):
        fp, fn = simular(10000, minimo, maximo)
        print(
            f"{minimo} a {maximo}: "
            f"falsos positivos = {fp:.2f}%, "
            f"falsos negativos = {fn:.2f}%"
        )
