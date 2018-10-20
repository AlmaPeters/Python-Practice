# Script to calculate tip
bill = float(input("How much was the bill? "))
service = int(input("How was the service? (poor=1, good=2, great=3)? "))
region = str.upper(input("What Geography are you in (Europe= E, North America = NA, Japan = J, Other = O)? "))
tip_matrix = [["E", 0, 0.1, 0.15],
             ["NA", 0.1, 0.15, 0.2],
            ["JA", 0, 0, 0],
            ["O", 0, 0.1, 0.15]]

if service <1 or service > 3:
    print("Invalid input for service. Will assume good service")
    service = 2

# Verify Region and get multiplier
region_index = 0
while region_index < 4:
    if tip_matrix[region_index][0] == region: break
    region_index += 1
        
if region_index == 4:
    region_index = 3
    print("Unknown region, default tip calculations will be used")
    
tip_amount = round(bill* tip_matrix[region_index][service], 2)

print ("Tip amount:", tip_amount, "(" + str((tip_matrix[region_index][service] * 100)) + "%)")
print ("Total Bill is: ", (tip_amount + bill))




              
              
