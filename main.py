import sys
from flashcard import *
# from ui import generate_html

def main():
    
    if len(sys.argv) < 2:
        print("Usage: py main.py <command> [options]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) == 4:
            front = sys.argv[2]
            back = sys.argv[3]
            add_card(front, back)
            print("Card added successfully.")
        else:
            print("Usage: py main.py add <front> <back>")
    
    elif command == "list":
        if len(sys.argv) >= 2:
            option = "all"
            if len(sys.argv) == 3 and sys.argv[2] in ["all", "due", "learn"]:
                option = sys.argv[2]
            cards = list_cards(option, sort_by_date=True)
            # generate_html(cards) 
            for card in cards:
                print(card)
        else:
            print("Usage: py main.py list [all/due/learn]")
    
    elif command == "delete":
        data = load()
        if len(sys.argv) == 3:
            front_to_delete = sys.argv[2]
            index_to_delete = next((i for i, card in enumerate(data) if card['front'] == front_to_delete), None)
            if index_to_delete is not None:
                delete_card(index_to_delete)
                print(f"Card '{front_to_delete}' deleted successfully.")
            else:
                print(f"Card '{front_to_delete}' not found.")
        else:
            print("Usage: py main.py delete <front>")
    
    elif command == "edit":
        data = load()
        if len(sys.argv) == 3:
            front_to_edit = sys.argv[2]
            card_to_edit = next((card for card in data if card['front'] == front_to_edit), None)
            if card_to_edit:
                card_to_edit['flag'] = 'edit'
                save()
                print(f"Card '{front_to_edit}' marked for editing.")
            else:
                print(f"Card '{front_to_edit}' not found.")
        else:
            print("Usage: py main.py edit <front>")

    elif command == "review":
        if len(sys.argv) == 3:
            set_review(sys.argv[2])
        else:
            print("Usage: py main.py review <front>")
    
    else:
        print(f"Unknown command: {command}")
        print("Usage: py main.py <command> [options]")

if __name__ == "__main__":
    main()
