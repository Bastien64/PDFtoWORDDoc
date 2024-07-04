from pdf2docx import Converter
import sys

def pdf_to_word(pdf_file, word_file):
    # Initialiser le convertisseur avec le fichier PDF
    cv = Converter(pdf_file)
    
    # Convertir le PDF en DOCX
    cv.convert(word_file, start=0, end=None)
    
    # Fermer le convertisseur
    cv.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.pdf output.docx")
    else:
        pdf_file = sys.argv[1]
        word_file = sys.argv[2]
        pdf_to_word(pdf_file, word_file)
        print(f"Le fichier '{pdf_file}' a été converti en '{word_file}' avec succès.")
