from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from database.session import db_session
from database.models import Brands,Products,ProductsImages
from sqlalchemy import func
def api_method():

    sub1=db_session.query(Products,ProductsImages).join(ProductsImages,Products.id==ProductsImages.product_id).with_entities(Products.store_id.label("s_id"),func.count(ProductsImages.image).label("count_of_images")).group_by(Products.store_id).subquery('sub1') 

    sub2=db_session.query(Products).with_entities(Products.store_id.label('s_id'),func.count(Products.id).label("count_of_products")).group_by(Products.store_id).subquery('sub2')  

    combine_query=db_session.query(sub1).join(sub2,sub1.c.s_id==sub2.c.s_id).with_entities(sub1.c.s_id,sub1.c.count_of_images,sub2.c.count_of_products)

    dict={}
    for i in combine_query:
        dict[i[0]]=[i[1],i[2]]
    return jsonify(dict)