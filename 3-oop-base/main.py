

# class User:
#     def __init__(self, name: str, balance: float) -> None:
#         self.name = name
#         self.__balance = balance

#     def get_balance(self) -> float:
#         return self.__balance
    
#     def deposit(self, value: float) -> None:
#         if value > 0:
#             self.__balance += abs(value)
#         else:
#             raise ValueError("Deposit amount must be positive")
        
#     def withdraw(self, value: float) -> None:
#         if 0 < value <= self.__balance:
#             self.__balance -= abs(value)
#         else:
#             raise ValueError("Not enough balance")

# u = User("Alice", 100.0)
# u.deposit(50.0)
# print(u.get_balance())  # Output: 150.0
# u.withdraw(30.0)
# print(u.get_balance())  # Output: 120.0
# print(u.__dict__) 
# u.__balance = 1000.0  # This will not change the actual balance due to name mangling
# print(u.__dict__)


# class User:
#     def __init__(self, name: str, email: str) -> None:
#         self.name = name
#         self.email = email  
    
#     def get_info(self) -> str:
#         return f"Name: {self.name}, Email: {self.email}"

# class Student(User):
    
#     def watch_video(self):
#         print(f"{self.name} is watching a video.")

# class Mentor(User):
   
#     def check_homework(self):
#         print(f"{self.name} is checking homework.")

# student = Student("Alice", "alice@example.com")
# mentor = Mentor("Bob", "bob@example.com")
# print(student.get_info())  # Output: Name: Alice, Email:
# print(mentor.get_info())   # Output: Name: Bob, Email:
# student.watch_video()      # Output: Alice is watching a video. 
# mentor.check_homework()    # Output: Bob is checking homework.  

# class Light:

#     def turn_on(self):
#         print("Light is turned on.")

# class Music:

#     def play(self):
#         print("Music is playing.")

#     def turn_on(self):
#         print("Music is turned on.")

# class SmartHome(Light, Music):

#     def activate(self):
#         print("Activating smart home...")
#         self.turn_on()
#         # self.play()


# home = SmartHome()
# home.activate()  # Output: Light is turned on. Music is playing.
# print(SmartHome.__mro__)  # Output: (<class '__main__.SmartHome'>, <class '__main__.Light'>, <class '__main__.Music'>, <class 'object'>)


# class Order:

#     def __init__(self, number: int, total: float):
#         self.number = number
#         self.total = total
#         print(f"Order {self.number} with total {self.total} created.")

#     def process(self):
#         print("Processing order...")
    

# class EmailOrder(Order):

#     def __init__(self, number: int, total: float, email: str):
#         super().__init__(number, total)  # Call the constructor of the parent class
#         self.email = email
#         print(f"Email order will be sent to {self.email}.")

#     def process(self):
#         super().process()  # Call the process method of the parent class
#         print("Processing email order...")

# e = EmailOrder(1, 100.0, "alice@example.com")
# e.process()

# class Payment:
#     def pay(self, amount: float):
#         raise NotImplementedError("Метод pay должен быть реализован в подклассе")


# class CardPayment(Payment):

#     def pay(self, amount: float):
#         print(f"Processing card payment of {amount}.")

# class CryptoPayment(Payment):

#     def pay(self, amount: float):
#         print(f"Processing crypto payment of {amount}.")

# class ApplePay(Payment):

#     def pay(self, amount: float):
#         print(f"Processing Apple Pay payment of {amount}.")

# payments = [CardPayment(), CryptoPayment(), ApplePay()]

# for p in payments:
#     p.pay(100.0)

class Notifaction:
    def __init__(self, sender):
        self.sender = sender

    def send(self, message: str):
        self.sender.send(message)
    
    def get_acknowledgment(self):
        pass

class EmailSender():
    def send(self, message: str):
        print(f"Sending email: {message}")


notification = Notifaction(EmailSender())
notification.send("message")