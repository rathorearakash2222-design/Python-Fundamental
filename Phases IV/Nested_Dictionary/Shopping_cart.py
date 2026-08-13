cart = {}

while True:

    print("\n===== SHOPPING CART =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Quantity")
    print("4. Display Cart")
    print("5. Total Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

            product = input("Enter product name: ").strip()
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))

            if product in cart:
               print("Product already exists!")
            else:
               cart[product] = {
               "price": price,
               "quantity": quantity
            }

            print("Product added successfully!")

    elif choice == "2":
    
        product = input("Enter product name: ").strip()

        if product in cart:
             del cart[product]
             print("Product removed successfully!")
        else:
             print("Product not found!")    
          
    elif choice == "3":

        product = input("Enter product name: ").strip()

        if product in cart:
            new_quantity = int(input("Enter new quantity: "))
            cart[product]["quantity"] = new_quantity
            print("Quantity updated successfully!")
        else:
            print("Product not found!")

    elif choice == "4":

      if not cart:
        print("Cart is empty!")
      else:
        print("\n===== SHOPPING CART =====")

        for product, details in cart.items():
            print("Product:", product)
            print("Price:", details["price"])
            print("Quantity:", details["quantity"])

    elif choice == "5":

        if not cart:
            print("Cart is empty!")
        else:
            total = 0

            for product, details in cart.items():
              price = details["price"]
              quantity = details["quantity"]
              subtotal = price * quantity
              total += subtotal

              print("\nProduct:", product)
              print("Price:", price)
              print("Quantity:", quantity)
              print("Subtotal:", subtotal)
              

              print("\n===== TOTAL BILL =====")
              print("Total Bill:", total)

    elif choice == "6":
        print("Thank you for using Shopping Cart!")
        break

    else:
        print("Invalid choice!")