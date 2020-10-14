#I imported the requests, time and pickle function.
#my resources for learning python 1): https://www.youtube.com/watch?v=_uQrJ0TkZlc    2): https://www.youtube.com/watch?v=rfscVS0vtbw 3):i did basic programing in my previous study and i self studied java 4): on a codio by my tutor mathew england
import requests
import time
from datetime import datetime
import pickle
print("Hello i will be assisting you today i can make small talk a bit and perform other minor talks\n")
# i set initialise to 1 to erase data from the repository.
# if you set initialise as 0 it will keep the data saved.
# i learned how to use pickle from my 4000CEM lab tutor dorian florescu and mathew england using pickle.
initialise = 1
if initialise:
    repository = {}
else:
   with open('repository.pickle', 'rb') as f:
      repository = pickle.load(f) #data is loaded


def Main_menu():
    print('You can return to the main menu by entering "Menu" or exit program by typing "Q".\n')
    User_choice = input("Do you have a account Yes/No\n").lower()
    print("")
    if User_choice == "yes":
        existing_user()
    elif User_choice == "no":
        New_User()
    elif User_choice == "menu":
       menu()
    elif User_choice == "q":
       quit()

    else:
       Main_menu()

    with open('repository.pickle', 'wb') as f:
        pickle.dump(repository, f) #data is dumped



def New_User(): #function to make a new account
    sign_up = input("Please enter a username for your account ")
    if sign_up in repository:
        sign_up_failure = input(
            '\nThis account already exists\n\nif you do have an account type: "Yes" to renter your account details\n\nif you would like to continue making a account then press any key to continue making a account.\n\n').lower()
        print("")

        if sign_up_failure == "yes":
            existing_user()

        else:
            New_User()
    else:
        password = input("Please enter a password ")
        repository[sign_up] = password
        print("\nnew user created\nsignin with your new User account\n")
        existing_user()



def existing_user(): #function to use a existing account
    login = input("please enter your username ")
    Password = input("Enter password ")

    if login in repository and repository[login] == Password:
        print("\nLogin successful!\n\n")
        time.sleep(2)
        menu()


    else:
        login_failure = input(
            '\nUser does not exist Or wrong password.\nType "Yes" to Try again Or Any key to Return to main menu \n\n').lower()
        print("")
        if login_failure == "yes":
            existing_user()

        else:
            Main_menu()

 # i learned how to use api from https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236, https://requests.readthedocs.io/en/master/ and https://www.youtube.com/watch?v=pxofwuWTs7c
 
#function to search recipies
def recipe():
    url =  'http://www.recipepuppy.com/api/?i='   #refrence: http://www.recipepuppy.com/about/api/
    print('if you want to find the recipe of something for example pizza then enter "pizza".\n\nwe will give you ingrediants to make the pizza and webisites that help you make it isnt that cool.')
    url_input = input("please enter the recpie that you would like to search ")
    Final_url = url + url_input
    request = requests.get(Final_url)
    print(request.text)
    time.sleep(2)
    menu()
#function that generates jokes
def joke():
    url =  'https://official-joke-api.appspot.com/random_joke'   #refrence: https://github.com/15Dkatz/official_joke_api

    request = requests.get(url)
    print(request.text)
    time.sleep(2)
    menu()
#function that tells the weather 
def coventry_weather():
    url =  'https://www.metaweather.com/api/location/17044/'    #refrence: https://www.metaweather.com/api/

    request = requests.get(url)
    print(request.text)
    time.sleep(2)
    menu()







