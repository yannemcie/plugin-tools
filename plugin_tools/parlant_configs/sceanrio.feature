Feature: Guidelines
    Background:
        Given the alpha engine
        And an empty session

    Scenario: The agent follows a the correct guideline
        Given an agent
        And a guideline "in_stock", to verify if the type of product is in stock when a user asks anything about a product
        And a guideline "ask_for_specs", to ask the user what exactly is he looking for when the product type is in stock
        And a guideline connection whereby "in_stock" entails "ask_for_specs"
        
        And the tool "get_in_stock"
        And an association between "in_stock" and "get_in_stock"
        And a guideline "recommend_products", to recommend 3 most suitable products when the user mentions product usage.
        And the tool "get_products_by_tags"
        And an association between "recommend_products" and "get_products_by_tags"
        And a user message, "Hey there! i'm looking to buy a notebook but not sure which one to chose. can you help me out?"
        When processing is triggered
        Then a single message event is emitted
        And the message contains request for clarification


    Scenario: The agent 
        Given an agent
        And a guideline "in_stock", to verify if the type of product exists when a user asks anything about a product
        And a guideline "ask_for_specs", to ask the user what exactly is he looking for when a user asks anything about a product
        And a guideline connection whereby "in_stock" entails "ask_for_specs"
        And the tool "get_in_stock"
        And an association between "in_stock" and "get_in_stock"
        And a guideline "recommend_products", to recommend 3 most suitable products when the user mentions product usage
        And the tool "get_products_by_tags"
        And an association between "recommend_products" and "get_products_by_tags"
        And a user message, "Hey there! i'm looking to buy a notebook but not sure which one to chose. can you help me out?"
        When processing is triggered
        Then a single message event is emitted
        And the message contains request for clarification