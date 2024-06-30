Feature: Switch_Window

  Scenario: Verify 30 day money back guarantee text and close the opened window
    Given I open practice page
    When I click the open window button
    Then I should see "30 day money back guarantee" text displayed in the new window
    And I go back to the practice page