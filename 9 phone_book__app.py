class Contact:
      phone_directory = []

      def __init__(self,name,phone_number):
            self.name = name 
            self.phone = phone_number
            Contact.phone_directory.append(self)

            
      def show_contact(self):
            return f"Name: {self.name},Contact number :{self.phone}"
      

      @classmethod
      def show__all__contact(cls):
            if len(cls.phone_directory) == 0:
               print("No contats found in the directory")
            else:
                 for contact in cls.phone_directory:
                      print(contact.show_contact())
        
      @staticmethod
      def validate_phone_number(number):
           if len(number)>=8 and number.isdigit():
                return True
           else:
                return False
           



      @classmethod
      def search_contact(cls,search_name):
           for contact in cls.phone_directory:
                if contact.name.lower() == search_name.lower():
                     return contact.phone
                
           return f"No contact found for {search_name}"
           
      
n_contacts = int(input("How many contacts do you want to add? : ")) 

for i in range(n_contacts):
     name = input("Enter the Name of the contact :  ")
     phone_number = input("Enter the phone Number : ")
     if Contact.validate_phone_number(phone_number):
          Contact(name,phone_number)
     else:
          print(f"Invalid phone number for {name} , phone number should be atleast 8 degits and should only contails the numbers ")




# c1 = Contact("john",97524979858)  
# c2 = Contact("Sam",9458721644) 
# c3 = Contact("Deepu",9489844852)
# print(Contact.phone_directory)  
# print(c1.show_contact())
# print(c2.show_contact())
# c1.show__all__contact()
Contact.show__all__contact() ##if no object created so this is used 
# print(Contact.search_contact("john"))
# print(Contact.search_contact("Sam"))
# print(Contact.search_contact("Deepu"))
# print(Contact.search_contact("Mark"))
# print(Contact.search_contact("JOHN"))




