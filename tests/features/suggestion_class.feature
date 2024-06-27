Feature: Suggestion Class

    Scenario: Selecting Mexico from suggestions
    Given I move to the Suggestion Class Example page
    When I enter "Me" into the suggestion box
    And I select the country "Mexico" from the suggestions
    Then the selected country should be "Mexico"
