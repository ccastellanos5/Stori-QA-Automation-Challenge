Feature: Dropdown

  Scenario: Selecting multiple choices in the dropdown
    Given I open practice page
    When I select "Option2" from the dropdown
    Then I should see displayed "Option2"
    When I select "Option3" from the dropdown
    Then I should see displayed "Option3"