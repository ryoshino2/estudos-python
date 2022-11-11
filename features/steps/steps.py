from behave import *

from ApiAttachDocument import *


@given('request valid')
def step_impl(context):
    context.url, context.params = ApiAttachDocument().request_valid()


@when('send requisition to api')
def step_impl(context):
    context.statusCode = ApiAttachDocument().send_request(context.url, context.params)


@then('response status code is 200')
def step_impl(context):
    assert context.statusCode is 200


@given('request invalid')
def step_impl(context):
    context.url, context.params = ApiAttachDocument().request_valid()


@then('response status code is 400')
def step_impl(context):
    assert context.statusCode is 400
