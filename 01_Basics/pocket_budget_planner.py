income=int(input("enter your total monthly income or pocket money : "))
category=int(input("how many categories of expenses ? "))
i=0
expence=[]
name=[]
percentage=[]
while i<category:
    c= {
        "name":input("enter name : "),
        "amount":int(input("enter amount : "))
    }
    i+=1
    name.append(c["name"])
    expence.append(c["amount"])
    p=(c["amount"]/income)*100
    percentage.append(p)
total=sum(expence)
print(f"total expence = {total}")

saving=income-total
total_per=sum(percentage)
if saving < income * 0.2:
    print("⚠️ Warning: You’re spending over 80% of your income!")

saving_p=100-total_per
print(f"total saving : {saving} percentage {saving_p}")
for i in range(category):
    print(name[i], ":", percentage[i])

    