def menu():# main function and starting point
    talk = { #dictionary for storing responses to users input
        "hello": "Hello i am here to help you\n ",
        "hi": "hey how's it going?",
        "hey": "oh hello",
        "im good": "that's good",
        "How's the weather": "its beyond my capabilities to know that but i think itd be nice",
        "can i have something to eat": "why not",
        "who am i": "you are a respected user",
        "should i order a pizza": "maybe ",
        "have you eaten": "i don't eat really",
        "bye": "good bye",
        "im going away": "bye",
        "should i eat": " you can ",
        "can i have some food": "yes you can",
        "do you guys do take away": "yes we do sometimes ",
        "which is the best place for pizza": "our pizza is quite good i think ",
        "that smells nice": "its our special pizza sauce",
        "are you ok": "i think i am ",
        "i hate you": "why that?",
        "i love you": "i love you too",
        "whats your name?": "a name? i dont think i have a name but im your personal assistant",

    }


    choice = input("""
  Hello how can we help you?

  we can help you in various was heres a few

  A: Do you want to order a pizza?
  B: Do you need any information about us?
  C: Do you want to login or signup?
  Q: Would you like to exit this program?

  we can also tell you about food recipies. 

  to find a recipe type "Recipe" 

  if you want help from the choices above please enter the respective choice.
  Please enter your choice: """).lower()
    #below i used for loops combined with the split function.
    #i learned for loops from my 4000CEM lab tutor dorian florescu
    words = choice.split()
    choiceA = ["a"]
    choiceB = ["b"]
    for i in choiceA:
        for m in choiceB:
          if i in words:
            pizza()
          elif m in words:
              help()
          elif choice == "c" or choice == "C":
                Main_menu()
          elif choice == "q" or choice == "quit":
                print("\nGood bye (^_^)")

                quit()

          elif choice == "time" or choice == "date":
                today = datetime.now()
                print("")
                print(today)
                print("")
                time.sleep(2)
                menu()
          elif choice == "weather":
              coventry_weather()
          elif choice == "joke":
              joke()

          elif choice == "recipe":
              recipe()

          elif choice in talk:
                Out_put = (talk[choice])
                print("\n" + Out_put)
                time.sleep(2)
                menu()
          elif choice != talk:

                print("\n!!! Thats not a   option try again !!! \n")
                time.sleep(2)
                menu()



