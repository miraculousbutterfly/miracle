# Miracle Soap

Interactive business website for **Miracle Soap**, a handmade natural bar soap (aloe vera, lemon, unscented, herbal/tea tree) for sensitive and acne-prone skin, priced at ₱30 per bar.

Final project for **Free Elec 1 Business Analytics** and **Event-Driven Programming**, Cebu Eastern College.

## Features
- Landing page with logo, business introduction and embedded 36-second promotional video
- Survey-based "Why Miracle Soap?" statistics (n = 31)
- Shop, price estimator and shopping cart
- Order form with confirmation message
- Business Analytics Corner: revenue, expenses, profit and break-even calculator (₱30 price, ₱15 variable cost, ₱3,100 fixed monthly costs)

## PyScript and event-driven programming (`main.py`)
| Event | Element | What happens |
|---|---|---|
| `input` / `change` | quantity and scent fields | live price estimate |
| `click` | Add to cart, Remove | cart is updated and re-rendered |
| `submit` | order form | validates, confirms the order, clears the cart |
| `input` | bars-sold field | revenue, expenses, profit and break-even update |

## Project files
- `index.html`: the website page
- `style.css`: styling
- `main.py`: PyScript code (events and calculations)
- `promo.mp4`: promotional video
- `logo-badge.png`, `logo.png`: logo files

## Run it
Open the GitHub Pages link:https://miraculousbutterfly.github.io/miracle/
An Internet connection is needed to load PyScript.

## Group members
Manguilimotan, Lovely Chloe N. • Cuizon, Maria Sofia E. • Lawas, Rubbie Ann P. • Mina, Beveymae G. • Solasco, Mera N.
