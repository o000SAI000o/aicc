import time

def bot_delay(text):
    time.sleep(1)
    print("Bot:", text)

def main():
    print("Welcome to ShopSmart Customer Support!")
    name = input("User: Hi, may I know your name? \nYou: ")
    bot_delay(f"Hello {name}, how can I help you today?")
    
    while True:
        print("\nChoose a category:")
        print("1. Order Status")
        print("2. Return/Refund")
        print("3. Product Inquiry")
        print("4. Talk to Human Agent")
        print("5. Exit")
        choice = input("You: ")

        if choice == "1":
            order_id = input("Please enter your Order ID: ")
            bot_delay(f"Fetching status for Order ID: {order_id}...")
            bot_delay("Your order has been shipped and will arrive in 2-3 business days.")
        
        elif choice == "2":
            order_id = input("Enter your Order ID for return/refund: ")
            reason = input("Reason for return/refund: ")
            bot_delay("Processing your request...")
            bot_delay(f"Return request for Order ID {order_id} has been submitted.")
            bot_delay("Our team will review it and contact you within 24 hours.")
        
        elif choice == "3":
            product = input("Enter the product name: ")
            bot_delay(f"Looking up information for '{product}'...")
            bot_delay(f"'{product}' is currently in stock. Price: ₹499. Estimated delivery: 3-5 days.")
        
        elif choice == "4":
            bot_delay("Connecting you to a human agent...")
            bot_delay("Please wait while we transfer your chat.")
            break

        elif choice == "5":
            bot_delay(f"Thank you for contacting ShopSmart, {name}. Have a great day!")
            break

        else:
            bot_delay("Sorry, I didn't understand that. Please choose a valid option.")

if __name__ == "__main__":
    main()
