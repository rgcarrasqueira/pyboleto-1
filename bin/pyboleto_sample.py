#!/Users/dudus/Work/pyboleto/venv/bin/python
# -*- coding: utf-8 -*-
import pyboleto
from pyboleto.bank.real import BoletoReal
from pyboleto.bank.bradesco import BoletoBradesco
from pyboleto.bank.caixa import BoletoCaixa, BoletoCaixaSIGCB
from pyboleto.bank.bancodobrasil import BoletoBB
from pyboleto.bank.santander import BoletoSantander
from pyboleto.bank.banconordeste import BoletoBancoNordeste
from pyboleto.bank.bancoob import BoletoBancoob
from pyboleto.bank.bancodaamazonia import BoletoBancodaAmazonia
from pyboleto.bank.sicredi import BoletoSicredi

from pyboleto.pdf import BoletoPDF
import datetime


def print_bb():
    listaDados = []
    for i in range(2):
        d = BoletoBB(7, 2)
        d.nosso_numero = '87654'
        d.numero_documento = '27.030195.10'
        d.convenio = '7777777'
        d.especie_documento = 'DM'

        d.carteira = '18'
        d.cedente = 'Empresa ACME LTDA'
        d.cedente_documento = "102.323.777-01"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
        d.agencia_cedente = '9999'
        d.conta_cedente = '99999'

        d.data_vencimento = datetime.date(2010, 3, 27)
        d.data_documento = datetime.date(2010, 2, 12)
        d.data_processamento = datetime.date(2010, 2, 12)

        d.instrucoes = [
            "- Linha 1",
            "- Sr Caixa, cobrar multa de 2% após o vencimento",
            "- Receber até 10 dias após o vencimento",
            ]
        d.demonstrativo = [
            "- Serviço Teste R$ 5,00",
            "- Total R$ 5,00",
            ]
        d.valor_documento = 255.00

        d.sacado = [
            "Cliente Teste %d" % (i + 1),
            "Rua Desconhecida, 00/0000 - Não Sei - Cidade - Cep. 00000-000",
            ""
            ]
        listaDados.append(d)

    boleto = BoletoPDF('boleto-bb-formato-normal-teste.pdf')
    for i in range(len(listaDados)):
        boleto.drawBoleto(listaDados[i])
        boleto.nextPage()
    boleto.save()


def print_real():
    listaDadosReal = []
    for i in range(2):
        d = BoletoReal()
        d.carteira = '57'  # Contrato firmado com o Banco Real
        d.cedente = 'Empresa ACME LTDA'
        d.cedente_documento = "102.323.777-01"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
        d.agencia_cedente = '0531'
        d.conta_cedente = '5705853'

        d.data_vencimento = datetime.date(2010, 3, 27)
        d.data_documento = datetime.date(2010, 2, 12)
        d.data_processamento = datetime.date(2010, 2, 12)

        d.instrucoes = [
            "- Linha 1",
            "- Sr Caixa, cobrar multa de 2% após o vencimento",
            "- Receber até 10 dias após o vencimento",
            ]
        d.demonstrativo = [
            "- Serviço Teste R$ 5,00",
            "- Total R$ 5,00",
            ]
        d.valor_documento = 5.00

        d.nosso_numero = "%d" % (i + 2)
        d.numero_documento = "%d" % (i + 2)
        d.sacado = [
            "Cliente Teste %d" % (i + 1),
            "Rua Desconhecida, 00/0000 - Não Sei - Cidade - Cep. 00000-000",
            ""
            ]
        listaDadosReal.append(d)

    # Real Formato normal - uma pagina por folha A4
    boleto = BoletoPDF('boleto-real-formato-normal-teste.pdf')
    for i in range(len(listaDadosReal)):
        boleto.drawBoleto(listaDadosReal[i])
        boleto.nextPage()
    boleto.save()


