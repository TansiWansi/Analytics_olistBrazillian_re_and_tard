import pandas as pd

datasetPath : str = "C:/Users/BACI/.cache/kagglehub/datasets/olistbr/brazilian-ecommerce/versions/2/"

datasetsCSV : dict = {
    "customers" : datasetPath + "olist_customers_dataset.csv",
    "geolocation" : datasetPath + "olist_geolocation_dataset.csv",
    "orders" : datasetPath + "olist_orders_dataset.csv",
    "orderItems" : datasetPath + "olist_order_items_dataset.csv",
    "orderPayments" : datasetPath + "olist_order_payments_dataset.csv",
    "orderReviews" : datasetPath + "olist_order_reviews_dataset.csv",
    "products" : datasetPath + "olist_products_dataset.csv",
    "sellers" : datasetPath + "olist_sellers_dataset.csv",
    "productCategoryNameTranslation" : datasetPath + "product_category_name_translation.csv"
}

# customer_id  customer_unique_id  customer_zip_code_prefix  customer_city  customer_state
customers_df : pd.DataFrame = pd.read_csv(datasetsCSV["customers"])

# geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng', 'geolocation_city', 'geolocation_state'
geolocation_df : pd.DataFrame = pd.read_csv(datasetsCSV["geolocation"])

# 'order_id', 'customer_id', 'order_status', 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date'
orders_df : pd.DataFrame = pd.read_csv(datasetsCSV["orders"])

# 'order_id', 'order_item_id', 'product_id', 'seller_id', 'shipping_limit_date', 'price', 'freight_value'
orderItems_df : pd.DataFrame = pd.read_csv(datasetsCSV["orderItems"])

# 'order_id', 'payment_sequential', 'payment_type', 'payment_installments', 'payment_value'
orderPayments_df : pd.DataFrame = pd.read_csv(datasetsCSV["orderPayments"])

# 'review_id', 'order_id', 'review_score', 'review_comment_title', 'review_comment_message', 'review_creation_date', 'review_answer_timestamp'
orderReviews_df : pd.DataFrame = pd.read_csv(datasetsCSV["orderReviews"])

# 'product_id', 'product_category_name', 'product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm'
products_df : pd.DataFrame = pd.read_csv(datasetsCSV["products"])

# 'seller_id', 'seller_zip_code_prefix', 'seller_city', 'seller_state'
sellers_df : pd.DataFrame = pd.read_csv(datasetsCSV["sellers"])

# 'product_category_name', 'product_category_name_english'
productCategoryNameTranslation_df : pd.DataFrame = pd.read_csv(datasetsCSV["productCategoryNameTranslation"])