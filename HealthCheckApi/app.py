from health_check_api import HealthCheckAPI
from message_notifier import HealthCheckNotifier

account_sid = 'ACaf500a7a074c32f57082830dce40f29b'
auth_token = 'c85bfe34763b714a3c2101db4ca9a5cb'
from_number = '+14179628485'
to_number = '+51981145791'

health_check_notifier = HealthCheckNotifier(account_sid, auth_token, from_number, to_number)

health_check_api = HealthCheckAPI()
health_check_api.attach_observer(health_check_notifier)

health_check_api.run()
