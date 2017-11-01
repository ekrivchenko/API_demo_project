from tools import req
from tools import dbconnect
import json

rq = req.REQ()
qry = dbconnect.DBConnect()

def create_a_product():
    print("Running 'create product' endpoint test ....")

    #set global variables to be used in different methods
    global product_id
    global title
    global price

    print("Building the payload for the call")
    title = 'TEST1 TITLE'
    price = '9.99'

    input_data = {'product':{'title':title,
                            'type':'simple',
                            'regular_price':price}}

    info = rq.post('products', input_data)
    print(info)
    response_code = (info[0])
    response_body = (info[1])

    assert response_code == 201

    rs_title = response_body["product"]['title']
    rs_price = response_body["product"]["regular_price"]
    product_id = response_body["product"]["id"]

    assert rs_title == title, "The title in response is not same is in request." \
                              "The response title is: {}".format(rs_title)

    assert rs_price == price, "The price in response did not match."" \
    ""Expected: {}, Actual {}".format(price, rs_price)
    print(product_id)
    print("The create_product test PASS")

def test_verify_product_created_in_db():
    print("getting info from db to verify that the product has been created")
    sql ='''SELECT p.post_title, p.post_type, pm.meta_value FROM eu_posts p JOIN eu_postmeta pm
            ON p.id=pm.post_id WHERE p.id={} AND pm.meta_key='_regular_price' '''.format(product_id)
    qrs = qry.select("wp881", sql)

    print(qrs)

    db_title = qrs[0][0]
    db_type = qrs[0][1]
    db_price = qrs[0][2]

    assert db_title == db_title, "ERROR MESSAGE TITLE"
    assert db_type == 'product', "ERROR MESSAGE TYPE"
    assert db_price == price, "ERROR MESSAGE PRICE"
    print("The test_verify_product_created_in_db test PASS")


create_a_product()
test_verify_product_created_in_db()

