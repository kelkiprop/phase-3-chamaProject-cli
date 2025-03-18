from database import get_session, Base, engine
from models import Member, Contribution, Loan
from datetime import date

# Initialize the database
def initialize_db():
    Base.metadata.create_all(engine)
    print("Chama database initialized!")

# Add a new member
def add_member(name, phone):
    session = get_session()
    try:
        if session.query(Member).filter_by(phone=phone).first():
            print("Member with this phone number already exists.")
            return
        member = Member(name=name, phone=phone)
        session.add(member)
        session.commit()
        print(f"Member {name} added successfully!")
    finally:
        session.close()

# Add a contribution
def add_contribution(member_id, amount):
    session = get_session()
    try:
        member = session.get(Member, member_id)
        if not member:
            print("Member not found.")
            return
        contribution = Contribution(amount=amount, date=date.today(), member_id=member_id)
        session.add(contribution)
        session.commit()
        print("Contribution recorded successfully!")
    finally:
        session.close()

# Request a loan
def request_loan(member_id, amount):
    session = get_session()
    try:
        member = session.get(Member, member_id)
        if not member:
            print("Member not found.")
            return
        loan = Loan(amount=amount, date=date.today(), member_id=member_id)
        session.add(loan)
        session.commit()
        print("Loan request submitted successfully!")
    finally:
        session.close()

# View all members
def view_members():
    session = get_session()
    try:
        members = session.query(Member).all()
        for member in members:
            print(f"ID: {member.id}, Name: {member.name}, Phone: {member.phone}")
    finally:
        session.close()

# View all contributions
def view_contributions():
    session = get_session()
    try:
        contributions = session.query(Contribution).all()
        for contrib in contributions:
            print(f"ID: {contrib.id}, Member ID: {contrib.member_id}, Amount: {contrib.amount}, Date: {contrib.date}")
    finally:
        session.close()

# View all loans
def view_loans():
    session = get_session()
    try:
        loans = session.query(Loan).all()
        for loan in loans:
            print(f"ID: {loan.id}, Member ID: {loan.member_id}, Amount: {loan.amount}, Date: {loan.date}, Status: {loan.status}")
    finally:
        session.close()

# Delete a member
def delete_member(member_id):
    session = get_session()
    try:
        member = session.get(Member, member_id)
        if not member:
            print("Member not found.")
            return
        session.delete(member)
        session.commit()
        print("Member deleted successfully.")
    finally:
        session.close()

# Update loan status
def update_loan_status(loan_id, status):
    session = get_session()
    try:
        loan = session.get(Loan, loan_id)
        if not loan:
            print("Loan not found.")
            return
        loan.status = status
        session.commit()
        print("Loan status updated successfully.")
    finally:
        session.close()

# Run menu-driven program
if __name__ == "__main__":
    initialize_db()

    while True:
        print("\n1. Add Member\n2. Add Contribution\n3. Request Loan\n4. View Members\n5. View Contributions\n6. View Loans\n7. Delete Member\n8. Update Loan Status\n9. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter member name: ")
            phone = input("Enter phone number: ")
            add_member(name, phone)
        elif choice == "2":
            member_id = int(input("Enter member ID: "))
            amount = float(input("Enter contribution amount: "))
            add_contribution(member_id, amount)
        elif choice == "3":
            member_id = int(input("Enter member ID: "))
            amount = float(input("Enter loan amount: "))
            request_loan(member_id, amount)
        elif choice == "4":
            view_members()
        elif choice == "5":
            view_contributions()
        elif choice == "6":
            view_loans()
        elif choice == "7":
            member_id = int(input("Enter member ID to delete: "))
            delete_member(member_id)
        elif choice == "8":
            loan_id = int(input("Enter loan ID: "))
            status = input("Enter new status (approved/rejected/pending): ")
            update_loan_status(loan_id, status)
        elif choice == "9":
            print("Exiting application.")
            break
        else:
            print("Invalid choice, try again.")
