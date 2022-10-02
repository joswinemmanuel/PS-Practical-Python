money_owed = float(input("How much money do you owe, in $ ?? : "))
annual_percent = float(input("What is the annual percentage rate ?? : "))
payment = float(input("What will your monthly payment be, in $ ?? : "))
months = int(input("How many months do you want to see results for ?? : ", end="\n\n"))

monthly_percent = (annual_percent / 100) / 12

for i in range(months):
    interest_paid = money_owed * monthly_percent
    money_owed += interest_paid

    if money_owed - payment <= 0:
        print(f"\nThe last payment is ${money_owed}")
        print(f"You paid off the loan in {i+1} months")
        break

    money_owed -= payment

    print(f"Paid ${payment} of which ${interest_paid} was interest", end=" ")
    print(f"Now you owe ${money_owed}")


# How much money do you owe, in $ ?? : 50000
# What is the annual percentage rate ?? : 3
# What will your monthly payment be, in $ ?? : 1000
# How many months do you want to see results for ?? : 56

# Paid $1000.0 of which $125.0 was interest Now you owe $49125.0
# Paid $1000.0 of which $122.8125 was interest Now you owe $48247.8125
# Paid $1000.0 of which $120.61953125000001 was interest Now you owe $47368.43203125
# Paid $1000.0 of which $118.421080078125 was interest Now you owe $46486.85311132812
# Paid $1000.0 of which $116.2171327783203 was interest Now you owe $45603.07024410644
# Paid $1000.0 of which $114.0076756102661 was interest Now you owe $44717.07791971671
# Paid $1000.0 of which $111.79269479929177 was interest Now you owe $43828.870614515996
# Paid $1000.0 of which $109.57217653628999 was interest Now you owe $42938.442791052286
# Paid $1000.0 of which $107.34610697763071 was interest Now you owe $42045.78889802992
# Paid $1000.0 of which $105.1144722450748 was interest Now you owe $41150.903370274995
# Paid $1000.0 of which $102.87725842568749 was interest Now you owe $40253.78062870068
# Paid $1000.0 of which $100.63445157175171 was interest Now you owe $39354.41508027243
# Paid $1000.0 of which $98.38603770068109 was interest Now you owe $38452.80111797311
# Paid $1000.0 of which $96.13200279493277 was interest Now you owe $37548.933120768044
# Paid $1000.0 of which $93.87233280192011 was interest Now you owe $36642.80545356996
# Paid $1000.0 of which $91.60701363392491 was interest Now you owe $35734.41246720389
# Paid $1000.0 of which $89.33603116800973 was interest Now you owe $34823.7484983719
# Paid $1000.0 of which $87.05937124592974 was interest Now you owe $33910.80786961783
# Paid $1000.0 of which $84.77701967404457 was interest Now you owe $32995.58488929187
# Paid $1000.0 of which $82.48896222322968 was interest Now you owe $32078.073851515102
# Paid $1000.0 of which $80.19518462878776 was interest Now you owe $31158.26903614389
# Paid $1000.0 of which $77.89567259035972 was interest Now you owe $30236.16470873425
# Paid $1000.0 of which $75.59041177183563 was interest Now you owe $29311.755120506084
# Paid $1000.0 of which $73.27938780126522 was interest Now you owe $28385.034508307348
# Paid $1000.0 of which $70.96258627076837 was interest Now you owe $27455.997094578117
# Paid $1000.0 of which $68.6399927364453 was interest Now you owe $26524.63708731456
# Paid $1000.0 of which $66.3115927182864 was interest Now you owe $25590.94868003285
# Paid $1000.0 of which $63.977371700082124 was interest Now you owe $24654.92605173293
# Paid $1000.0 of which $61.63731512933233 was interest Now you owe $23716.563366862265
# Paid $1000.0 of which $59.291408417155665 was interest Now you owe $22775.854775279422
# Paid $1000.0 of which $56.939636938198554 was interest Now you owe $21832.79441221762
# Paid $1000.0 of which $54.58198603054405 was interest Now you owe $20887.376398248165
# Paid $1000.0 of which $52.21844099562041 was interest Now you owe $19939.594839243786
# Paid $1000.0 of which $49.84898709810947 was interest Now you owe $18989.443826341896
# Paid $1000.0 of which $47.473609565854744 was interest Now you owe $18036.91743590775
# Paid $1000.0 of which $45.092293589769376 was interest Now you owe $17082.00972949752
# Paid $1000.0 of which $42.7050243237438 was interest Now you owe $16124.714753821263
# Paid $1000.0 of which $40.31178688455316 was interest Now you owe $15165.026540705816
# Paid $1000.0 of which $37.91256635176454 was interest Now you owe $14202.93910705758
# Paid $1000.0 of which $35.50734776764395 was interest Now you owe $13238.446454825224
# Paid $1000.0 of which $33.096116137063056 was interest Now you owe $12271.542570962287
# Paid $1000.0 of which $30.67885642740572 was interest Now you owe $11302.221427389693
# Paid $1000.0 of which $28.255553568474234 was interest Now you owe $10330.476980958168
# Paid $1000.0 of which $25.82619245239542 was interest Now you owe $9356.303173410564
# Paid $1000.0 of which $23.390757933526412 was interest Now you owe $8379.69393134409
# Paid $1000.0 of which $20.94923482836023 was interest Now you owe $7400.643166172451
# Paid $1000.0 of which $18.501607915431126 was interest Now you owe $6419.144774087882
# Paid $1000.0 of which $16.047861935219707 was interest Now you owe $5435.192636023102
# Paid $1000.0 of which $13.587981590057755 was interest Now you owe $4448.78061761316
# Paid $1000.0 of which $11.1219515440329 was interest Now you owe $3459.9025691571924
# Paid $1000.0 of which $8.649756422892981 was interest Now you owe $2468.5523255800854
# Paid $1000.0 of which $6.171380813950214 was interest Now you owe $1474.7237063940356
# Paid $1000.0 of which $3.6868092659850893 was interest Now you owe $478.4105156600208

# The last payment is $479.60654194917083
# You paid off the loan in 54 months