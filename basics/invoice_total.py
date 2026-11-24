def main():

    vendor_name = input("Whats the Vendon Name? ")

    invoice_amount = float(input("Whats the Invoice amount? "))

    tax_rate = float(input("Whats the Tax rate percentage %? "))

    total_tax= tax_rate/100 * invoice_amount

    
    print("Vendor:", vendor_name )
    print(f"Subtotal: ${invoice_amount:,.2f}")
    print(f"Tax: ${total_tax:,.2f}")
    print(f"Total:  ${calculate_total(invoice_amount, total_tax):,.2f}")


    


def calculate_total(invoice_amount,total_tax):
    
    
    total= invoice_amount + total_tax
    return total


main()