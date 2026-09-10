import random
random.seed(42)

def draw_hand(deck):
    deck = deck.copy()
    random.shuffle(deck)
    return deck[:7], deck[7:]


def count_lands(hand):
    return hand.count(0)


def build_deck():
    deck = [0] * 24 + [1] * 12 + [2] * 12 + [3] * 8 + [4] * 4
    assert len(deck) == 60
    return deck


def is_playable(hand, library):
    hand = hand.copy()
    library = library.copy()
    mana = 0

    for turn in range(1, 4):
        if turn > 1:
            hand.append(library.pop(0))

        if 0 in hand:
            hand.remove(0)
            mana += 1

        costs = sorted([x for x in hand if x > 0])

        if not costs:
            return False

        if costs[0] > mana:
            return False

        hand.remove(costs[0])

    return True


def run_simulation(n=10000, minimum=2, maximum=5):
    deck = build_deck()
    false_positives = 0
    false_negatives = 0

    for _ in range(n):
        hand, library = draw_hand(deck)

        lands = count_lands(hand)
        heuristic = minimum <= lands <= maximum
        oracle = is_playable(hand, library)

        if heuristic and not oracle:
            false_positives += 1

        if not heuristic and oracle:
            false_negatives += 1

    return false_positives / n * 100, false_negatives / n * 100


for minimum in range(1, 4):
    for maximum in range(3, 7):
        fp, fn = run_simulation(10000, minimum, maximum)
        print(
            f"{minimum}-{maximum}: "
            f"false positives = {fp:.2f}%, "
            f"false negatives = {fn:.2f}%"
        )
