Feature: Test API

  Scenario: Valid request
    Given request valid
    When send requisition to api
    Then response status code is 200
