# https://datatofish.com/images-to-pdf-python/
from PIL import Image


def export_pdf(image, filename):
	"""
	Function converts image to pdf file

	:param image: path to image you want to save as pdf
	:param filename: name you want to save the .pdf file as without extension
	:return: filename of image converted to a pdf
	"""
	filename = filename + ".pdf"
	img = Image.open(r'' + image)
	img1 = img.convert('RGB')

	img1.save(r'' + filename)

	return filename
