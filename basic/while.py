count = 0
while count < 5:
    if count <= 2:
        print(f"count is {count}")
        count += 1
        continue
    elif count == 3:
        break
