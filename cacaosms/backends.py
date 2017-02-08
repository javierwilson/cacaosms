from .models import SMSConfiguration


class InvalidSMSBackend(Exception):
    print "Invalid SMS Backend"
    pass


class BaseSMSBackend(object):

    def send_sms(self):
        raise NotImplementedError()


class DummySMSBackend(object):

    def send_sms(self, phone_number_from, phone_number_to, message, status_callback):
        message = "to=%s, from_=%s, body=%s, status_callback=%s" % (phone_number_to, phone_number_from, message, status_callback)
        print message


class TwilioSMSBackend(object):

    def __init__(self, account_sid, auth_token):
        from twilio.rest import TwilioRestClient
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = TwilioRestClient(self.account_sid, self.auth_token)

    def send_sms(self, phone_number_from, phone_number_to, message, status_callback):
        message = self.client.messages.create(to=phone_number_to, from_=phone_number_from, body=message, status_callback=status_callback)
        return message


def get_sms_backend_client():

    config = SiteConfiguration.get_solo()

    account_sid = settings.SMS_ACCOUNT_SID
    auth_token = settings.SMS_AUTH_TOKEN
    phone_number_from = settings.SMS_PHONE_NUMBER
    status_callback = settings.SMS_STATUS_CALLBACK

    if config == 'dummy':
        return DummySMSBackend(account_sid=accoutn_sid, auth_token=auth_token, phone_number_from=phone_number_from, status_callback=status_callback)

    elif config == 'twilio':
        return TwilioSMSBackend(account_sid=accoutn_sid, auth_token=auth_token, phone_number_from=phone_number_from, status_callback=status_callback)

    else:
        raise InvalidSMSBackend

def send_sms(to, message):
    backend = get_sms_backend_client()
    return backend.send_sms(settings.SMS_DEFAULT_FROM_NUMBER, to, message, status_callback)
