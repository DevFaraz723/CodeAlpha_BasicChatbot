def chatbot():



    print("=======================")
    print("   Welcome To ChatBot   ")
    print("Type : 'Bye' To Exit ")
    print("=======================")


while True:
    user_input = input("You: ").lower().strip()

    if user_input == "hello":
        print("Bot: Hi How Can I Help You? ")

    elif user_input == "hi":
         print("Bot: Hello.")



    elif user_input == "how are you":
     print("Bot: I am Fine, thanks for asking.")


    elif user_input == "what is your name?":
      print("Bot: My Name is ChatBot.")

    elif user_input == "who created you":
     print("Bot: I was created by CodeAlpha Intern.")


    elif user_input == "help":
     print("Bot: You can say hello,ask my name, or ask How I am.")

    elif user_input == "bye":
     print("Bot: Goodbye! Have a great day.")

    else:
       print("Sorry, I don't understand that. ")

    chatbot()