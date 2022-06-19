
#Email validation Using Regex
from ast import pattern
import re

pattern = re.compile(r"[a-zA-Z0-9._%-]+@[a-zA-Z0-9.]+\.[a-z|A-Z]{2,}")

def emeil_checker():
  while True:
      input_email = input("Enter your email address:")
      if re.fullmatch(pattern,input_email):
         print("_______Your Email Address is Valid____________")
         user_name = input_email[:input_email.index("@")]
         domain = input_email[input_email.index("@")+1:]
         print(f'your user name is"{user_name}"and domain "{domain}"')
      break
  else:
      print("Please enter a vallid email")
      
      
if __name__ == "__main__":
    emeil_checker()          
