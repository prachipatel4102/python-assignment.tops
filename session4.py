#Q1 Take the string 'Flipkart-Sale2024' and use string methods to convert it to lowercase, replace the dash with a space, and print the result.
string="Flipkart-Sale2024"
result=string.lower().replace("-"," ")
print(result)

#Q2 Given the product name ' OnePlus Nord-CE 3 ', write code to clean it by removing extra spaces, converting all letters to uppercase, and replacing the dash with a colon.<br><br><em><strong>Hint:</strong> Use strip(), upper(), and replace() methods in sequence.</em>
product="OnePlus Nord-CE 3"
clean=product.upper().strip().replace("-",":")
print(clean)

#Q3 Write a function split_product_code(product_code) that takes a string like 'ZOMATO-FOOD-2024' and returns a list of its parts using the split() method.
def split_product_code(product_code):
    return product_code.split("-")
result=split_product_code("ZOMATO-FOOD-2024")
print(result)

#Q4Given the string 'Spotify_Premium_Offer', use string slicing to extract and print only the word 'Premium'.
string="Spotify_premium_Offer"
print(string[8:15])

#Q5 Format and print a message using variables: product = 'Myntra Shirt', price = 799.5. The output should be: 'Deal: Myntra Shirt is available at ₹799.50 only!' using string formatting
product="Myntra Shirt"
price=799.5
print(f"Deal: {product} is available at {price:.2f} only!")