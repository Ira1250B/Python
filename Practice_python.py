import pandas as pd
contact_book=pd.read_excel(r"C:\Users\bhoga\OneDrive\Documents\Python_project.xlsx")
def Add_contact():#add new contact to existing contacts
  global contact_book
  cont_numb=int(input("Enter phone number of new contact\n"))
  name=input("Enter name of new contact\n")
  cat=input("Enter the category of contact: emergency or normal\n")
  if len(str(cont_numb)) != 10:
     print("INvalid contact number\n")
  elif cont_numb in contact_book['Phone Number'].values:
     print("Contact already exist\n")
  else:
      print("Contact added successfully!")
      new_contact={'Name':name,'Phone Number':cont_numb,'Category':cat}
      contact_book=contact_book._append(new_contact,ignore_index=True)
      contact_book.to_excel(r"C:\Users\bhoga\OneDrive\Documents\Python_project.xlsx",index=False)
  return contact_book
def Edit_contacts():#edit existing contact
  global contact_book
  cont_numb = int(input("Enter phone number of the contact you want to edit:\n"))
  if cont_numb in contact_book['Phone Number'].values:
        print("What do you want to edit?")
        print("1. Name")
        print("2. Category")
        print("3. Phone Number")
        
        choice = int(input("Enter your choice (1, 2, or 3): "))
        if choice == 1:#edits name of contact
            edit_name = input("Enter new name:\n")
            contact_book.loc[contact_book['Phone Number'] == cont_numb, 'Name'] = edit_name
            print("Name updated successfully!")    
        elif choice == 2:#edits category of contact
            edit_cat = input("Enter new category (emergency/normal):\n")
            contact_book.loc[contact_book['Phone Number'] == cont_numb, 'Category'] = edit_cat
            print("Category updated successfully!")    
        elif choice == 3:#edit number of the contact
            edit_num = int(input("Enter new phone number:\n"))
            contact_book.loc[contact_book['Phone Number'] == cont_numb, 'Phone Number'] = edit_num
            print("Phone number updated successfully!")    
        else:
            print("Invalid choice.")
        contact_book.to_excel(r"C:\Users\bhoga\OneDrive\Documents\Python_project.xlsx", index=False)    
  else:
    print("Contact not found.")    
    return contact_book
def Delete_contact():#delets a existing contact
  global contact_book
  cont_numb=int(input("Enter phone number  you want to delete\n"))
  print("Contact had been deleted")
  contact_book=contact_book[(contact_book['Phone Number']!=cont_numb)]
  contact_book.to_excel(r"C:\Users\bhoga\OneDrive\Documents\Python_project.xlsx",index=False)
  return contact_book
def Display_contacts():#user can see the saved contacts here
   global contact_book
   print(contact_book)
choice2=int(input("Enter '1'to add a new contact\n" 
                  "Enter '2' to edit contact\n " 
                  "Enter '3' to delete an existing contact\n"
                  "Eneter '4' to display the saved contact\n"))
if(choice2==1):
   Add_contact()
elif(choice2==2):
   Edit_contacts()
elif(choice2==3):
   Delete_contact()
elif(choice2==4):
   Display_contacts()


