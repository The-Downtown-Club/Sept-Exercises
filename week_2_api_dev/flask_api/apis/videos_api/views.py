from flask import jsonify
from database.session import db_session
from database.models import Products, ProductsImages
from sqlalchemy import func

# catch bad requests
def catch_bad_requests(x):
    msg = f'{x} is not a valid path'
    return jsonify(msg), 400

# main API method
def api_method():
    # get images per store
    q1 = db_session.query(Products, ProductsImages).with_entities(Products.store_id.label('products_store_id'), func.count(ProductsImages.image).label('images')).join(ProductsImages, ProductsImages.product_id == Products.id).group_by(Products.store_id).subquery('q1')

    # get products per store
    q2 = db_session.query(Products).with_entities(Products.store_id.label('products_store_id'), func.count(Products.id).label('num_prods')).group_by(Products.store_id).subquery('q2')

    # join q1 and q2
    q3 = db_session.query(q1).with_entities(q1.c.products_store_id, q2.c.num_prods, q1.c.images).join(q2, q2.c.products_store_id == q1.c.products_store_id)

    # store_id = [s_id[0] for s_id in q3]
    # product_count = [prod[1] for prod in q3]
    # image_count = [imgs[2] for imgs in q3]

    final_dict = {}

    # mapping product and image count to their respectivr stores
    for store_id, product_count, image_count in q3:
        final_dict[store_id] = [product_count, image_count]

    return jsonify(final_dict), 200