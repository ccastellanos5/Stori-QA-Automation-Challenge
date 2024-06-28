Feature: Suggestion Class

  Scenario: Selecting Mexico from suggestions
    Given I move to the Suggestion Class Example page
    When I enter "Me" into the suggestion box
    And I select the country "Mexico" from the suggestions
    Then the selected country should be "Mexico"

  Scenario: Selecting United States from suggestions
    Given I move to the Suggestion Class Example page
    When I enter "Uni" into the suggestion box
    And I select the country "United States (USA)" from the suggestions
    Then the selected country should be "United States"

  Scenario: Selecting United Arab Emirates from suggestions
    Given I move to the Suggestion Class Example page
    When I enter "Uni" into the suggestion box
    And I select the country "United Arab Emirates" from the suggestions
    Then the selected country should be "United Arab Emirates"

  Scenario: Selecting Spain country from suggestions
    Given I move to the Suggestion Class Example page
    When I enter "Spa" into the suggestion box
    And I select the country "Spain" from the suggestions
    Then the selected country should be "Spain"