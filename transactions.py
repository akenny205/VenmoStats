# class that represents a transaction in Venmo
class Transaction:
    def __init__(self, date, trans_type, note, sender, receiver, amount, source_or_destination):
        self.date = date
        self.trans_type = trans_type
        self.note = note
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.source_or_destination = source_or_destination

    def __str__(self):
        return (f"Transaction(date={self.date}, trans_type={self.trans_type}, note={self.note}, "
                f"sender={self.sender}, receiver={self.receiver}, amount={self.amount}, "
                f"source_or_destination={self.source_or_destination})")




