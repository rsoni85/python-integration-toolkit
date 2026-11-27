def main():
    invoice_batch = [
        {"vendor" : "Lumen", "amount" : 12500, "terms" : "net30"},
        {"vendor" : "Zayo", "amount" : 800, "terms" : "due"},
        {"vendor" : "Zayo", "amount" : -50, "terms" : "net60"},
        {"vendor" : "", "amount" : 500, "terms" : "net30"},
        {"vendor" : "Lumen", "amount" : 5000, "terms" : "NET60"},
        {"vendor" : "Comcast", "amount" : 9999.99, "terms" : "net90"}
    ]

    print_line(invoice_batch)
    
    
def approval_status(invoice_amount):
    if invoice_amount <= 0:
        return("Error: amount must be greater than zero.")
        
    elif invoice_amount > 10000:
        return("Needs manager approval.")
    else :
        return("Auto approved.")


def describe_terms(payment_terms):
    match payment_terms.lower():
            case "net30":
                return("Payment due in 30 days")
            case "net60":
                return("Payment due in 60 days")
            case "due":
                return("Payment due immediately")
            case _:
                return("Warning: Unknown payment term")



def print_line(invoice_batch):
    for invoice in invoice_batch:
        status = approval_status(invoice["amount"])
        terms = describe_terms(invoice["terms"])
        print (f"{invoice["vendor"]} | ${invoice["amount"]:,.2f} | {terms} | {status}")


main()