## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary=float(input("yearly_salary: "))
portion_saved=float(input("portion_saved: "))
cost_of_dream_home=float(input("cost_of_dream_home: "))
semi_annual_raise=float(input("semi_annual_raise: "))
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment=0.25
amount_saved=0

r=0.05

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
months=0
while amount_saved<cost_of_dream_home*portion_down_payment:
    if  (months>0 and months%6==0):
        yearly_salary=yearly_salary*(1+semi_annual_raise)
    
    monthly_saved=amount_saved*(r/12)
    monthly_deposit=(yearly_salary/12)*portion_saved
    amount_saved +=monthly_saved+monthly_deposit
    months+=1
print("输出月数：",months)