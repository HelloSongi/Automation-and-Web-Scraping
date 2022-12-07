import camelot
import cv2
tables = camelot.read_pdf('./foo.pdf')
#f= (could be json, excel, html, markup file etc)
tables.export('foo.csv', compress=True)