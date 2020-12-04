Feature: Listen

  Scenario: Listen to topic
    Given topic
    And event handler
    And subscribed
    When event occurred
    Then event handler called
