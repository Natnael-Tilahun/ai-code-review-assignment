# Write your corrected implementation for Task 1 here.
def calculate_average_order_value(orders):
    """
    Calculates the average order value for all non-cancelled orders.
    
    Args:
        orders (list): A list of dictionaries representing orders. 
                       Each dictionary should have "amount" and "status" keys.
                       
    Returns:
        float: The average order value of non-cancelled orders. 
               Returns 0.0 if there are no non-cancelled orders or the list is empty.
    """
    if not orders:
        return 0.0

    valid_orders = [order for order in orders if order.get("status") != "cancelled"]
    
    if not valid_orders:
        return 0.0
        
    total_amount = sum(order.get("amount", 0) for order in valid_orders)
    return total_amount / len(valid_orders)
# Do not modify `task1.py`.
