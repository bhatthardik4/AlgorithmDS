# -*- coding: utf-8 -*-
"""TestRunDeliverable2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WHj-nE7icbf_ayBurJxPDkS4WptiXUqz
"""

from test_deliverable2 import *

# Instantiate the URLValidator class
validator = URLValidator()

# Define user prompt and URL
user_prompt = "I recently tested positive for COVID-19. How long should I wait before traveling internationally?"
url_to_check = "https://www.cdc.gov/coronavirus/2019-ncov/travelers/international-travel-during-covid19.html"

# Run the validation
result = validator.rate_url_validity(user_prompt, url_to_check)

# Print the results
import json
print(json.dumps(result, indent=2))

