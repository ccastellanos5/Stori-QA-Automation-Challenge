Feature: Switch_Tab

  Scenario: Go to QAClick Academy and take screenshot of Upcoming events
    Given I open practice page
    When I click the open tab button
    Then I should be redirected to QAClick Academy
    And I scroll to the Upcoming events section
    Then I should be able to take a screenshot
    And I go back to the practice page