from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing

class PollySynthSpeech():
    def _init_():
        pass
    def speechconvert(self, text):
        if(len(text) > 0):
        # Create a client using the credentials and region defined in the [adminuser]
        # section of the AWS credentials file (~/.aws/credentials).
            if(len(text)>3000):
                text1 = text[0:3000]
            else:
                text1 = text
            session = Session(profile_name="user1")
            polly = session.client("polly")
            response = polly.synthesize_speech(VoiceId='Salli',
                                    OutputFormat='mp3',
                                    Text=text1)

            file = open('ConvertedSpeech/speech.mp3', 'wb')
            file.write(response['AudioStream'].read())
            file.close()
