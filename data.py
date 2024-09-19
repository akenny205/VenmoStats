from venmo import get_all_transactions, get_balances
from keyboard_mashing import keyboard_mashing_probability

transactions = get_all_transactions()
#balances = get_balances()

# retrieves data for each transaction for the given field
def get_data(field):
    res = []
    if not hasattr(transactions[0], field):
        raise AttributeError("field given is not in the dataset")
    for transaction in transactions:
        res.append(getattr(transaction, field, None))
    return res


def getTotalSentAndReceived():
    return round(sum(abs(a) for a in get_data("amount")),2)
def getTotalSent():
    return round(abs(sum(a for a in get_data("amount") if a < 0)),2)
def getTotalReceived():
    return round(sum(a for a in get_data("amount") if a > 0),2)

notes_with_scores = []
for transaction in transactions:
    if transaction.trans_type in ("Payment", "Charge"):
        notes_with_scores.append([transaction.note, keyboard_mashing_probability(transaction.note)])

# print all notes:
notes_with_scores = sorted(notes_with_scores, key=lambda x: x[1], reverse=True)
for note in notes_with_scores:
    print(note)
    




