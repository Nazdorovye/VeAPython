#   Price of the book is @24.95 EUR, but the book store offers @40% discount. Delivery costs @3.00 
# EUR for the first unit, then @0.75 EUR for each next unit.
#   What would be the sum cost for purchasing @60 book units?

#   Positions marked with @ symbol must be defined as according variables. Output result - sumcost 
# - variable, with calculated value.

price     = 24.95
discount  = 0.4
delivery0 = 3.0
delivery1 = 0.75
order     = 60.0

sumcost = ((price - price * discount) * order) + delivery0 + (delivery1 * (order - 1.0))

print("Sum cost:", sumcost)