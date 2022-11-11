from behave import *

from ApiAttachDocument import *


@given('request valid')
def step_impl(context):
    context.url, context.params = ApiAttachDocument().request_valid()


@given('request invalid')
def step_impl(context):
    context.url, context.params = ApiAttachDocument().request_valid()


@when('send requisition to api')
def step_impl(context):
    context.status_code = ApiAttachDocument().send_request(context.url, context.params)


@then('response status code is 200')
def step_impl(context):
    assert context.status_code == 200


@when('send requisition invalid to api')
def step_impl(context):
    context.status_code = ApiAttachDocument().send_request_invalid(context.url)


@then('response status code is 400')
def step_impl(context):
    assert context.status_code == 400
