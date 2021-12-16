while True:
  currentPrice = float(input("What is the current price of the stock?"))
          priceAtPurchase = float(input("What was the price of the stock when you purchased it?"))
          amountOfStock = float(input("How much stock did you buy, in dollars?"))

          yesOrNo = input("In yes or no, has the stock fallen below the price you bought it at?")
          yesOrNo = yesOrNo.lower()

          quotient = priceAtPurchase/currentPrice
          quotientOne = (1 - quotient)
          newQuotient = (quotientOne + 1) * amountOfStock

          if yesOrNo == "no":
              if quotient < 1:
                  print("Your position is now valued at $" + str(newQuotient) + ".")

              elif quotient >=1:
                  quotient = quotient * amountOfStock
                  print("Your position is now valued at $" + str(quotient) + ".")
              else:
                  print("The value you've inputed is incompatible.")

          elif yesOrNo == "yes":
              amountOfDrop = amountOfStock - newQuotient
              newAmount = amountOfStock - amountOfDrop
              print("Your position is now valued at $" + str(newAmount) + ".")
          else:
              print("Does not compute...")
