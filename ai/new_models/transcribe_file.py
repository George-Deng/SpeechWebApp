from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import configparser


def get_auth():
    config = configparser.RawConfigParser()
    config.read('speech.cfg')
    apikey = config.get('auth', 'apikey')
    return apikey

def get_url():
    config = configparser.RawConfigParser()
    config.read('speech.cfg')
    url = config.get('auth', 'url')
    return url

def main():
    apikey = get_auth()
    url = get_url()
    authenticator = IAMAuthenticator(apikey)
    stt = SpeechToTextV1(authenticator=authenticator)
    stt.set_service_url(url)

    with open('tester.mp3', 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel').get_result()
        print(res)

if __name__ == "__main__":
    main()