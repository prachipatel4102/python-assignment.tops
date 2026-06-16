#Q1 Create three variables in Python named item_price, delivery_fee, and coupon_discount, and assign them values representing a Swiggy order (e.g., 250, 30, 20). Print each variable.
item_price=250
delivery_fee=30
coupan_discount=20
print("item price:",item_price)
print("delivery fee",delivery_fee)
print("coupan discount:",coupan_discount)

#Q2 Write a Python script that uses indentation correctly to check if a Flipkart product's price is above 1000; if yes, print 'Eligible for free delivery', else print 'Delivery charges apply'.<br><br><em><strong>Hint:</strong> Use an if-else block and make sure your indentation is consistent.</em>
price=1200
if price>1000:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")

#Q3 Add both single-line and multi-line comments in your script explaining what each section does, using # for single-line and triple quotes for multi-line comments.
#this variable store the product price
price=1200
"""this program checks whether the product is eligible for free delivery or not"""

#Q4 Create variables for an IPL match: team_name, runs_scored, and overs_played. Assign appropriate values and print them using the correct naming conventions for Python variables.<br><br><em><strong>Constraint:</strong> Use snake_case for all variable names.</em>
team_name="Gujarat titans"
runs_scored=185
overs_played=20.0
print("Team Name:",team_name)
print("Runs Scored:",runs_scored)
print("Overs Played:",overs_played)