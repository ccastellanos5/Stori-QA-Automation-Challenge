Feature: Switch_To_Alert

  Scenario: Handle alert dialog
    Given I open practice page
    When I type "Stori Card" into the alert input
    And I click the "alert" button
    Then I should see an alert with the text "Hello Stori Card, share this practice page and share your knowledge"
    And I print the alert text
    And I "accept" the alert

  Scenario: Handle confirm dialog
    Given I open practice page
    When I type "Stori Card" into the alert input
    And I click the "confirm" button
    Then I should see an alert with the text "Hello Stori Card, Are you sure you want to confirm?"
    And I print the alert text
    And I "confirm" the alert