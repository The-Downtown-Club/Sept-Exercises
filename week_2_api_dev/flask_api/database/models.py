from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    BigInteger,
    ARRAY,
    Numeric,
    DateTime
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AbstractShopifyObject:
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))

    shopify_created_at = Column(DateTime(timezone=True))
    shopify_updated_at = Column(DateTime(timezone=True))

    is_deleted = Column(Boolean)
    delete_counter = Column(Integer)
    deleted_at = Column(DateTime(timezone=True))
    hash = Column(String(512))


class Brands(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True)
    city = Column(String(32))
    cover_link = Column(String(1000))  # TODO :To be changes to URL
    description = Column(String(10240), nullable=True)
    domain = Column(String(256), nullable=True)
    myshopify_domain = Column(String(256), nullable=True)
    email = Column(String(512), nullable=True)
    facebook_handle = Column(String(256), nullable=True)
    instagram_handle = Column(String(256), nullable=True)
    youtube_handle = Column(String(256), nullable=True)
    logo_link = Column(String(1000))  # TODO :To be changes to URL
    status = Column(Boolean, default=False)
    store_name = Column(String(256), nullable=True)
    store_name_slug = Column(String(255))  # not define in sheet
    
    
class Products(Base, AbstractShopifyObject):
    __tablename__ = "products"

    category_id = Column(Integer, nullable=True)
    category2_id = Column(Integer, nullable=True)
    category3_id = Column(Integer, nullable=True)
    description = Column(String(10240), nullable=True)
    handle = Column(String(512))
    id = Column(Integer, primary_key=True)
    image = Column(String(500))
    image_link = Column(String(500))
    inventory_quantity = Column(Integer, default=0)
    page_link = Column(String(500))
    price = Column(Numeric(10, 2))
    shopify_product_id = Column(BigInteger, nullable=False, unique=True)
    store_id = Column(Integer, ForeignKey("brands.id", ondelete="CASCADE"), nullable=True)
    title = Column(String(512))

    raw_description = Column(String(10240), nullable=True)
    openai_benefits = Column(ARRAY(String(256)), nullable=True)
    openai_color = Column(ARRAY(String(256)), nullable=True)
    openai_contents = Column(ARRAY(String(256)), nullable=True)
    openai_flavours = Column(ARRAY(String(256)), nullable=True)
    openai_ingredients = Column(ARRAY(String(256)), nullable=True)
    openai_keywords = Column(ARRAY(String(256)), nullable=True)
    openai_materials = Column(ARRAY(String(256)), nullable=True)
    openai_occasion = Column(ARRAY(String(256)), nullable=True)
    openai_pattern = Column(ARRAY(String(256)), nullable=True)
    openai_style = Column(ARRAY(String(256)), nullable=True)
    openai_summary = Column(String(4096), nullable=True)
    openai_product_type = Column(String(512), nullable=True)
    openai_subcategory = Column(String(512), nullable=True)
    shopify_subcategory = Column(String(512), nullable=True)
    openai_is_sustainable = Column(Boolean, nullable=True)
    openai_is_vegan = Column(Boolean, nullable=True)
    openai_is_glutenfree = Column(Boolean, nullable=True)
    openai_is_handmade = Column(Boolean, nullable=True)

    is_published = Column(Boolean, nullable=False, default=False)
    published_at = Column(DateTime(timezone=True))


class ProductsImages(Base, AbstractShopifyObject):
    __tablename__ = "products_images"

    height = Column(Integer)
    id = Column(Integer, primary_key=True)
    image = Column(String(500))
    image_index = Column(Integer, default=0)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    shopify_image_id = Column(BigInteger)
    src = Column(String(500))
    width = Column(Integer)
