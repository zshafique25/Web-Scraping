# data_processing.py
import pandas as pd

def process_data(products):
    try:
        names = []
        prices = []
        links = []
        image_urls = []
        ratings = []
        descriptions = []
        product_id = []
        manufactured_by = []
        sold_by = []
        width = []
        depth = []
        height = []
        weight = []
        color = []
        materials = []
        category = []
        style = []
        numberOfColors = []
        listOfColors = []

        for product in products:
            names.append(product['Name'])
            price = product['Price'][0] if product['Price'] else None
            prices.append(price)
            links.append(product['Link'])
            image_url = product['Image_URL'].split(',')[0]
            image_urls.append(image_url)
            rating_str = product['Rating']
            if rating_str:
                rating = float(rating_str.replace('Average rating: ', '').replace(' out of 5 stars', ''))
                rating = round(rating, 1)
                rating = str(rating) + ' out of 5 stars'
            else:
                rating = None
            ratings.append(rating)
            descriptions.append(product['Description'])
            # Additional product details
            product_id.append(product['Product ID'])
            manufactured_by.append(product['Manufactured By'])
            sold_by.append(product['Sold By'])
            width_val = product['Width']
            width_unit = 'inches' if width_val else None
            width.append(f"{width_val} {width_unit}")
            depth_val = product['Depth']
            depth_unit = 'inches' if depth_val else None
            depth.append(f"{depth_val} {depth_unit}")
            height_val = product['Height']
            height_unit = 'inches' if height_val else None
            height.append(f"{height_val} {height_unit}")
            weight_val = product['Weight']
            weight_unit = 'lbs' if weight_val else None
            weight.append(f"{weight_val} {weight_unit}")
            color.append(product['Color'])
            materials.append(product['Materials'])
            category.append(product['Category'])
            style.append(product['Style'])
            numberOfColors.append(product.get('Number of Colors', 0))
            listOfColors.append(', '.join(product.get('List of Colors', [])))

        data = {'Name': names, 'Price': prices, 'Link': links, 'Image_URL': image_urls, 'Rating': ratings, 
                'Description': descriptions, 'Product ID': product_id, 'Manufactured By': manufactured_by, 
                'Sold By': sold_by, 'Width': width, 'Depth': depth, 'Height': height, 'Weight': weight, 
                'Color': color, 'Materials': materials, 'Category': category, 'Style': style, 
                'Number of Colors': numberOfColors, 'List of Colors': listOfColors
                }
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Error processing data: {e}")
        return pd.DataFrame()
    