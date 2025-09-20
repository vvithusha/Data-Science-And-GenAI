user_name = "vithu2004@gmail.com"
pass_word = "vithu26"
count=0
attem=3

while count<=attem:

  user_name1 = input ("enter your user name:")
  pass_word1 = input ("enter your password:")

  if user_name == user_name1 and pass_word == pass_word1:
    print("login successfull")
    break
  else:
    count+=1
    print("please enter tha valid password")



