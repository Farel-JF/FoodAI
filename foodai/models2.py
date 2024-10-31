# foodai/another_module.py

def calculate_total_price(cart_items):
    """
    Calculate the total price of items in the cart.

    Args:
        cart_items (list): A list of dictionaries, where each dictionary contains
                            'price' and 'quantity' keys.

    Returns:
        float: The total price calculated.
    """
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return total

# You can add more functions or classes as needed.
