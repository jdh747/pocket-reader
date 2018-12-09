"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Note: add credentials to env variables: e.g. GOOGLE_APPLICATION_CREDENTIALS"="/Users/joshuadrewhayes/Dropbox/Projects/instapaper-reader/google_application_credentials.json"
# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(text="""
    Travel Is No Cure for the Mind

    More To That Blocked Unblock Follow Following Mar 21

    At this very moment, you may be here:

    Or you may be here:

    Or here:

    But most likely, you’re probably here:

    It’s just another day… and you’re just doing what you need to do.

    You’re getting things done, and the day moves forward in this continuous sequence of checklists, actions, and respites.

    But at various moments of your routine, you pause and take a good look at your surroundings.

    The scenes of your everyday life. The blur of this all-too-familiar film.

    And you can’t help but to wonder…

    If there is more to it all.
"""
                                                    )

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
