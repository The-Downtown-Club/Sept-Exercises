from connector import products_db_session
from models import Products, Brands, ProductsImages, ProductsVariants
from datetime import datetime as dt

def get_products_by_brand_id(brand_id):
    # i = 0

    prods = products_db_session.query(Products).filter(Products.store_id == brand_id).all()

    products_list = []
    for prod in prods:
        products_json = {}
        products_json['title'] = prod.title
        products_json['body_html'] = prod.description
        products_json['created_at'] = prod.created_at.replace(microsecond=0).replace(tzinfo=None).isoformat()
        if prod.published_at:
            products_json['published_at'] = prod.published_at.replace(microsecond=0).replace(tzinfo=None).isoformat()
        else:
            products_json['published_at'] = ''

        variants_list = []
        option_num = 0
        variants = products_db_session.query(ProductsVariants).filter(ProductsVariants.product_id == prod.id).all()
        for prod_var in variants:
            option_num += 1
            variant_dict = {
                    'id' : prod_var.id,
                    'product_id' : prod_var.product_id,
                    'price' : float(str(prod_var.price)),
                    'sku' : prod_var.sku,
                    'option1': option_num,
                    'option2': None,
                    'option3': None,
                    'created_at': prod_var.created_at.replace(microsecond=0).replace(tzinfo=None).isoformat(),
                    'updated_at': prod_var.updated_at.replace(microsecond=0).replace(tzinfo=None).isoformat(),
                    'taxable': prod_var.taxable,
                    'requires_shipping': prod_var.requires_shipping
                }
            if prod_var.compare_at_price:
                variant_dict['compare_at_price'] = prod_var.compare_at_price
            if prod_var.weight:
                variant_dict['weight'] = prod_var.weight
                variant_dict['weight_unit'] = prod_var.weight_unit

            variants_list.append(variant_dict)
        products_json['variants'] = variants_list
        products_json['options'] = []
        
        images_list = []
        imgs = products_db_session.query(ProductsImages).filter(ProductsImages.product_id == prod.id).all()
        for prod_img in imgs:
            images_list.append(
                {
                    'id': prod_img.id,
                    'product_id': prod_img.product_id,
                    'position': prod_img.image_index,
                    'created_at': prod_img.created_at.replace(microsecond=0).replace(tzinfo=None).isoformat(),
                    'updated_at': prod_img.updated_at.replace(microsecond=0).replace(tzinfo=None).isoformat(),
                    'width': prod_img.width,
                    'height': prod_img.height,
                    'src': prod_img.src
                }
            )
            if prod_img.image_index == 1:
                products_json['image'] = {
                    'id': prod_img.id,
                    'product_id': prod_img.product_id,
                    'position': prod_img.image_index,
                    'created_at': prod_img.created_at.replace(microsecond=0).replace(tzinfo=None).isoformat(),
                    'updated_at': prod_img.updated_at.replace(microsecond=0).replace(tzinfo=None).isoformat(),
                    'width': prod_img.width,
                    'height': prod_img.height,
                    'src': prod_img.src
                }
        products_json['images'] = images_list
        products_list.append(products_json)
        # if len(variants_list) > 1:
        #     print(i)
        # i+=1

    return products_list

final_list = get_products_by_brand_id(169)
# print(final_list[34])

with open('C:/Users/Vijay/flask/flaskRestX/prj3/prod_sync2/sample.txt', 'w') as f:
    f.write(str(final_list[34]))