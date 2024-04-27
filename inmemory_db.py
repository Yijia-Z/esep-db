class InMemoryDB:
    def __init__(self):
        self.data = {}
        self.transaction = None

    def get(self, key):
        if key in self.data:
            if self.transaction is None:
                return self.data[key]
            elif key in self.transaction:
                return self.transaction[key]
            else:
                return self.data[key]
        return None

    def put(self, key, val):
        if self.transaction is None:
            raise Exception("Transaction not in progress")

        self.transaction[key] = val

    def begin_transaction(self):
        if self.transaction is not None:
            raise Exception("Transaction already in progress")

        self.transaction = {}

    def commit(self):
        if self.transaction is None:
            raise Exception("Transaction not in progress")

        self.data.update(self.transaction)
        self.transaction = None

    def rollback(self):
        if self.transaction is None:
            raise Exception("Transaction not in progress")

        self.transaction = None

def main():
    inmemoryDB = InMemoryDB()

    # Should return None, because 'A' doesn't exist in the DB yet
    print(inmemoryDB.get("A"))  # Output: None

    # Should throw an error because a transaction is not in progress
    try:
        inmemoryDB.put("A", 5)
    except Exception as e:
        print(e)  # Output: Transaction not in progress

    # Starts a new transaction
    inmemoryDB.begin_transaction()

    # Set's value of 'A' to 5, but it's not committed yet
    inmemoryDB.put("A", 5)

    # Should return None, because updates to 'A' are not committed yet
    print(inmemoryDB.get("A"))  # Output: None

    # Update 'A's value to 6 within the transaction
    inmemoryDB.put("A", 6)

    # Commits the open transaction
    inmemoryDB.commit()

    # Should return 6, that was the last value of 'A' to be committed
    print(inmemoryDB.get("A"))  # Output: 6

    # Starts a new transaction
    inmemoryDB.begin_transaction()

    # Set's value of 'A' to 7, but it's not committed yet
    inmemoryDB.put("A", 7)

    # Should return 7, because updates to 'A' are not committed yet
    print(inmemoryDB.get("A"))  # Output: 7

    # Rollback the open transaction
    inmemoryDB.rollback()

    # Should return 6, that was the last value of 'A' to be committed
    print(inmemoryDB.get("A"))  # Output: 6

if __name__ == "__main__":
    main()