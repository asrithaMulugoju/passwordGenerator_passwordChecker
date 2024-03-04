import random
import string
def generate_pwd():
  pwd=list()
  pwd.append(random.choice(string.ascii_lowercase))
  pwd.append(random.choice(string.ascii_uppercase))
  pwd.append(random.choice(string.digits))
  pwd.append(random.choice(string.punctuation))
  while len(pwd)<8:
    pwd.append(random.choice(string.ascii_letters+string.digits+string.punctuation))
  random.shuffle(pwd)
  return "".join(pwd)

def check_pwd(pwd):
  check_lower=any(char.islower() for char in pwd)
  check_upper=any(char.isupper() for char in pwd)
  check_digit=any(char.isdigit() for char in pwd)
  check_special=any(char in string.punctuation for char in pwd)
  if check_lower and check_upper and check_digit and check_special and len(pwd) >=8:
    return "Hurray! you've successfully generated password which meets all the conditions"
  else:
    return "Sorry! the generated password does not meet all the conditions"

generated_pwd=generate_pwd()
print("Generated password:", generated_pwd)

result=check_pwd(generated_pwd)
print(result)
  
