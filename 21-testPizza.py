
pizza = int(input("How many pizzas do you wish to oreder?:"))

if pizza<=6:
    totalPizzaPrice = pizza*17
    totalDeliFee = pizza * 2 
    totalPrice = totalPizzaPrice +  totalDeliFee
elif pizza>6 and pizza < 12:
    stage1 = pizza-6 
    stage1Price = 6*17
    stage2Price = stage1 *15
    
    totalPizzaPrice = stage1Price+ stage2Price
    
    deliFeeFor1 =6*2 
    deliFeeFor2 =stage1*1
    totalDeliFee = deliFeeFor1 + deliFeeFor2
    
    totalPrice = totalPizzaPrice + totalDeliFee 
    
else:
    stage1 = pizza-6 
    stage1Price = 6*17 
    
    deliFeeFor1 =6*2 
    deliFeeFor2 =5*1
    
    stage2 = stage1 - 5 
    stage2Price = 5*15
    
    stage3Price = stage2*13 
    
    totalPizzaPrice = stage1Price +stage2Price+stage3Price 
    totalDeliFee = deliFeeFor1+deliFeeFor2 
    
    totalPrice = totalPizzaPrice+totalDeliFee

print("Your pizzas cost ${0}, your delivery fee is ${1}.A total cost of ${2}"
      .format(totalPizzaPrice,totalDeliFee,totalPrice))