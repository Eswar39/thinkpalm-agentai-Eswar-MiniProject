Feature: Outbound Bulk SMS Campaign Delivery & Failover

  Scenario: Successful primary SMPP delivery within threshold
    Given an enterprise client triggers an outbound bulk SMS campaign
    When the gateway routes messages via the primary SMPP connection
    And a delivery receipt (DLR) with status "DELIVRD" is received within 15 seconds
    Then the message status is marked as "Delivered"
    And no fallback retry is triggered

  Scenario: Automatic fallback retry on primary DLR timeout
    Given an enterprise client triggers an outbound bulk SMS campaign
    When the primary SMPP connection does not return a "DELIVRD" DLR within 15 seconds
    Then the system triggers an automatic fallback retry through the secondary route
    And if the secondary route returns "DELIVRD", the transaction succeeds

  Scenario: Both routes fail and raise billing credit exception
    Given an enterprise client triggers an outbound bulk SMS campaign
    When both primary and secondary routes fail or return "EXPIRED" or "UNDELIV"
    Then the transaction logs an error event
    And updates the dashboard status to "Failed"
    And raises a billing credit exception
