def password_generator(username):
  lastitem = username[-1]
  removelastitem = username[:-1]
  password = lastitem + removelastitem
  begin = 0
  for letter in range(0, len(username)):
    if begin == len(username):
      password[0] = letter
    else:
      password[begin] = letter

    return str(password)



password_generator("testpassword")