def pizza():
        #i used while loops to loop in a statement instead of recursions
        #i learned while loops from my 4000CEM lab tutor dorian florescu
        flag0 = 1
        while flag0:
            print("\nwhich pizza would you like")
            sub_choicea = input("""
                        The pizzas available are:

                        Chicken
                        Beef
                        Vegan



                        if you want to order from the choices above please enter the respective choice.
                        Please enter your choice: """).lower()
            menu_1 = ["chicken", "beef", "vegan"]

            sub_wordsa = sub_choicea.split()

            for n in sub_wordsa:
                if n in menu_1:
                    flag0 = 0
                    flag = 1
                    while flag:
                     print("\n                        Which you like any toppings with that?")
                     sub_choicea1 = input("""
                                             Extra toppings include:

                                             Chicken
                                             Beef
                                             vegetables
                                             Cheese

                                             .

                                             if you want to order from the choices above please enter the respective choice.
                                             Please enter your choice: """).lower()
                     sub_menu1 = ["chicken", "beef", "vegetables", "cheese"]
                     sub_wordsa1 = sub_choicea1.split()
                     flag = 0


                     for m in sub_wordsa1:
                      if m in sub_menu1:
                          price = (10)
                          flag2 = 1
                          while flag2:
                              Size = input("""
                                                                              which size would you like each size comes with a price?
    
                                                                              Small
                                                                              Medium
                                                                              Large
                                                                              Extra large
    
    
    
                                                                              please select the size of the pizza you would like to order.
                                                                              Please enter your choice: """).lower()
                              if Size == "small" :
                                 flag2 = 0
                                 print("\n                                             your order is a " + sub_choicea + " pizza with extra " + sub_choicea1 + " toppings and the price is " + str(price) + "£")
                                 print('\n                                             are you happy with your order? if so enter "yes" to order. ')
                                 print('                                              if not type "menu" to return to the main menu')
                                 print('                                              if you wanna exit the program enter "q" or enter "quit." ')
                                 flag1 = 1
                                 while flag1:
                                     final_choice = input(
                                         "                                what would you like to do ").lower()
                                     if final_choice == "yes":
                                         print("\n                                your order has been taken")
                                         return sub_choicea + sub_choicea1 + str(price)
                                         flag1 = flag1 - 1

                                     elif final_choice == "menu":
                                         menu()
                                     elif final_choice == "q" or final_choice == "quit":
                                         quit()
                                     else:
                                         print("\n                        incorrect choice try again")
                                         time.sleep(2)
                                         flag1 = flag1 + 1

                              elif Size == "medium":
                                  flag2 = 0
                                  price = price * 2
                                  print(
                                     "\n                                             your order is a " + sub_choicea + " pizza with extra " + sub_choicea1 + " toppings and the price is " + str(price) + "£")
                                  print(
                                     '\n                                             are you happy with your order? if so enter "yes" to order. ')
                                  print(
                                     '                                              if not type "menu" to return to the main menu')
                                  print(
                                     '                                              if you wanna exit the program enter "q" or enter "quit." ')
                                  flag1 = 1
                                  while flag1:
                                      final_choice = input(
                                         "                                what would you like to do ").lower()
                                      if final_choice == "yes":
                                          print("\n                                your order has been taken")
                                          return sub_choicea + sub_choicea1 + str(price)
                                          flag1 = flag1 - 1

                                      elif final_choice == "menu":
                                           menu()
                                      elif final_choice == "q" or final_choice == "quit":
                                           quit()
                                      else:
                                          print("\n                        you,ve entred inccorect information")
                                          time.sleep(2)
                                          flag1 = flag1 + 1
                              elif Size == "large":
                                  flag2 = 0
                                  price = price * 3
                                  print(
                                      "\n                                             your order is a " + sub_choicea + " pizza with extra " + sub_choicea1 + " toppings and the price is " + str(
                                          price) + "£")
                                  print(
                                      '\n                                             are you happy with your order? if so enter "yes" to order. ')
                                  print(
                                      '                                              if not type "menu" to return to the main menu')
                                  flag1 = 1
                                  while flag1:
                                      final_choice = input(
                                         "                                what would you like to do ").lower()
                                      if final_choice == "yes":
                                          print("\n                                your order has been taken")
                                          return sub_choicea + sub_choicea1 + str(price)
                                          flag1 = flag1 - 1

                                      elif final_choice == "menu":
                                           menu()
                                      elif final_choice == "q" or final_choice == "quit":
                                           quit()
                                      else:
                                          print("\n                        incorrect choice try again")
                                          time.sleep(2)
                                          flag1 = flag1 + 1

                              elif Size == "extra large":
                                  flag2 = 0
                                  price = price * 4
                                  print(
                                      "\n                                             your order is a " + sub_choicea + " pizza with extra " + sub_choicea1 + " toppings and the price is " + str(
                                          price) + "£")
                                  print(
                                      '\n                                             are you happy with your order? if so enter "yes" to order. ')
                                  print(
                                      '                                              if not type "menu" to return to the main menu')
                                  print(
                                      '                                              if you wanna exit the program enter "q" or enter "quit." ')
                                  flag1 = 1
                                  while flag1:
                                      final_choice = input(
                                         "                                what would you like to do ").lower()
                                      if final_choice == "yes":
                                          print("\n                                your order has been taken")
                                          return sub_choicea + sub_choicea1 + str(price)
                                          flag1 = flag1 - 1

                                      elif final_choice == "menu":
                                           menu()
                                      elif final_choice == "q" or final_choice == "quit":
                                           quit()
                                      else:
                                          print("\n                        incorrect choice try again")
                                          time.sleep(2)
                                          flag1 = flag1 + 1
                              else:
                                  print("\n                        you,ve entred inccorect information")
                                  time.sleep(2)
                                  flag2 = flag2 + 1

                      else:
                             print("\n                                             incorrect choice try again")
                             time.sleep(2)
                             flag = flag + 1




                else:

                    print("\n                                             you,ve entred inccorect information")
                    time.sleep(2)
                    flag0 = flag0 + 1

def help():

        choice1 = input("""
           what information would you like?



           A: would you like our number?
           B: Do you wanna know our address?


           if you want help from the choices above please enter the respective choice.
           Please enter your choice: """).lower()
        print("")

        word1 = choice1.split()
        List = ["a", "number"]
        List2 = ["b", "address"]

        for i in List:#function to tell the date and time
             for n in List2:
                if i in word1:
                    print("\n                sorry we don't have a number as where a chatbot ")
                    time.sleep(2)
                    menu()
                elif n in word1:
                 print("\n                        We are currently located in coventry")
                 time.sleep(2)
                 menu()
        else:
           print("you,ve entred inccorect information")
           time.sleep(2)
           help()
menu()