def print_bradesco():
    listaDadosBradesco = []
    for i in range(2):
        d = BoletoBradesco()
        d.carteira = '06'  # Contrato firmado com o Banco Bradesco
        d.cedente = 'Empresa ACME LTDA'
        d.cedente_documento = "102.323.777-01"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
        d.agencia_cedente = '0278-0'
        d.conta_cedente = '43905-3'

        d.data_vencimento = datetime.date(2011, 1, 25)
        d.data_documento = datetime.date(2010, 2, 12)
        d.data_processamento = datetime.date(2010, 2, 12)

        d.instrucoes = [
            "- Linha 1",
            "- Sr Caixa, cobrar multa de 2% após o vencimento",
            "- Receber até 10 dias após o vencimento",
            ]
        d.demonstrativo = [
            "- Serviço Teste R$ 5,00",
            "- Total R$ 5,00",
            ]
        d.valor_documento = 2158.41

        d.nosso_numero = "1112011668"
        d.numero_documento = "1112011668"
        d.sacado = [
            "Cliente Teste %d" % (i + 1),
            "Rua Desconhecida, 00/0000 - Não Sei - Cidade - Cep. 00000-000",
            ""
            ]
        listaDadosBradesco.append(d)

    # Bradesco Formato carne - duas paginas por folha A4
    boleto = BoletoPDF('boleto-bradesco-formato-carne-teste.pdf', True)
    for i in range(0, len(listaDadosBradesco), 2):
        boleto.drawBoletoCarneDuplo(
            listaDadosBradesco[i],
            listaDadosBradesco[i + 1]
        )
        boleto.nextPage()
    boleto.save()

    # Bradesco Formato normal - uma pagina por folha A4
    boleto = BoletoPDF('boleto-bradesco-formato-normal-teste.pdf')
    for i in range(len(listaDadosBradesco)):
        boleto.drawBoleto(listaDadosBradesco[i])
        boleto.nextPage()
    boleto.save()


def print_santander():
    listaDadosSantander = []
    for i in range(2):
        d = BoletoSantander()
        d.agencia_cedente = '1333'
        d.conta_cedente = '0707077'
        d.data_vencimento = datetime.date(2012, 7, 22)
        d.data_documento = datetime.date(2012, 7, 17)
        d.data_processamento = datetime.date(2012, 7, 17)
        d.valor_documento = 2952.95
        d.nosso_numero = '1234567'
        d.numero_documento = '12345'
        d.ios = '0'

        d.cedente = 'Empresa ACME LTDA'
        d.cedente_documento = "102.323.777-01"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"

        d.instrucoes = [
            "- Linha 1",
            "- Sr Caixa, cobrar multa de 2% após o vencimento",
            "- Receber até 10 dias após o vencimento",
            ]
        d.demonstrativo = [
            "- Serviço Teste R$ 5,00",
            "- Total R$ 5,00",
            ]
        d.valor_documento = 255.00

        d.sacado = [
            "Cliente Teste %d" % (i + 1),
            "Rua Desconhecida, 00/0000 - Não Sei - Cidade - Cep. 00000-000",
            ""
            ]
        listaDadosSantander.append(d)

    # Caixa Formato normal - uma pagina por folha A4
    boleto = BoletoPDF('boleto-santander-formato-normal-teste.pdf')
    for i in range(len(listaDadosSantander)):
        boleto.drawBoleto(listaDadosSantander[i])
        boleto.nextPage()
    boleto.save()


def print_caixa():
    listaDadosCaixa = []
    for i in range(2):
        d = BoletoCaixaSIGCB()
        d.carteira = 'SR'  # Contrato firmado com o Banco Bradesco
        d.cedente = 'Empresa ACME LTDA'
        d.cedente_documento = "102.323.777-01"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
        d.agencia_cedente = '2010'
        d.conta_cedente = '074532'
        d.inicio_nosso_numero='24'
        d.data_vencimento = datetime.date(2011, 3, 10)
        d.data_documento = datetime.date(2012, 9, 22)
        d.data_processamento = datetime.date(2012, 9, 22)

        d.instrucoes = [
            "- Linha 1",
            "- Sr Caixa, cobrar multa de 2% após o vencimento",
            "- Receber até 10 dias após o vencimento",
            ]
        d.demonstrativo = [
            "- Serviço Teste R$ 5,00",
            "- Total R$ 5,00",
            ]
        d.valor_documento = 50.00

        d.nosso_numero = "605353"
        d.numero_documento = "5361"
        d.sacado = [
            "Cliente Teste %d" % (i + 1),
            "Rua Desconhecida, 00/0000 - Não Sei - Cidade - Cep. 00000-000",
            ""
            ]
        listaDadosCaixa.append(d)

    # Caixa Formato normal - uma pagina por folha A4
    boleto = BoletoPDF('boleto-caixa-formato-carne-teste.pdf', True)
    for i in range(0, len(listaDadosCaixa), 2):
        boleto.drawBoletoCarneDuplo(
            listaDadosCaixa[i],
            listaDadosCaixa[i + 1]
        )
        boleto.nextPage()
    boleto.save()

    # Caixa Formato normal - uma pagina por folha A4
    boleto = BoletoPDF('boleto-caixa-formato-normal-teste.pdf')
    for i in range(len(listaDadosCaixa)):
        boleto.drawBoleto(listaDadosCaixa[i])
        boleto.nextPage()
    boleto.save()


