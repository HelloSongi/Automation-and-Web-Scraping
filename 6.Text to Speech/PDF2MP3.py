import pyttsx3
import PyPDF2

pdfreader = PyPDF2.PdfFileReader(open('text2speech.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
	text = pdfreader.getpages(page_num).extractText()
	clean_text = text.strip().replace('\n', ' ')
	print(clean_text)

speaker.save_to_file(clean_text, 'text2speech.mp3')
speaker.runAndWait()

speaker.stop()
