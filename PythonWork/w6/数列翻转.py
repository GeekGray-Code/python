sequenceList=list(input().strip().split())

sequenceList1=sequenceList[1:len(sequenceList)+1]

sequenceList1.reverse()


for item in sequenceList1:
    print(item,end=" ")