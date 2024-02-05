import json
import datetime

data = []

def load():
    try:
        with open('/data/data/com.termux/files/home/dictionary/phrases.json', 'r') as f:
            global data
            data = json.load(f)
    except FileNotFoundError:
        data = []
    return data

def save():
    with open('/data/data/com.termux/files/home/dictionary/phrases.json', 'w') as f:
        json.dump(data, f, indent=4)

def initialize_cards_data():
    try:
        with open('/data/data/com.termux/files/home/dictionary/phrases.json', 'r') as f:
            pass
    except FileNotFoundError:
        with open('/data/data/com.termux/files/home/dictionary/phrases.json', 'w') as f:
            json.dump([], f)

def initialize_words():
    words_to_add = [
    ("ocorrência", None),
    ("previsão", None),
    ("enganar", None),
    ("sacana", None),
    ("sacanagem", None),
    ("previsto", None),
    ("sabedoria", None),
    ("derreter", None),
    ("palhaso", None),
    ("greve", None),
    ("paso", None),
    ("cacofonia", None),
    ("pasto", None),
    ("perseguir", None),
    ("tecido", None),
    ("fio", None),
    ("taer", None),
    ("tingir", None),
    ("teclado", None),
    ("trama", None),
    ("teclar", None),
    ("digitar", None),
    ("tecer", None),
    ("teia", None),
    ("regata", None),
    ("manga", None),
    ("remar", None),
    ("paletó", None),
    ("blazer", None),
    ("conto de fadas", None),
    ("vício", None),
    ("intrometer", None),
    ("afastar", None),
    ("sequestar", None),
    ("renda", None),
    ("comportar", None),
    ("molde", None),
    ("exagerar", None),
    ("moldar", None),
    ("deputado", None),
    ("agir", None),
    ("respingar", None),
    ("alheios", None),
    ("câmara", None),
    ("voto popular", None),
    ("arcaico", None),
    ("desprender", None),
    ("cercar", None),
    ("louvor", None),
    ("cipoal", None),
    ("desencanto", None),
    ("virtudes", None),
    ("preservar", None),
    ("capaz", None),
    ("altura", None),
    ("largura", None),
    ("comprimento", None),
    ("cumprimentar", None),
    ("torcer", None),
    ("cospir", None),
    ("bisop", None),
    ("por que", None),
    ("porque", None),
    ("redor", None),
    ("afinada", None),
    ("desafinada", None),
    ("afinar", None),
    ("estrebaria", None),
    ("boja", None),
    ("baja", None),
    ("qural", None),
    ("mudo", None),
    ("humor", None),
    ("couve", None),
    ("couve-flor", None),
    ("fêmur", None),
    ("apojo", None),
    ("don", None),
    ("assombrosos", None),
    ("inflação", None),
    ("deflação", None),
    ("conviver", None),
    ("prevalecer", None),
    ("dotado", None),
    ("imprestar", None),
    ("chapa", None),
    ("caprichoso", None),
    ("assa", None),
    ("picou", None),
    ("mamar", None),
    ("gemer", None),
    ("churrasqueira", None),
    ("ademissão", None),
    ("demissão", None),
    ("demitir", None),
    ("chapeado", None),
    ("lascado", None),
    ("caber", None),
    ("prender", None),
    ("curto", None),
    ("atrocidade", None),
    ("remorco", None),
    ("pulsera", None),
    ("unção", None),
    ("célula", None),
    ("cela de prisão", None),
    ("fera", None),
    ("feira", None)
    ]

    for word, meaning in words_to_add:
        add_card(word, meaning)

def add_card(front, back):
    data = load()
    for card in data:
        if card['front'] == front and card['back'] == back:
            print("Card already exists.")
            return

    next_review_date = datetime.datetime.now()
    interval = 1

    data.append({
        'front': front,
        'back': back,
        'next_review_date': next_review_date.isoformat(),
        'interval': interval,
    })

    save()

def delete_card(index):
    data.pop(index)
    save()

def delete_cards(start_index, end_index):
    del data[start_index:end_index+1]
    save()

def edit_cards():
    for card in data:
        if card.get('flag') and card['flag'] == "edit":
            del card['flag']

    save()

def list_cards(option="all", sort_by_date=False):
    data = load()
    card_list = []
    now = datetime.datetime.now()

    # Function to get the next review date for sorting
    def get_sort_key(card):
        return datetime.datetime.fromisoformat(card['next_review_date'])

    if sort_by_date:
        data.sort(key=get_sort_key, reverse=True)

    for card in data:
        if card.get('flag') and card['flag'] == "wrong":
            continue

        next_review = datetime.datetime.fromisoformat(card['next_review_date'])

        if option == "all":
            card_list.append(f"{card['front']}")
        elif option == "due" and next_review <= now:
            card_list.append(f"{card['front']}")
        elif option == "learn" and card.get('flag') == "learn":
            card_list.append(f"{card['front']}")

    return card_list

def set_review(front):
    print(front)
    data = load()
    now = datetime.datetime.now()
    for card in data:
        if card['front'] == front:
            card['next_review_date'] = now.isoformat()
            save()


def review_cards():
    now = datetime.datetime.now()
    reviewed = False

    for card in data:
        if card.get('flag') and card['flag'] == "wrong":
            continue

        next_review = datetime.datetime.fromisoformat(card['next_review_date'])

        if next_review <= now:

            print(f"Front: {card['front']}")
            answer = input("Do you remember what's on the back? (y/n) ")

            if answer.lower() == 'y':
                # Important formula
                card['interval'] *= 2
                card['next_review_date'] = calculate_review_date(card['interval']).isoformat()
                print("Congratulation!")
                save()
            else:
                card['interval'] = 0
                card['next_review_date'] = datetime.datetime.now().isoformat()
                print("Back: ")
                print(card['back'])
                save()

            end = input("Press Enter to continue...")

def calculate_review_date(interval):
    return datetime.datetime.now() + datetime.timedelta(minutes=interval)
