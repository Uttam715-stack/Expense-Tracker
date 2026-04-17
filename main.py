#Expense Tracker Project
expenses = []
print("---Welcome to the Expense Tracker---")

while True:
   print("===Menu===")
   print("1. Add Expense")
   print("2.View all Expenses")
   print("3.View total expenses")
   print("4. Exit")

   choice = int(input("Enter your choice(1-4): "))
   
   #Add Expense
   if choice == 1:
      amount = float(input("Enter amount:"))
      category = input("Enter category(food,travel,books,etc):")
      date = input("Enter date(YYYY-MM-DD):")
      Note = input("Enter note(optional):")
      expense = {
         "amount": amount,
         "category": category,
         "date": date,
         "note": Note  
      }
      expenses.append(expense)
      print("\nExpense added successfully!")
    #View all Expenses
   elif choice == 2:
            if len(expenses) == 0:
                print("\nNo expenses added yet.")
            else:
                 print("\n==All expenses==")
                 count = 1
                 for each_expense in expenses:
                       print(f"expense {count} -> Amount: {each_expense['amount']}, Category: {each_expense["category"]}, Date: {each_expense["date"]}, Notes: {each_expense["note"]}")
                 count += 1    
   #View total expenses
   elif choice == 3:
      total_expenses = 0
      for each_expense in expenses:
         total_expenses += each_expense["amount"]
      print(f"\nTotal expenses: {total_expenses}")
   
   elif choice == 4:
      print("\nThank you for using the Expense Tracker. Goodbye!")
      break
   #Exit
   else:
      print("\nInvalid choice. Please enter a number between 1 and 4.")

     
        



   
          
       
