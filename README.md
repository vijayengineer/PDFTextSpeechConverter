# PDFTextSpeechConverter
Converts scanned documents and ordinary documents into text. Synthesizes speech as mp3 using Amazon Polly

Pre-requisites:
1.Setup amazon credentials files and install requirements.
2. Ensure Amazon polly works by checking aws configure 

![Screenshot](https://github.com/vijayengineer/PDFTextSpeechConverter/blob/main/assets/Screenshot%202020-12-30%20at%2017.51.39.png)


Server.py: Django file which uses Post to render the index.html template
regularpdftext.py: Uses pdfminer to scan pdf files to text
scannedpdftext.py: Uses tesseract to scan pdf files to text

Polly_synth_speech.py: Converts text file to mp3 using the Polly "Salli" speaker
Converted speech files are stored in ConvertedSpeech folder

Test:
Run server.py and check with the provided sample pdf
Speech sample is provided as a test example

