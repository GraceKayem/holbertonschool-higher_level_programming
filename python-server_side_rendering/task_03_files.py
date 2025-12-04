#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def json_file():
    try:
        with open("products.json", "r") as f:
            data = json.load(f)

            if isinstance(data, dict):
              return data.get("products", [])
            return data
    except Exception:
        return None

def csv_file():
    products = []
    try:
        with open("products.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception:
        return None

@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")


    if source == "json":
        data = json_file()
    elif source == "csv":
        data = csv_file()
    else:
        return render_template("product_display.html", error="Wrong source")


    if data is None:
        return render_template("product_display.html", error="Could not read the file")


    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Invalid id")

        filtered = [p for p in data if p["id"] == product_id]

        if not filtered:
            return render_template("product_display.html", error="Product not found")

        return render_template("product_display.html", products=filtered)


    return render_template("product_display.html", products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
