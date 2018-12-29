Feature: Getting CSV file
  To sort any CSV file
  We must first get the CSV file

  Scenario: Get CSV file
    Given the file is valid
    And the file can be opened
    And the file can be read
    When I open the file to read with csv module
    Then I should get a csv reader iterator object

  Scenario: Write to CSV file
    Given a valid list of lists
    And output file can be written to
    When I write to the output file
    Then I should be able to see the contents in the output file

  Scenario: CSV file to list
    Given the CSV reader iterator object
    When I turn the iterator object into a list
    Then I should be able to sort on the list

  Scenario: CSV file data validity
    Given each item in CSV file is valid
    When I sort based on lower case letters
    Then I should be able to sort every item

