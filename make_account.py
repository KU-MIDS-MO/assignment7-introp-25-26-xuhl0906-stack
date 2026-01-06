def make_account(initial_balance):
    if not isinstance(initial_balance, (int, float)):
        raise TypeError("Initial balance must be numeric.")
    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative.")

    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be numeric.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
       
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdraw amount must be numeric.")
     
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
     
        if amount > balance:
            raise ValueError("Insufficient funds.")

        balance -= amount
        return balance

    return deposit, withdraw
