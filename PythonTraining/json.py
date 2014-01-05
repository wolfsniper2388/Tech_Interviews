''' Learn the use of json
'''

import json
count=100
validation_criteria_string = """
    {
        \"validation\": {
            \"validation_criteria_array\": [
                {
                    \"counter\": \"IpInReceives\",
                    \"sign\": \">=\",
                    \"value\": %d,
                    \"result\": 0
                },
                {
                    \"counter\": \"IpForwDatagrams\",
                    \"sign\": \">=\",
                    \"value\": %d,
                    \"result\": 0
                },
                {
                    \"counter\": \"rx_line\",
                    \"sign\": \">=\",
                    \"value\": %d,
                    \"result\": 0
                },
                {
                    \"counter\": \"tx_forward\",
                    \"sign\": \">=\",
                    \"value\": %d,
                    \"result\": 0
                }
            ],
            \"validation_criteria_join_array\": [
                {
                    \"sign\": \"and\"
                },
                {
                    \"sign\": \"and\"
                },
                {
                    \"sign\": \"and\"
                }
            ],
            \"number_of_criteria\": 4
        }
    }
    """ % (int(count)*2, int(count)*2, int(count), int(count))

validation_criteria_json = json.loads(validation_criteria_string)
print validation_criteria_json
                
