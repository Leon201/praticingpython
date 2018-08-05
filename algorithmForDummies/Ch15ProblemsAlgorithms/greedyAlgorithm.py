def change(to_be_changed, denomination):
    resulting_change = list()
    for bill in denomination:
        while to_be_changed >= bill:
            resulting_change.append(bill)
            to_be_changed = to_be_changed - bill
    return resulting_change, len(resulting_change)

currency = [100, 50, 20, 10, 5, 1]
amount = 367
print('Change: %s (using %i bills)'
      % (change(amount, currency)))

print('Change: %s (using %i bills)'
      % (change(30, [25, 15, 1])))

