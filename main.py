from sqlalchemy.orm import sessionmaker
import logging
logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

import module
from module import engine, Person, Bank, Account, Transaction


Session = sessionmaker(bind=engine)
session = Session()

while True:
    choice = int(input("1 - Add Person\n2 - Add Bank\n3 - Add Account\n4 - Add Income/Expense\n5 - View All Persons\n6 - View All Banks\n7 - View All Accounts\n8 - View Transactions History\n9 - Exit\nEnter your choice: "))

    if choice == 1:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        person = Person(first_name=first_name, last_name=last_name, email=email)
        session.add(person)
        session.commit()

    elif choice == 2:
        name = input("Enter bank name: ")
        address = input("Enter bank address: ")
        bank_code = int(input("Enter bank code: "))
        swift_code = input("Enter SWIFT code: ")
        bank = Bank(name=name, address=address, bank_code=bank_code, swift_code=swift_code)
        session.add(bank)
        session.commit()

    elif choice == 3:
        number = input("Enter account number: ")
        balance = 0
        persons = session.query(Person).all()
        for person in persons:
            print(person)
        person_id = input("Choose person ID: ")
        banks = session.query(Bank).all()
        for bank in banks:
            print(bank)
        bank_id = input("Choose bank ID: ")
        account = Account(number=number, balance=balance, person_id=person_id, bank_id=bank_id)
        session.add(account)
        session.commit()

    elif choice == 4:
        accounts = session.query(Account).all()
        for account in accounts:
            print(account)
        account_id = int(input("Choose account ID: "))
        # selected_account = session.query(Account).get(account_id)
        selected_account = session.get(Account, account_id)
        amount = float(input("Enter income/expense amount (use - for expense): "))
        selected_account.balance += amount
        transaction = Transaction(amount=amount, account_id=account_id)
        session.add(transaction)
        session.commit()


        # in future create new table History of Transactions. With amount and bank account ID.

    elif choice == 5:
        persons = session.query(Person).all()
        for person in persons:
            print(person)

    elif choice == 6:
        banks = session.query(Bank).all()
        for bank in banks:
            print(bank)

    elif choice == 7:
        accounts = session.query(Account).all()
        for account in accounts:
            print(account)

    elif choice == 8:
        account_id = int(input("Choose account ID: "))
        results = session.query(Transaction).filter_by(account_id=account_id).all()
        for result in results:
            print(result.amount)
        session.commit()

    elif choice == 9:
        print("Exiting the program.")
        break
    else:
        print("Input incorrect, try to choose another number")


