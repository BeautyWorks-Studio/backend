from flask import request, jsonify
from app.models.payment_model import Payment
from app.models.order_model import Order
import stripe, razorpay, os
from dotenv import load_dotenv
load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

razor = razorpay.Client(auth=(os.getenv("RAZORPAY_KEY_ID"), os.getenv("RAZORPAY_KEY_SECRET")))

def create_stripe_payment():
    data = request.get_json()
    items = data.get("items")
    order_id = data.get("orderId")

    try:
        line_items = [{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": item["name"]},
                "unit_amount": int(item["price"] * 100),
            },
            "quantity": item["quantity"],
        } for item in items]

        session = stripe.checkout.Session.create(
            success_url=f"{data.get('origin')}/verify?success=true&orderId={order_id}",
            cancel_url=f"{data.get('origin')}/verify?success=false&orderId={order_id}",
            line_items=line_items,
            mode="payment"
        )
        return jsonify({"success": True, "session_url": session.url})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

def verify_stripe():
    data = request.get_json()
    order_id = data.get("orderId")
    success = data.get("success")

    if success == "true":
        order = Order.objects(id=order_id).first()
        order.payment_status = True
        order.save()

        Payment(order_id=order_id, method="Stripe", amount=order.amount, status="paid").save()
        return jsonify({"success": True})
    else:
        Order.objects(id=order_id).delete()
        return jsonify({"success": False})

def create_razorpay_order():
    data = request.get_json()
    order_id = data.get("orderId")
    amount = int(data.get("amount") * 100)

    try:
        order = razor.order.create({
            "amount": amount,
            "currency": "INR",
            "receipt": order_id
        })
        return jsonify({"success": True, "order": order})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

def verify_razorpay():
    data = request.get_json()
    razorpay_order_id = data.get("razorpay_order_id")
    user_id = data.get("userId")

    try:
        order_info = razor.order.fetch(razorpay_order_id)
        if order_info["status"] == "paid":
            Order.objects(id=order_info["receipt"]).update_one(set__payment_status=True)
            Payment(order_id=order_info["receipt"], method="Razorpay", amount=order_info["amount"] / 100, status="paid").save()
            User.objects(id=user_id).update_one(set__cart_data={})
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": "Payment failed"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})