from functools import cmp_to_key

with open('input/07.txt', 'r') as file:
    _input = [x.strip().split(' ') for x in file.readlines()]

normal_deck = list('23456789TJQKA')
joker_deck = list('J23456789TQKA')
joker = False


def compare_hands(player_a, player_b):
    hands = {
        'a': player_a[0],
        'b': player_b[0]
    }

    deck = joker_deck if joker else normal_deck

    cards = {}

    for p in ['a', 'b']:
        cards[p] = dict.fromkeys(deck, 0)

        for card in hands[p]:
            cards[p][card] += 1

        if joker:
            count = cards[p]['J']
            cards[p]['J'] = 0
            cards[p][max(cards[p], key=cards[p].get)] += count

    # 5, 4 and 3 of kind
    if max(cards['a'].values()) > max(cards['b'].values()):
        return 1
    elif max(cards['a'].values()) < max(cards['b'].values()):
        return -1

    # full house, two pairs and pairs
    if sum([x for x in cards['a'].values() if x > 1]) > sum([x for x in cards['b'].values() if x > 1]):
        return 1
    elif sum([x for x in cards['a'].values() if x > 1]) < sum([x for x in cards['b'].values() if x > 1]):
        return -1

    # high card
    for c in range(5):
        if deck.index(hands['a'][c]) > deck.index(hands['b'][c]):
            return 1
        elif deck.index(hands['a'][c]) < deck.index(hands['b'][c]):
            return -1

    return 0


_input.sort(key=cmp_to_key(compare_hands))
print('0701:', sum([(x+1) * int(_input[x][1]) for x in range(len(_input))]))

joker = True
_input.sort(key=cmp_to_key(compare_hands))
print('0702:', sum([(x+1) * int(_input[x][1]) for x in range(len(_input))]))
