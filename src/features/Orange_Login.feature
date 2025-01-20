@Orange
Feature: Login Test in Orange portal


  Scenario: Test Login Portal
      Given The User fill username text box
      And The User fill password text box
      When The User clicks Login button
      Then Verify the user is logged in

  Scenario: Get System Users from User list
    Given the user is Logged in
    And The user go to System user list
    When Verify Admin user is present in the list