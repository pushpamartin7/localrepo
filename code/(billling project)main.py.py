import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@@pushpamartin@#!P",
    database = "inventory_db"
)

cursor = conn.cursor()
print("\n========INVENTORY & BILLING SYSTEM========")
print("1.View products")
print("2.Add product")
print("3.Update product")
print("4.Delete product")
print("5.Search product")
print("6.Generate Bill")
print("7.Sales History")
print("8.Exit")

choice = input("Enter your choice: ")


if choice == "1":

    cursor.execute("SELECT * FROM prodocts")

    products = cursor.fetchall()

    for product in products:
        print(product)

elif choice =="2":

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))


    query = """
      INSERT INTO products(product_name,price,quantity)
      VALUES(%s,%s,%s)

      """
    values = (name,price,quantity)


    cursor.execute(query,values)
    conn.commit()


    price("Product added successfully!")

elif choice == "3":

    product_id = int(input("Enter product ID: "))
    new_price = float(input("Enter new price: "))
    new_quantity = int(input("Enter new quantity: "))

    query ="""
      UPDATE products
      SET price = %s,quantity=%s
      WHERE product_id =%s

"""
    values = (new_price,new_quantity,product_id)

    cursor.execute(query,values)
    conn.commit()

    if cursor.rowcount>0:
        print("Product updated successfully!")
    else:
        print("Product not found or no changes made.")

elif choice == "4":

    product_id=int(input("Enter product ID to delete: "))
    query ="DELETE FROM products WHERE product_id=%s"

    cursor.execute(query,(product_id,))
    conn.commit()

    if cursor.rowcount>0:
            print("Product updated successfully!")
    else:
        print("Product not found.")

elif choice == "5":

    name=(input("Enter product name to search: "))
    query ="""

       SELECT * FROM products
       WHERE product_name=%s
    """

    cursor.execute(query,(name,))
    product=cursor.fetchone()
    if product:
             print("Product found",product)
    else:
        print("Product not found.")
    
    
elif choice == "6":

    product_id=int(input("Enter product ID: "))
    quantity=int(input("Enter purchase quantity: "))
    cursor.execute(
         "SELECT * FROM products WHERE product_id=%s",
         (product_id,)
    )
    product=cursor.fetchone()
    
    if product is None:
         print("Product not found")

    elif quantity <= 0:
         print("Quantity must be greater than zero.")


    elif quantity > product[3]:
         print("Insufficient stock!")
         print("Available quantity:",product[3])
    else:
         product_name=product[1]
         price=float(product[2])
         total=price*quantity
    update_query="""
        UPDATE products
        SET quantity = quantity-%s
        WHERE product_id=%s
    """
    sale_query="""
        INSERT INTO sales
        (product_id,product_name,quantity_sold,unit_price,total_amount)
        VALUES(%s,%s,%s,%s,%s)
    """

    try:
        cursor.execute(
            update_query,
            (quantity,product_id)
        )

        cursor.execute(
            sale_query,
            (product_id,product_name,quantity,price,total)
        )

        conn.commit()

        print("\n------CUSTOMER BILL------")
        print("Product",product_name)
        print("Price",price)
        print("Quantity",quantity)
        print("Total Amount",total)
        print("Thank you for shopping!")

    except mysql.connector.Error as error:
        conn.rollback()
        print("Billing failed:",error)


elif choice == "7":
    sales_history()   


elif choice == "8":
    print("Thank you for using the system!")
    break

def sales_history():
    try:

        cursor.execute("SELECT * FROM sales ORDER BY sale_id DESC")
        sales=cursor.fetchall()

        if not sales:
                print("No sales records found.")

        else:
            print("\n-------SALES HISTORY-----------")

        for sale in sales:
            print("Sale Id:",sale[0])
            print("Product Id:",sale[1])
            print("Product Name:",sale[2])
            print("Quantity Sold:",sale[3])
            print("unit Price:",sale[4])
            print("Total Amount:",sale[5])
            print("Sale Date:",sale[6])
            print("------------------")  
                
    except mysql.connector.Error as error:
        print("Error.",error)
            
             0