def print_itau():
    pass

def print_banconordeste():
    listaDadosBancoNordeste = []
    for i in range(2):
        d = BoletoBancoNordeste()
        d.carteira = '51'  # Contrato firmado com o Banco BancoNordeste
        d.cedente = 'CONNECT'
        d.cedente_documento = "102.323.777-01"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
        d.agencia_cedente = '0226'
        d.conta_cedente = '0000085'
        d.conta_cednte_dv = '0'

        d.data_vencimento = datetime.date(2014, 6, 10)
        d.data_documento = datetime.date(2014, 4, 8)
        d.data_processamento = datetime.date(2015, 4, 8)

        d.instrucoes = [
            "- Linha 1",
            "- Sr Caixa, cobrar multa de 2% após o vencimento",
            "- Receber até 10 dias após o vencimento",
            ]
        d.demonstrativo = [
            "- Serviço Teste R$ 5,00",
            "- Total R$ 5,00",
            ]
        d.valor_documento = 65.00

        d.nosso_numero = "0055298"
        d.numero_documento = "55298"
        d.sacado = [
            "Cliente Teste %d" % (i + 1),
            "Rua Desconhecida, 00/0000 - Não Sei - Cidade - Cep. 00000-000",
            ""
            ]
        listaDadosBancoNordeste.append(d)

    # BancoNordeste Formato carne - duas paginas por folha A4
    boleto = BoletoPDF('boleto-BancoNordeste-formato-carne-teste.pdf', True)
    for i in range(0, len(listaDadosBancoNordeste), 2):
        boleto.drawBoletoCarneDuplo(
            listaDadosBancoNordeste[i],
            listaDadosBancoNordeste[i + 1]
        )
        boleto.nextPage()
    boleto.save()

    # BancoNordeste Formato normal - uma pagina por folha A4
    boleto = BoletoPDF('boleto-BancoNordeste-formato-normal-teste.pdf')
    for i in range(len(listaDadosBancoNordeste)):
        boleto.drawBoleto(listaDadosBancoNordeste[i])
        boleto.nextPage()
    boleto.save()


def print_sicoob():
    listaDadosBancoob = []
    for i in range(2):
        d = BoletoBancoob()
        d.carteira = '1'       
        d.cedente = 'CLIENTE TESTE'
        d.cedente_documento = "102.323.777-01"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
        d.agencia_cedente = '4293'
        d.conta_cedente = '44563'
        d.convenio = '44563'
        d.modalidade_cobranca='02'
        d.numero_parcela='001'
        d.data_vencimento = datetime.date(2014, 9, 16)
        d.data_documento = datetime.date(2014, 6, 16)
        d.data_processamento = datetime.date(2014, 6, 16)

        d.instrucoes = [
            "- Linha 1",
            "- Sr Caixa, cobrar multa de 2% após o vencimento",
            "- Receber até 10 dias após o vencimento",
            ]
        d.demonstrativo = [
            "- Serviço Teste R$ 5,00",
            "- Total R$ 5,00",
            ]
        d.valor_documento = 9.00

        d.nosso_numero = "50149"
        d.numero_documento = "48958"
        
        d.sacado = [
            "Cliente Teste %d" % (i + 1),
            "Rua Desconhecida, 00/0000 - Não Sei - Cidade - Cep. 00000-000",
            ""
            ]
        listaDadosBancoob.append(d)

    # Bancoob Formato carne - duas paginas por folha A4
    boleto = BoletoPDF('boleto-Bancoob-formato-carne-teste.pdf', True)
    for i in range(0, len(listaDadosBancoob), 2):
        boleto.drawBoletoCarneDuplo(
            listaDadosBancoob[i],
            listaDadosBancoob[i + 1]
        )
        boleto.nextPage()
    boleto.save()

    # Bancoob Formato normal - uma pagina por folha A4
    boleto = BoletoPDF('boleto-Bancoob-formato-normal-teste.pdf')
    for i in range(len(listaDadosBancoob)):
        boleto.drawBoleto(listaDadosBancoob[i])
        boleto.nextPage()
    boleto.save()

