from tools import req

rq = req.REQ()

def test_ng_tc1_product_empty_payload():

    print("Running Test Case1: Testing 'products' endpoint, with empty payload")

    input_data = {}
    info = rq.post('products', input_data)

    print(info)

    response_code = info[0]
    assert response_code == 400, 'Test Case 1: empty payload, Expected: 400, got {act}'.format(act=response_code)

    response_body = info[1]
    assert 'errors' in  response_body.keys(), 'Test Case 1: empty payload, the response body ' \
                                              'does not have "errors" as a key'

    exp_error_msg = 'No product data specified to create product'
    act_error_msg = response_body['errors'][0]['message']
    assert exp_error_msg == act_error_msg, 'ERROR MESSAGE'

    exp_error_code = 'woocommerce_api_missing_product_data'
    act_error_code = response_body['errors'][0]['code']
    assert exp_error_code == act_error_code, 'ERROR CODE'

    print('Test case 1: empty payload PASS')

def test_ng_tc2_product_with_missing_title_key_in_payload():

    input_data = {}
    product = {}
    product["regular_price"] = '19.99'
    product["type"] = 'simple'


    input_data["product"] = product
    info = rq.post('products', input_data)
    print('\n')
    print(info)

    response_code = info[0]
    assert response_code == 400, 'Test Case 2: empty title, Expected: 400, got {act}'.format(act=response_code)

    response_body = info[1]
    assert 'errors' in response_body.keys(), 'Test Case 2: empty title, the response body ' \
                                             'does not have "errors" as a key'

    exp_error_msg = 'Missing parameter title'
    act_error_msg = response_body['errors'][0]['message']
    assert exp_error_msg == act_error_msg, 'ERROR in MESSAGE'

    exp_error_code = 'woocommerce_api_missing_product_title'
    act_error_code = response_body['errors'][0]['code']
    assert exp_error_code == act_error_code, 'ERROR in CODE'

    print('Test case 2: empty title PASS')
    tc = 'ng, products, missing title'
    expected_message = 'Missing parameter title'
    expected_error_code = 'woocommerce_api_missing_product_title'

    verify_ng_test_response(info, tc, expected_message, expected_error_code)

def test_ng_tc3_product_with_missing_value_key_in_title():

    input_data = {}
    product = {}
    product["regular_price"] = '19.99'
    product["type"] = 'simple'
    product["title"] = ""

    input_data["product"] = product
    info = rq.post('products', input_data)

    print(info)


def verify_ng_test_response(response_list, test_case_name, exp_err_msg, exp_err_code):

    response_code = response_list[0]
    assert response_code == 400, "Response code is wrong for {tc} Expected: 400," \
                                 "Actual: {act}".format(tc=test_case_name, act=response_code)
    response_body = response_list[1]
    assert 'errors' in response_body.keys(), "For test case {tc}," \
                                             "response body does not have 'errors".format(tc=test_case_name)

    act_error_msg = response_body['errors'][0]['message']
    assert act_error_msg == exp_err_msg, "Test Case {tc} failed, Expected message: {exp}," \
                                         "actual msg {act}".format(tc=test_case_name, exp=exp_err_msg)

    act_error_code = response_body['errors'][0]['code']
    assert act_error_code == exp_err_code, "Test Case: {tc}. The error code is wrong. Expected: {exp}" \
                                           "Actual: {act}".format(tc=test_case_name, exp=exp_err_code, act=act_error_code)

    print('Test {tc} PASS'.format(tc=test_case_name))



# test_ng_tc1_product_empty_payload()
test_ng_tc2_product_with_missing_title_key_in_payload()
# test_ng_tc3_product_with_missing_value_key_in_title()

