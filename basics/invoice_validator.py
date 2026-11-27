def main():
    vendor_name = input ("What's the vendor name? ")
    
    if vendor_name == "":
        print("Error: vendor name is required")
        return
    
    invoice_amount = float (input ("What's the Invoice Amount? "))
    payment_terms = input ("What's the payment terms? ").lower() 
    status = approval_status(invoice_amount) 
    print (status)
    match payment_terms:
        case "net30":
            print("Payment due in 30 days")
        case "net60":
            print("Payment due in 60 days")
        case "due":
            print("Payment due immediately")
        case _:
            print("Warning: Unknown payment term")     
    print (f"Vendor: {vendor_name} | Amount: ${invoice_amount:,.2f}")

def approval_status(invoice_amount):
    if invoice_amount <= 0:
        return("Error: amount must be greater than zero.")
        
    elif invoice_amount > 10000:
        return("Needs manager approval.")
    else :
        return("Auto approved.")


main()