
tables = "file io/tables"  
for i in range(2,21):
    with open(f"{tables}/table_{i}.txt" , "w") as f:
        for j in range(1, 11):
            f.write(f"{j} X {i} = {j*i}\n")
    