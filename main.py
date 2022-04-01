from cellphone import Cellphone

myphone = Cellphone("S21+")
print(myphone.contacts)

myphone.receive_text_message("Hank", "what's going on over at your house I see a bunch of ducks")
myphone.receive_text_message("Steve", "have you seen my flux capacitor")
print(myphone.messages)

myphone.create_text_message("Bill", "wanna go play catch?")
myphone.toggle_vibrate_setting()
myphone.toggle_vibrate_setting()
print(myphone.on_vibrate)