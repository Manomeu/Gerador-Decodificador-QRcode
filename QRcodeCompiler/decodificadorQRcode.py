from PIL import Image
from pyzbar.pyzbar import decode

# abaixo é informado o caminho do QRcode:
imagem = Image.open('C:/Users/Manomeu/PycharmProjects/QRcodeCompiler/imagens/meuqrcode.png')

resultado = decode(imagem)

print(resultado)
