items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":40},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"tomatto","price":120,"avl_qty":5},
    {"id":5,"name":"potatto","price":45,"avl_qty":70},
    {"id":6,"name":"carrot","price":80,"avl_qty":0},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hideandseak","price":50,"avl_qty":50}
]

# all_products_names=[i.get("name") for i in items]
# print(all_products_names)

# rsfif=[i.get("name") for i in items if i.get("price")>20 and i.get("price")<50]
# print(rsfif)

# range_filter=[i.get ("name") for i in items if i.get("price") in range(20,51)]
# print(range_filter)

# costly_products=max(items,key=lambda i:i.get("price"))
# print(costly_products)

product_sort=sorted(items,reverse=True,key=lambda i:i.get("avl_qty"))
print(product_sort)
