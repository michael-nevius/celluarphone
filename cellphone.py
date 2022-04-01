class Cellphone:
    def __init__(self, model) -> None:
        self.model = model
        self.number = "800-919-8874"
        self.contacts = {"Bill" : "800-919-3846", "Bubba" : "800-919-8961", "Hank" : "800-919-3106", "Steve" : "800-919-4582"}
        self.messages = []
        self.on_vibrate = False
    def receive_text_message (self, contact, message):
        print(f"New message from: {contact}. Message: {message}")
        self.messages.append(message) 
    def toggle_vibrate_setting (self):
        if self.on_vibrate == False:
            self.on_vibrate = True
            print("pst i'm vibrating")
        else:
            self.on_vibrate = False
            print("Vibrate turned off.")
    def create_text_message (self, to, message):
        print(f"To: {to}. Message: {message}")