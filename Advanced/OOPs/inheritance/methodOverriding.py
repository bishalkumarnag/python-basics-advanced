"""
================================================================================
TOPIC: Method Overriding in Python
================================================================================
SHORT THEORY:
- Method Overriding occurs when a child class provides a specific implementation 
  for a method that is already defined in its parent class.
- Allows a child class to change or augment inherited behavior.
- Python determines which method to call at runtime based on the actual object type 
  (Dynamic Dispatch / Late Binding).

SYNTAX REFERENCE:
    class Parent:
        def process(self): ...

    class Child(Parent):
        def process(self):
            # Complete override or super().process() extension

KEY TAKEAWAYS / PITFALLS:
- Python does NOT support traditional Method Overloading (multiple methods with the 
  same name and different signatures). Defining two methods with the same name in the 
  same class overwrites the first one! Use default arguments or `functools.singledispatch`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

class PaymentProcessor:
    """Base payment gateway interface."""
    def process_payment(self, amount: float) -> str:
        return f"Processing generic baseline transaction of ${amount:.2f}"


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        # Override with PayPal specific processing
        fee = amount * 0.029 + 0.30
        return f"PayPal: Charged ${amount:.2f} + fee ${fee:.2f} via PayPal API"


class CryptoProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        # Override with blockchain specific processing
        gas_fee = 1.50
        return f"Crypto: Transferred ${amount:.2f} with gas fee ${gas_fee:.2f} to wallet address"


processors: list[PaymentProcessor] = [
    PaymentProcessor(),
    PayPalProcessor(),
    CryptoProcessor()
]

print("Dynamic Dispatch across overridden methods:")
for p in processors:
    print(" ", p.process_payment(100.0))
