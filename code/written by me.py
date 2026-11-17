import mysql.connector

#=============1.Database connection==========
mydb = mysql.connector.connect(
user = "root",
password = "mysql",
database = "inventory_db"
)

cursor = mydb.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
sale_id INT PRIMRY KEY NOT NULL,
product_id INT NOT NULL,
product_name VARCHAR(100) NOT NULL,
product_price DECIMAL NOT NULL,
product_quantity INT NOT NULL,
total DECIMAL NOT NULL,
sale_date TIMESTAMP DEFAULT CURRENT TIMESTAMP

) """)
mydb.commit()
print("Database connected successfully!")


#==============2.VIEW PRODUCTS=============

def view_product():
    cursor.execute("SELECT * FROM products")
    records = cursor.fetchall()
    print("\n----------VIEW PRODUCTS------------")

    if not records:
        print("No products available.")


    for record in records:
        print("Product ID:",record[0])
        print("Product Name:",record[1])
        print("Product Price:",record[2])
        print("Product Quantity:",record[3])
        print("------------------------")



    #==============3.ADD PRODUCTS=============

def add_products():
    try:
        name =input("Enter product name: ")
        price =float(input("Enter price: "))
        quantity =int(input("Enter qunatity: "))

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative!")
            return
        
        query = """
        INSERT INTO products
        (product_name,price,quantity)
        VALUES(%S,%S,%S)
        """

        values = (name,price,quantity)
        cursor.execute(query,values)
        mydb.commit()
        print("Product added successfully!")

    except(ValueError,mysql.connector.Error)as error:
        print("Error",error)

#===========4.UPDATE PRODUCTS============

def update_product():
   try:
       product_id =int(input("Enter product ID: "))
       cursor.execute(
            "SELECT * FROM products WHERE product_id =%s",
            (product_id,)
       )

       product = cursor.fetchone()

       if not product:
           print("No product found")
           return
       
       price = float(input("Enter new price: "))
       quantity =int(input("Enter new quantity: "))

       if price<0 or quantity<0:
           print("Price and quantity cannot be negative!")


       query ="""
       UPDATE products
       SET price =%s, quantity =%s
       WHERE product_id =%s
       """
       values=(price,quantity,product_id)
       cursor.execute(query,values)
       mydb.commit()
       print("Product updated successfully!")

   except(ValueError,mysql.connector.Error)as error:
       mydb.rollback()
       print("Error",error)


def delete_product():
    try:
        product_id =int(input("Enter product id: "))

        query=""""
        DELETE FROM product
        WHERE product_id =%s
        """
        cursor.execute(query,(product_id,))
        mydb.commit()

        if cursor.rowcount>0:
            print("Product deleted successfully")

        else:
            print("Product not found")
    except(ValueError,mysql.connector.Error)as error:
        mydb.rollback()
        print("Error:",error)


#============SEARCH PRODUCT============


    
