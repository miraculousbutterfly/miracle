from pyscript import document, when

PRICE = 30         
VAR_COST = 15       
FIXED_COST = 3100  
cart = []          


def q(selector):
    return document.querySelector(selector)


def peso(amount):
    return f"₱{amount:,.2f}"


def to_int(text, default=0):
    try:
        return max(int(text), 0)
    except ValueError:
        return default



def update_estimate(event=None):
    qty = to_int(q("#qty").value)
    q("#estimate").innerText = f"Total: {peso(qty * PRICE)}"


@when("input", "#qty")
def on_qty_input(event):
    update_estimate()


@when("change", "#scent")
def on_scent_change(event):
    update_estimate()



def add_to_cart(scent, qty):
    if qty < 1:
        q("#order-msg").innerText = "Please enter a quantity of at least 1."
        return
    for item in cart:
        if item["scent"] == scent:
            item["qty"] += qty
            break
    else:
        cart.append({"scent": scent, "qty": qty})
    q("#order-msg").innerText = ""
    render_cart()


@when("click", ".add")
def add_from_card(event):
    add_to_cart(event.target.getAttribute("data-scent"), 1)


@when("click", "#add-est")
def add_from_estimator(event):
    add_to_cart(q("#scent").value, to_int(q("#qty").value))


@when("click", "#cart-list")
def remove_item(event):
    btn = event.target.closest("button")
    if btn:
        cart.pop(int(btn.getAttribute("data-idx")))
        render_cart()


def render_cart():
    box = q("#cart-list")
    if not cart:
        box.innerHTML = '<li class="muted">Your cart is empty.</li>'
    else:
        box.innerHTML = "".join(
            f'<li>{i["qty"]} × {i["scent"]} = {peso(i["qty"] * PRICE)}'
            f'<button class="rm" data-idx="{n}">Remove</button></li>'
            for n, i in enumerate(cart)
        )
    total = sum(i["qty"] for i in cart) * PRICE
    q("#cart-total").innerText = f"Total: {peso(total)}"


@when("submit", "#order-form")
def place_order(event):
    event.preventDefault()
    msg = q("#order-msg")
    if not cart:
        msg.innerText = "Your cart is empty. Add a soap first."
        return
    name = q("#cust-name").value.strip()
    contact = q("#cust-contact").value.strip()
    if not name or not contact:
        msg.innerText = "Please enter your name and contact details."
        return
    bars = sum(i["qty"] for i in cart)
    msg.innerText = (f"Thank you, {name}! Order received: {bars} bar(s), "
                     f"total {peso(bars * PRICE)}. We will contact you soon.")
    cart.clear()
    render_cart()
    q("#order-form").reset()



def update_calculator(event=None):
    units = to_int(q("#units").value)
    revenue = units * PRICE
    expenses = FIXED_COST + units * VAR_COST
    profit = revenue - expenses
    q("#calc-out").innerText = (f"Revenue {peso(revenue)} | Expenses {peso(expenses)} | "
                                f"Profit {peso(profit)}")
    break_even = -(-FIXED_COST // (PRICE - VAR_COST))
    state = "above" if units >= break_even else "below"
    q("#calc-status").innerText = (f"Break-even: {break_even} bars per month. "
                                   f"You are {state} break-even.")


@when("input", "#units")
def on_units_input(event):
    update_calculator()


update_estimate()
update_calculator()
