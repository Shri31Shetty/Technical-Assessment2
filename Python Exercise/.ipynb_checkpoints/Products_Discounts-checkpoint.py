#5.Create a DataFrame of products with columns: Product Name, Price, Category.
import pandas as pd
products_data = {
    "Product Name": ["Laptop", "Headphones", "Keyboard", "Mouse", "Monitor"],
    "Price": [1200, 450, 350, 200, 600],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics"]
}
df_products = pd.DataFrame(products_data)
df_products["Discounted Price"] = df_products["Price"] * 0.9
cheap_products = df_products[df_products["Discounted Price"] < 500]
print("\nProducts cheaper than 500:\n", cheap_products)