"""
================================================================================
TOPIC: The super() Proxy & Cooperative Inheritance
================================================================================
SHORT THEORY:
- `super()` returns a proxy object that delegates method calls to the next class 
  in the Method Resolution Order (MRO).
- Key use cases:
  1. Forwarding arguments to parent constructors (`super().__init__(...)`).
  2. Extending (rather than completely overwriting) parent method functionality.
  3. Enabling cooperative multiple inheritance without hardcoding parent class names.
- Zero-argument `super()` in Python 3 automatically infers current class and instance.

SYNTAX REFERENCE:
    class Child(Parent):
        def __init__(self, child_arg, *parent_args):
            super().__init__(*parent_args)  # Constructor forwarding
            self.child_arg = child_arg

        def action(self):
            super().action()                # Call parent action first
            # child-specific enhancement

KEY TAKEAWAYS / PITFALLS:
- Avoid hardcoding parent name calls like `Parent.__init__(self)` because it breaks 
  in multiple inheritance diamond hierarchies. Always use `super()`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

class Notification:
    """Base notification system."""
    def __init__(self, recipient: str) -> None:
        self.recipient = recipient

    def send(self, message: str) -> None:
        print(f"[BASE DISPATCH] Sending notification to: {self.recipient}")


class EmailNotification(Notification):
    """Specialized email notification using super()."""
    def __init__(self, recipient: str, subject: str) -> None:
        # Delegate recipient initialization to parent
        super().__init__(recipient)
        self.subject = subject

    def send(self, message: str) -> None:
        # Extend parent dispatch logic with email header
        super().send(message)
        print(f"[EMAIL] Subject: '{self.subject}' | Body: '{message}'")


class SMSNotification(Notification):
    """Specialized SMS notification using super()."""
    def __init__(self, recipient: str, sender_id: str) -> None:
        super().__init__(recipient)
        self.sender_id = sender_id

    def send(self, message: str) -> None:
        super().send(message)
        print(f"[SMS from {self.sender_id}]: {message}")


# Testing notifications
email = EmailNotification("dev@company.com", "Deployment Alert")
email.send("Production release v2.4.0 completed successfully.")

print("-" * 50)
sms = SMSNotification("+1-555-0199", "AUTH-SVC")
sms.send("Your OTP verification code is 482901.")