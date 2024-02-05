import os
import json
import datetime

data = []

HOME = os.environ['HOME'] if os.name == 'posix' else os.path.join(os.environ['USERPROFILE'], 'Desktop')

if 'ARCHIVE' not in os.environ:
    # Verificar o sistema operacional
    if os.name == 'posix':
        print("""
              Use this command to set path to your archive:
              export ARCHIVE=/dictionary/<topic>.json""")
    elif os.name == 'nt':
        print("""
              Use this command to set path to your archive:
              set ARCHIVE=Dictionary-CLI\<topic>.json""")
    exit()


def load():
    # print(HOME)
    # print(os.path.join(HOME, os.environ['ARCHIVE']))
    try:
        with open(os.path.join(HOME, os.environ['ARCHIVE']), 'r') as f:
            global data
            data = json.load(f)
    except FileNotFoundError:
        data = []
    return data

def save():
    with open(os.path.join(HOME, os.environ['ARCHIVE']), 'w') as f:
        json.dump(data, f, indent=4)

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
    data = load()
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
    print("You reviewed:", front)
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
