""" Build a Budget App
In this lab, you will build a simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should have a Category class that accepts a name as the argument.

The Category class should have an instance attribute ledger that is a list, and contains the list of transactions.

The Category class should have the following methods:

A deposit method that accepts an amount and an optional description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
A withdraw method that accepts an amount and an optional description (default to an empty string). The method should store in ledger the amount passed in as a negative number, and should return True if the withdrawal succeeded and False otherwise.
A get_balance method that returns the current category balance based on ledger.
A transfer method that accepts an amount and another Category instance, withdraws the amount with description Transfer to [Destination], deposits it into the other category with description Transfer from [Source], where [Destination] and [Source] should be replaced by the name of destination and source categories. The method should return True when the transfer is successful, and False otherwise.
A check_funds method that accepts an amount and returns False if it exceeds the balance or True otherwise. This method must be used by both the withdraw and transfer methods.
When a Category object is printed, it should:

Display a title line of 30 characters with the category name centered between * characters.
List each ledger entry with up to 23 characters of its description left-aligned and the amount right-aligned (two decimal places, max 7 characters).
Show a final line Total: [balance], where [balance] should be replaced by the category total.
Here is an example usage:

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
And here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
You should have a function outside the Category class named create_spend_chart(categories) that returns a bar-chart string. To build the chart:

Start with the title Percentage spent by category.
Calculate percentages from withdrawals only and not from deposits. The percentage should be the percentage of the amount spent for each category to the total spent for all categories (rounded down to the nearest 10).
Label the y-axis from 100 down to 0 in steps of 10.
Use o characters for the bars.
Include a horizontal line two spaces past the last bar.
Write category names vertically below the bar.
This function will be tested with up to four categories.

Make sure to match the spacing of the example output exactly:

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
"""

import math

class Category:

  def __init__(self,category):
    self.category=category
    self.ledger=[]

  def __str__(self):
    left=math.floor((30-len(self.category))/2)
    right=30-len(self.category)-left
    stri=left*'*'+self.category+right*'*'+"\n"
    for item in self.ledger:
      pt1=item["description"][0:23]+(23-len(item["description"][0:23]))*" "
      pt2=(7-len("{:.2f}".format(item["amount"])))*" "+"{:.2f}".format(item["amount"])
      hlp=pt1+pt2
      stri=stri+hlp+"\n"
    total="Total: "+"{:.2f}".format(self.get_balance())
    stri=stri+total
    return stri

  def deposit(self,amount,description=""):
    dic={}
    dic['amount']=amount
    dic['description']=description
    self.ledger.append(dic)
    

  def withdraw(self,amount,description=""):
    dic={}
    if self.check_funds(amount):
      dic['amount']=-amount
      dic['description']=description
      self.ledger.append(dic)
      return True
    return False

  def transfer(self,amount,other_cat):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to "+other_cat.category)
      other_cat.deposit(amount,"Transfer from "+self.category)
      return True
    return False

  def get_balance(self):
    balance=0
    for item in self.ledger:
      balance = balance+item['amount']
    return balance

  def check_funds(self,amount):
    if amount > self.get_balance():
      return False
    return True

def create_spend_chart(categories):
   p=[]
   for cat in categories:
     c_s=0
     for item in cat.ledger:
       if item["amount"]<0:
         c_s+=item["amount"]*(-1)
     p.append(c_s)
   t_s=sum(p)
   for i in range(len(p)):
     p[i]=10*math.floor(10*p[i]/t_s)

   st="Percentage spent by category"+"\n"
   for i in range(100,-1,-10):
     st+=(3-len(str(i)))*" "+str(i)+"|"
     for k in range(len(p)):
       if p[k] >=i:
         st+=" o "
       else:
         st+=3*" "
     st+=" "+"\n"
   st+=4*" "
   for i in range(len(p)):
     st+=3*"-"
   st+="-"+"\n"+" "

   maxi=0
   for cat in categories:
     if len(cat.category)>maxi:
       maxi=len(cat.category)
   cats=[]
   for cat in categories:
     cats.append(cat.category+(maxi-len(cat.category))*" ")
   tl=""
   for i in range(maxi):
     tl+=4*" "
     for j in range(len(cats)):
       tl+=cats[j][i]+2*" "
     if i < maxi-1:
       tl+="\n"+" "

   st+=tl
   return st
