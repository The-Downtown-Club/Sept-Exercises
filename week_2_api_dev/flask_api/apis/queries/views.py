from database.models import Brands, Products, ProductsImages
from flask import jsonify
from sqlalchemy import func
from database.session import db_session
# from flask import current_app


def api_method():

    print("check endpoints")

    q1 = db_session.query(Products).join(ProductsImages , Products.id==ProductsImages.product_id).with_entities(Products.store_id.label('STORE_ID'), func.count(ProductsImages.image).label("Total_Images")).group_by(Products.store_id).subquery('q1')

    q2 = db_session.query(Products).with_entities(Products.store_id.label('STORE_ID'), func.count(Products.id).label("Count_of_Products")).group_by(Products.store_id).subquery('q2')

    final = db_session.query(q1).join(q2, q1.c.STORE_ID==q2.c.STORE_ID).with_entities(q1.c.STORE_ID, q1.c.Total_Images, q2.c.Count_of_Products)     
    
    final_dict = {}
    for row in final:
        final_dict[row[0]] = [row[1], row[2]]

    return jsonify(final_dict)