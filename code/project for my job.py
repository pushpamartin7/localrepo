import mysql.connector

# ==================================
# STEP 1: DATABASE CONNECTION
# ==================================

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@@pushpamartin@#!P",
    database="inventory_db"
)

cursor = mydb.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    quantity_sold INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

mydb.commit()

print("Database connected successfully!")


# ==================================
# STEP 2: VIEW PRODUCTS
# ==================================

def view_products():

    cursor.execute("SELECT * FROM products")
    records = cursor.fetchall()

    print("\n===== PRODUCT LIST =====")

    if not records:
        print("No products available.")
        return

    for record in records:
        print("Product ID:", record[0])
        print("Product Name:", record[1])
        print("Price:", record[2])
        print("Quantity:", record[3])
        print("------------------------")



# ==================================
# STEP 3: ADD PRODUCT
# ==================================

def add_product():

    try:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative.")
            return

        query = """
        INSERT INTO products
        (product_name, price, quantity)
        VALUES (%s, %s, %s)
        """

        values = (name, price, quantity)

        cursor.execute(query, values)
        mydb.commit()

        print("Product added successfully!")

    except (ValueError, mysql.connector.Error) as error:
        mydb.rollback()
        print("Error:", error)


# ==================================
# STEP 4: UPDATE PRODUCT
# ==================================

def update_product():

    try:
        product_id = int(input("Enter product ID: "))

        cursor.execute(
            "SELECT * FROM products WHERE product_id = %s",
            (product_id,)
        )

        product = cursor.fetchone()

        if not product:
            print("Product not found.")
            return

        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative.")
            return

        query = """
        UPDATE products
        SET price = %s, quantity = %s
        WHERE product_id = %s
        """

        values = (price, quantity, product_id)

        cursor.execute(query, values)
        mydb.commit()

        print("Product updated successfully!")

    except (ValueError, mysql.connector.Error) as error:
        mydb.rollback()
        print("Error:", error)


# ==================================
# STEP 5: DELETE PRODUCT
# ==================================

def delete_product():

    try:
        product_id = int(input("Enter product ID: "))

        query = """
        DELETE FROM products
        WHERE product_id = %s
        """

        cursor.execute(query, (product_id,))
        mydb.commit()

        if cursor.rowcount > 0:
            print("Product deleted successfully!")
        else:
            print("Product not found.")

    except (ValueError, mysql.connector.Error) as error:
        mydb.rollback()
        print("Error:", error)


# ==================================
# STEP 6: SEARCH PRODUCT
# ==================================

def search_product():

    name = input("Enter product name to search: ")

    query = """
    SELECT * FROM products
    WHERE product_name LIKE %s
    """

    cursor.execute(query, ("%" + name + "%",))

    records = cursor.fetchall()

    if not records:
        print("Product not found.")
        return

    for record in records:
        print("Product ID:", record[0])
        print("Product Name:", record[1])
        print("Price:", record[2])
        print("Quantity:", record[3])


# ==================================
# STEP 7: GENERATE BILL
# ==================================

def generate_bill():

    try:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        cursor.execute(
            "SELECT * FROM products WHERE product_id = %s",
            (product_id,)
        )

        product = cursor.fetchone()

        if not product:
            print("Product not found.")
            return

        product_name = product[1]
        price = float(product[2])
        available_quantity = product[3]

        if quantity > available_quantity:
            print("Insufficient stock!")
            print("Available quantity:", available_quantity)
            return

        total = price * quantity

        update_query = """
        UPDATE products
        SET quantity = quantity - %s
        WHERE product_id = %s
        """

        cursor.execute(
            update_query,
            (quantity, product_id)
        )

        sale_query = """
        INSERT INTO sales
        (product_id, product_name, quantity_sold,
         unit_price, total_amount)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            sale_query,
            (product_id, product_name, quantity, price, total)
        )

        mydb.commit()

        print("\n========== CUSTOMER BILL ==========")
        print("Product:", product_name)
        print("Price:", price)
        print("Quantity:", quantity)
        print("Total Amount:", total)
        print("Thank you for shopping!")
        print("===================================")

    except (ValueError, mysql.connector.Error) as error:
        mydb.rollback()
        print("Billing failed:", error)


# ==================================
# STEP 8: SALES HISTORY
# ==================================

def sales_history():

    try:
        cursor.execute(
            "SELECT * FROM sales ORDER BY sale_id DESC"
        )

        records = cursor.fetchall()

        if not records:
            print("No sales history found.")
            return

        print("\n========== SALES HISTORY ==========")

        for record in records:
            print("Sale ID:", record[0])
            print("Product ID:", record[1])
            print("Product Name:", record[2])
            print("Quantity Sold:", record[3])
            print("Unit Price:", record[4])
            print("Total Amount:", record[5])
            print("Sale Date:", record[6])
            print("-----------------------------------")

    except mysql.connector.Error as error:
        print("Error:", error)


# ==================================
# STEP 9: LOW STOCK ALERT
# ==================================

def low_stock_alert():

    try:
        cursor.execute(
            "SELECT * FROM products WHERE quantity <= 5"
        )

        records = cursor.fetchall()

        print("\n========== LOW STOCK ALERT ==========")

        if not records:
            print("All products have sufficient stock.")
            return

        for record in records:
            print("Product ID:", record[0])
            print("Product Name:", record[1])
            print("Available Quantity:", record[3])
            print("-------------------------------------")

    except mysql.connector.Error as error:
        print("Error:", error)


# ==================================
# MAIN MENU
# ==================================

while True:

    print("\n===== INVENTORY & BILLING SYSTEM =====")

    print("1. View Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Generate Bill")
    print("7. Sales History")
    print("8. Low Stock Alert")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_products()

    elif choice == "2":
        add_product()

    elif choice == "3":
        update_product()

    elif choice == "4":
        delete_product()

    elif choice == "5":
        search_product()

    elif choice == "6":
        generate_bill()

    elif choice == "7":
        sales_history()

    elif choice == "8":
        low_stock_alert()

    elif choice == "9":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")


# ==================================
# CLOSE DATABASE CONNECTION
# ==================================

cursor.close()
mydb.close()

print("Database connection closed.")