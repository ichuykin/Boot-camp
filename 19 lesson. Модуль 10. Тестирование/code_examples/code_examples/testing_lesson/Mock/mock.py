from unittest.mock import Mock
import json

# mock = Mock()
# print(mock.some_attribute)
# print(mock.some_attribute())
####################
# json = Mock()
# print(json.loads('{"k": "v"}').get('k'))
#####################
# json = Mock()
# print(json.loads('{"key": "value"}'))
# json.loads.assert_called()
# json.loads.assert_called_once()
# json.loads.assert_called_with('{"key": "value"}')
# json.loads.assert_called_once_with('{"key": "value"}')
# print(json.loads('{"key": "value"}'))
# json.loads.assert_called_once()
# json.loads.assert_not_called()
# print(json.loads.call_count)
# print(json.loads.call_args)
# print(json.loads.call_args_list)
# print(json.method_calls)
# print()
######################################
# from datetime import datetime

# def is_weekday():
#     today = datetime.today()
#     # Python's datetime library treats Monday as 0 and Sunday as 6
#     return (0 <= today.weekday() < 5)

# # Test if today is a weekday
# assert is_weekday()
#############################################
# import datetime
# from unittest.mock import Mock
# # Save a couple of test days
# tuesday = datetime.datetime(year=2019, month=1, day=1)
# saturday = datetime.datetime(year=2019, month=1, day=5)
# # Mock datetime to control today's date
# datetime = Mock()

# def is_weekday():
#     today = datetime.datetime.today()
#     # Python's datetime library treats Monday as 0 and Sunday as 6
#     return (0 <= today.weekday() < 5)

# # Mock .today() to return Tuesday
# datetime.datetime.today.return_value = tuesday
# # Test Tuesday is a weekday
# assert is_weekday()
# # Mock .today() to return Saturday
# datetime.datetime.today.return_value = saturday
# # Test Saturday is not a weekday
# assert not is_weekday()