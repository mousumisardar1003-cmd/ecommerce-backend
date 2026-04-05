import hmac
import hashlib
from django.conf import settings

def verify_razorpay_signature(order_id, payment_id, signature):
    """
    Verify Razorpay payment signature to ensure it's genuine.
    Returns True if valid, False otherwise.
    """
    try:
        generated_signature = hmac.new(
            key=bytes(settings.RAZORPAY_KEY_SECRET, 'utf-8'),
            msg=bytes(order_id + "|" + payment_id, 'utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(generated_signature, signature)
    except Exception as e:
        print("Signature verification failed:", e)
        return False
