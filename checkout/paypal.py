import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AQ1GfPGZM5WmGULqn4GEQa1tJa7mIrg457VxYeSBLZIfS6-PdqP2O_L3AjiJ5-zoGf-UPeV6vrn8b5qE"
        self.client_secret = "EBTq1RAydzKEMCurQG8rOVI6VGJmAsL0FKuolzbFjGcQvy4kFYrtVnJ4Vxcte3EjTdUOU1s5mT34N-_J"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)