import qrcode

# abaixo é informado o que o QRcode possuirá
data = 'https://fast.com/pt/'  # teste de velocidado do Netflix
imagem = qrcode.make(data)
imagem.save('C:/Users/Manomeu/PycharmProjects/QRcodeCompiler/imagens/meuqrcode.png')
