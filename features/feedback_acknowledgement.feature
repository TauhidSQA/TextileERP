Feature: Complete the acknowledgment phase
  Background:
    Given I am on the dashboard page
    When I click on Supply Chain Management
    And I click the Pre-Procurement-Yarn
    And I click the M&M Fabric Projection Acknowledgement
    And I click on the view icon

  Scenario: Acknowledgment
    And I click on the acknowledge button
    Then I should see a "Save successfully" message


  Scenario: Feedback
   When I click on the feedback button
   And I click on the drop-down option and select the available reason
   And I click on the OK button
   Then I should see a "Save successfully" message
