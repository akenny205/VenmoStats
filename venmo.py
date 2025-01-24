from collections import Counter, defaultdict
import pandas as pd
import os
from transactions import Transaction

# If you want to use this yourself, simply change the working directory,
# and the acc_holder name. Make sure to use the same naming convention for the csv files
folder = "/Users/andrewkenny/Desktop/PythonProjects/VenmoStats/transactions/"
csvs = os.listdir(folder)
csvs = [folder + s for s in csvs if s.startswith('transaction_history')]
acc_holder = "Andrew Kenny"


def get_transactions(df):
    transactions = []
    for row in df.itertuples():
        if not pd.isna(row[3]):
            datetime = row[2]
            trans_type = row[3]
            note = str(row[5])
            sender = str(row[6])
            receiver = str(row[7])
            amount = float(row[8].replace('$', '').replace('+','').replace(' ', ''))
            funding_source = row[14]
            if trans_type == "Standard Transfer":
                funding_source = row[15]
            elif amount > 0:
                funding_source = row[15]
            curr_trans = Transaction(datetime, trans_type, note, sender, receiver, amount, funding_source)
            transactions.append(curr_trans)
    return transactions



def get_all_transactions():
    all_transactions = []
    for csv in csvs:
        df = pd.read_csv(csv, header=2, usecols=lambda column: column != 'Unnamed: 0')
        transactions = get_transactions(df)
        all_transactions.extend(transactions)
    return all_transactions


# gets beginning and ending balances for each month, as floats
# returns a list of lists where each list is [beginning, ending]
def get_balances():
    balances = []
    for csv in csvs:
        df = pd.read_csv(csv, header=2, usecols=lambda column: column != 'Unnamed: 0')
        beginning = float(df.values[0][15][1:])
        ending = float(df.values[len(df.values) - 1][16][1:])
        balances.append((beginning, ending))
    return balances


ALL_TRANSACTIONS = []
for trans in get_all_transactions():
    if trans.trans_type in ("Payment", "Charge"):
        ALL_TRANSACTIONS.append(trans)



def get_all_transactions_name(name):
    res = []
    for transaction in ALL_TRANSACTIONS:
        if name.lower() in transaction.sender.lower() or name.lower() in transaction.receiver.lower():
            res.append(transaction)
    return res

def get_all_names():
    res = set()
    for transaction in ALL_TRANSACTIONS:
        res.add(transaction.sender.lower())
        res.add(transaction.receiver.lower())
    if "nan" in res:
        res.remove("nan")
    return sorted(res)

def get_all_first_and_last_names():
    names = set()
    for transaction in get_all_transactions():
        if transaction.trans_type in ("Charge", "Payment"):
            names.add(transaction.sender)
            names.add(transaction.receiver)
    return names

def get_all_names_not_lower():
    res = set()
    for transaction in ALL_TRANSACTIONS:
        res.add(transaction.sender)
        res.add(transaction.receiver)
    if "nan" in res:
        res.remove("nan")
    return sorted(res)


def total_sent():
    return round(sum(abs(trans.amount) for trans in ALL_TRANSACTIONS if acc_holder.lower() in trans.sender.lower()),2)

def total_sent_name(name):
    return round(sum(abs(trans.amount) for trans in ALL_TRANSACTIONS if name.lower() in trans.sender.lower()),2)

def total_received():
    return round(sum(abs(trans.amount) for trans in ALL_TRANSACTIONS if acc_holder.lower() in trans.receiver.lower()),2)

def total_received_name(name):
    return round(sum(abs(trans.amount) for trans in ALL_TRANSACTIONS if name.lower() in trans.receiver.lower()),2)

def total_sent_and_received():
    return total_sent() + total_received()

def total_sent_and_received_name(name):
    return round(total_sent_name(name) + total_received_name(name),2)

def all_sent_and_received():
    names = get_all_names()
    res = []
    for name in names:
        if name not in acc_holder.lower():
            res.append([name, total_sent_and_received_name(name)])
    return reversed(sorted(res, key = lambda x: x[1]))


#PROBLEM WITH BANK TRANSFERS
def all_amounts():
    dict = Counter()
    for transaction in ALL_TRANSACTIONS:
        dict[abs(transaction.amount)]+=1
    return dict


def all_amounts2():
    res = set()
    for transaction in ALL_TRANSACTIONS:
        res.add(abs(transaction.amount))
    return sorted(res, reverse=True)

def get_topX_sent(x):
    sent_totals = defaultdict(float)
    for transaction in ALL_TRANSACTIONS:
        sent_totals[transaction.sender] += abs(transaction.amount)
    del sent_totals['Andrew Kenny']
    for total in sent_totals:
        sent_totals[total] = round(sent_totals[total],2)
    sorted_sent = sorted(sent_totals.items(), key=lambda item: item[1], reverse=True)
    return sorted_sent[:x]

def get_topX_received(x):
    received_totals = defaultdict(float)
    for transaction in ALL_TRANSACTIONS:
        received_totals[transaction.receiver] += abs(transaction.amount)
    del received_totals['Andrew Kenny']
    for total in received_totals:
        received_totals[total] = round(received_totals[total],2)
    sorted_received = sorted(received_totals.items(), key=lambda item: item[1], reverse=True)
    return sorted_received[:x]
print(get_topX_received(5))

def get_topX_sent_and_received(x):
    totals = defaultdict(float)
    for transaction in ALL_TRANSACTIONS:
        totals[transaction.sender] += abs(transaction.amount)
        totals[transaction.receiver] += abs(transaction.amount)
    del totals['Andrew Kenny']
    for total in totals:
        totals[total] = round(totals[total],2)
    sorted_totals = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    return sorted_totals[:x]

def get_topX_sent_and_received_freq(x):
    totals = defaultdict(float)
    for transaction in ALL_TRANSACTIONS:
        totals[transaction.sender] += 1
        totals[transaction.receiver] += 1
    del totals['Andrew Kenny']
    for total in totals:
        totals[total] = round(totals[total], 2)
    sorted_totals = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    return sorted_totals[:x]

def lprint(list):
    for n in list:
        print(n)


def get_all_data_name(name):
    return [f"Total Sent: ${total_sent_name(name)}",
            f"Total Received: ${total_received_name(name)}",
            f"Total Sent and Received: ${total_sent_and_received_name(name)}",
            ]

def get_all_data():
    return [f"Total Sent: ${total_sent()}",
            f"Total Received: ${total_received()}",
            f"Total Sent and Received: ${total_sent_and_received()}",
    ]