def print_amazonia():
    listaDados = []
    for i in range(2):
        d = BoletoBancodaAmazonia()
        d.nosso_numero = '123'
        d.numero_documento = '123'
        d.convenio = '0001'
        d.especie_documento = 'DS'
        d.carteira = 'CNR'
        d.cedente = 'Empresa ACME LTDA'
        d.cedente_documento = "102.323.777-01"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
        d.agencia_cedente = '0078'
        d.conta_cedente = '0000011'

        d.data_vencimento = datetime.date(2008, 6, 27)
        d.data_documento = datetime.date(2008, 6, 5)
        d.data_processamento = datetime.date(2008, 6,5)

        d.instrucoes = [
            "- Linha 1",
            "- Sr Caixa, cobrar multa de 2% após o vencimento",
            "- Receber até 10 dias após o vencimento",
            ]
        d.demonstrativo = [
            "- Serviço Teste R$ 5,00",
            "- Total R$ 5,00",
            ]
        d.valor_documento = 15.56

        d.sacado = [
            "Cliente Teste %d" % (i + 1),
            "Rua Desconhecida, 00/0000 - Não Sei - Cidade - Cep. 00000-000",
            ""
            ]
        listaDados.append(d)

    boleto = BoletoPDF('boleto-basa-formato-normal-teste.pdf')
    for i in range(len(listaDados)):
        boleto.drawBoleto(listaDados[i])
        boleto.nextPage()
    boleto.save()


def print_sicredi():
    listaDados = []
    for i in range(2):
        d = BoletoSicredi('06','5','1')
        d.nosso_numero = '13871'
        d.numero_documento = '2700'
        d.especie_documento = 'DS'
        d.carteira = '1'
        d.cedente = 'Empresa ACME LTDA'
        d.cedente_documento = "102.323.777-01"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
        d.agencia_cedente = '1234'
        d.conta_cedente = '12345'
        d.conta_cedente_dv = '6'
        
        d.inicio_nosso_numero='08'


        d.data_vencimento = datetime.date(2008, 6, 27)
        d.data_documento = datetime.date(2008, 6, 5)
        d.data_processamento = datetime.date(2008, 6,5)

        d.instrucoes = [
            "- Linha 1",
            "- Sr Caixa, cobrar multa de 2% após o vencimento",
            "- Receber até 10 dias após o vencimento",
            ]
        d.demonstrativo = [
            "- Serviço Teste R$ 5,00",
            "- Total R$ 5,00",
            ]
        d.valor_documento = 2950.00

        d.sacado = [
            "Cliente Teste %d" % (i + 1),
            "Rua Desconhecida, 00/0000 - Não Sei - Cidade - Cep. 00000-000",
            ""
            ]
        listaDados.append(d)

    boleto = BoletoPDF('boleto-sicredi-formato-normal-teste.pdf')
    for i in range(len(listaDados)):
        boleto.drawBoleto(listaDados[i])
        boleto.nextPage()
    boleto.save()



def print_all():
    print "Pyboleto version: %s" % pyboleto.__version__
    print "----------------------------------"
    print "     Printing Example Boletos     "
    print "----------------------------------"
    
    print "Banco do Brasil"
    print_bb()
    
    print "Bradesco"
    print_bradesco()
    
    #print "Itau"
    #print_itau()

    print "Caixa"
    print_caixa()

    print "Real"
    print_real()
    
    print "Santander"
    print_santander()

    print "Banco Nordeste"
    print_banconordeste()

    print "Bancoob/Sicoob"
    print_sicoob()

    print "banco da amazonia"
    print_amazonia()

    print "sicredi"
    print_sicredi()

    print "----------------------------------"
    print "Ok"





if __name__ == "__main__":
    print_all()
