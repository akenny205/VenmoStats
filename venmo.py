from idlelib.pyparse import trans
import pandas as pd
import os
from transactions import Transaction


folder = "/Users/andrewkenny/Desktop/PythonProjects/VenmoStats/transactions/"
csvs = os.listdir(folder)
csvs = [folder + s for s in csvs if s.startswith('transaction_history')]


def get_transactions(df):
    transactions = []
    for row in df.itertuples():
        if not pd.isna(row[3]):
            datetime = row[2]
            trans_type = row[3]
            status = row[4]
            note = str(row[5])
            sender = str(row[6])
            receiver = str(row[7])
            amount = float(row[8].replace('$', '').replace('+','').replace(' ', ''))
            funding_source = ""
            if trans_type == "Standard Transfer":
                funding_source = row[15]
            elif amount > 0:
                funding_source = row[15]
            else:
                funding_source = row[14]
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







def get_balances():
    #first row, for begining balance

    for csv in csvs:
        df = pd.read_csv(csv, header=2, usecols=lambda column: column != 'Unnamed: 0')
        

    return 0


