from django.shortcuts import render,redirect
import xml.etree.ElementTree as ET
from datetime import datetime
import pandas as pd
from pandas import ExcelWriter
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .forms import SpesoForm
import os


def simple_upload(request):
        form = SpesoForm()
        if request.method == 'POST':
                form = SpesoForm(request.POST, request.FILES)
                mailto = request.POST.get('mailto', '')
                mail = EmailMessage('Spesometro','Hi, Please find attached Spesometro Files.',settings.EMAIL_HOST_USER,[mailto])
                if form.is_valid():
                    for f in request.FILES.getlist('files'):
                            name=os.path.splitext(f.name)[0]
                            type=f.name[0]
                            if type=="E":
                                    Efiles(f,name)
                                    mail.attach_file('/tmp/'+ name + ".xml")
                            elif type=="R":
                                    Rfiles(f,name)
                                    mail.attach_file('/tmp/'+ name + ".xml")
                    mail.send()
                    #return redirect('')
                else:
                    form=SpesoForm()
        return render(request, 'import/import.html', {'form': form})



def Efiles(f,name):
        excel_file = f
        df = pd.read_excel(excel_file)

        DatiFattura=ET.Element('p:DatiFattura')
        DatiFatturaHeader= ET.Element('DatiFatturaHeader')
        Dichiarante= ET.SubElement(DatiFatturaHeader,'Dichiarante')
        CodiceFiscale= ET.SubElement(Dichiarante,'CodiceFiscale')
        Carica= ET.SubElement(Dichiarante,'Carica')
        DTE= ET.SubElement(DatiFattura,'DTE')
        CedentePrestatoreDTE= ET.SubElement(DTE,'CedentePrestatoreDTE')
        IdentificativiFiscali= ET.SubElement(CedentePrestatoreDTE,'IdentificativiFiscali')
        IdFiscaleIVA= ET.SubElement(IdentificativiFiscali,'IdFiscaleIVA')
        IdPaese= ET.SubElement(IdFiscaleIVA,'IdPaese')
        IdCodice= ET.SubElement(IdFiscaleIVA,'IdCodice')
        CodiceFiscale= ET.SubElement(IdentificativiFiscali,'CodiceFiscale')
        AltriDatiIdentificativi= ET.SubElement(CedentePrestatoreDTE,'AltriDatiIdentificativi')
        Denominazione= ET.SubElement(AltriDatiIdentificativi,'Denominazione')
        Sede= ET.SubElement(AltriDatiIdentificativi,'Sede')
        Indirizzo= ET.SubElement(Sede,'Indirizzo')
        NumeroCivico= ET.SubElement(Sede,'NumeroCivico')
        CAP= ET.SubElement(Sede,'CAP')
        Comune= ET.SubElement(Sede,'Comune')
        Provincia= ET.SubElement(Sede,'Provincia')
        Nazione= ET.SubElement(Sede,'Nazione')

        CodiceFiscale_T=df.loc[4,df.columns[0]]
        Carica_T=df.loc[4,df.columns[9]]
        IdPaese_T=df.loc[4,df.columns[2]]
        IdCodice_T=df.loc[4,df.columns[0]]
        Denominazione_T=df.loc[4,df.columns[1]]
        Indirizzo_T=df.loc[4,df.columns[3]]
        NumeroCivico_T=df.loc[4,df.columns[4]]
        CAP_T=df.loc[4,df.columns[5]]
        Comune_T=df.loc[4,df.columns[6]]
        Provincia_T=df.loc[4,df.columns[7]]
        Nazione_T=df.loc[4,df.columns[8]]

        CodiceFiscale.text=str(CodiceFiscale_T)
        Carica.text=str(Carica_T)
        IdPaese.text=str(IdPaese_T)
        IdCodice.text=str(IdCodice_T)
        Denominazione.text=str(Denominazione_T)
        Indirizzo.text=str(Indirizzo_T)
        NumeroCivico.text=str(NumeroCivico_T)
        CAP.text=str(CAP_T)
        Comune.text=str(Comune_T)
        Provincia.text=str(Provincia_T)
        Nazione.text=str(Nazione_T)


        for i  in range(1,len(df)):
                CessionarioCommittenteDTE= ET.SubElement(DTE,'CessionarioCommittenteDTE')
                IdentificativiFiscali2= ET.SubElement(CessionarioCommittenteDTE,'IdentificativiFiscali')
                IdFiscaleIVA2= ET.SubElement(IdentificativiFiscali2,'IdFiscaleIVA')
                IdPaese2= ET.SubElement(IdFiscaleIVA2,'IdPaese')
                IdCodice2= ET.SubElement(IdFiscaleIVA2,'IdCodice')
                CodiceFiscale2= ET.SubElement(IdentificativiFiscali2,'CodiceFiscale')
                AltriDatiIdentificativi2= ET.SubElement(CessionarioCommittenteDTE,'AltriDatiIdentificativi')
                Denominazione2= ET.SubElement(AltriDatiIdentificativi2,'Denominazione')
                Sede2= ET.SubElement(AltriDatiIdentificativi2,'Sede')
                Indirizzo2= ET.SubElement(Sede2,'Indirizzo')
                NumeroCivico2= ET.SubElement(Sede2,'NumeroCivico')
                CAP2= ET.SubElement(Sede2,'CAP')
                Comune2= ET.SubElement(Sede2,'Comune')
                Provincia2= ET.SubElement(Sede2,'Provincia')
                Nazione2= ET.SubElement(Sede2,'Nazione')
                DatiFatturaBodyDTE= ET.SubElement(CessionarioCommittenteDTE,'DatiFatturaBodyDTE')
                DatiGenerali= ET.SubElement(DatiFatturaBodyDTE,'DatiGenerali')
                TipoDocumento= ET.SubElement(DatiGenerali,'TipoDocumento')
                Data= ET.SubElement(DatiGenerali,'Data')
                Numero= ET.SubElement(DatiGenerali,'Numero')
                DataRegistrazione= ET.SubElement(DatiGenerali,'DataRegistrazione')
                DatiRiepilogo= ET.SubElement(DatiFatturaBodyDTE,'DatiRiepilogo')
                ImponibileImporto= ET.SubElement(DatiRiepilogo,'ImponibileImporto')
                DatiIVA= ET.SubElement(DatiRiepilogo,'DatiIVA')
                Imposta= ET.SubElement(DatiIVA,'Imposta')
                Aliquota= ET.SubElement(DatiIVA,'Aliquota')
                Natura= ET.SubElement(DatiRiepilogo,'Natura')

                IdPaese2_T=df.loc[i,df.columns[21]]
                IdCodice2_T=df.loc[i,df.columns[22]]
                Denominazione2_T=df.loc[i,df.columns[24]]
                Indirizzo2_T=df.loc[i,df.columns[27]]
                NumeroCivico2_T=df.loc[i,df.columns[28]]
                CAP2_T=df.loc[i,df.columns[29]]
                Comune2_T=df.loc[i,df.columns[30]]
                Provincia2_T=df.loc[i,df.columns[31]]
                Nazione2_T=df.loc[i,df.columns[32]]
                TipoDocumento_T=df.loc[i,df.columns[10]]
                Data_T=df.loc[i,df.columns[11]]
                Numero_T=df.loc[i,df.columns[12]]
                DataRegistrazione_T=df.loc[i,df.columns[13]]
                ImponibileImporto_T=df.loc[i,df.columns[14]]
                Imposta_T=df.loc[i,df.columns[15]]
                Aliquota_T=df.loc[i,df.columns[16]]*100
                Natura_T=df.loc[i,df.columns[17]]

                IdPaese2.text=str(IdPaese2_T)
                IdCodice2.text=str(IdCodice2_T)
                Denominazione2.text=str(Denominazione2_T)
                Indirizzo2.text=str(Indirizzo2_T)
                NumeroCivico2.text=str(NumeroCivico2_T)
                CAP2.text=str(CAP2_T)
                Comune2.text=str(Comune2_T)
                Provincia2.text=str(Provincia2_T)
                Nazione2.text=str(Nazione2_T)
                TipoDocumento.text=str(TipoDocumento_T)
                Data.text=str(datetime.strftime(Data_T,'%Y-%m-%d'))
                Numero.text=str(Numero_T)
                DataRegistrazione.text=str(datetime.strftime(DataRegistrazione_T,'%Y-%m-%d'))
                ImponibileImporto.text=str(format(ImponibileImporto_T,'.2f'))
                Imposta_T=round(Imposta_T,2)
                Imposta.text=str(format(Imposta_T,'.2f'))
                Aliquota_T=round(Aliquota_T,2)
                Aliquota.text=str(format(Aliquota_T,'.2f'))
                Natura.text=str(Natura_T)


        DatiFattura.set('xmlns:ds', 'http://www.w3.org/2000/09/xmldsig#')
        DatiFattura.set('xmlns:p', 'http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v2.0')
        DatiFattura.set('versione', 'DAT20')
        #create a new XML file with the results
        mydata = ET.tostring(DatiFattura)
        myfile = open('/tmp/'+ name + ".xml",mode='w'+'b')
        begin='<?xml version="1.0" encoding="UTF-8" standalone="no"?><?xml-stylesheet type=''text/xsl'' href=''datifattura_v2.0.xsl''?>'
        myfile.write(begin.encode())
        myfile.write(mydata)


def Rfiles(f,name):
        excel_file = f
        df = pd.read_excel(excel_file)

        DatiFattura = ET.Element('p:DatiFattura')
        DatiFatturaHeader = ET.SubElement(DatiFattura, 'DatiFatturaHeader')
        Dichiarante = ET.SubElement(DatiFatturaHeader, 'Dichiarante')
        CodiceFiscale = ET.SubElement(Dichiarante, 'CodiceFiscale')
        Carica = ET.SubElement(Dichiarante, 'Carica')
        DTR = ET.SubElement(DatiFattura, 'DTR')
        CessionarioCommittenteDTR = ET.SubElement(DTR, 'CessionarioCommittenteDTR')
        IdentificativiFiscali = ET.SubElement(CessionarioCommittenteDTR, 'IdentificativiFiscali')
        IdFiscaleIVA = ET.SubElement(IdentificativiFiscali, 'IdFiscaleIVA')
        IdPaese = ET.SubElement(IdFiscaleIVA, 'IdPaese')
        IdCodice = ET.SubElement(IdFiscaleIVA, 'IdCodice')
        CodiceFiscale = ET.SubElement(IdentificativiFiscali, 'CodiceFiscale')
        AltriDatiIdentificativi = ET.SubElement(CessionarioCommittenteDTR, 'AltriDatiIdentificativi')
        Denominazione = ET.SubElement(AltriDatiIdentificativi, 'Denominazione')
        Sede = ET.SubElement(AltriDatiIdentificativi, 'Sede')
        Indirizzo = ET.SubElement(Sede, 'Indirizzo')
        NumeroCivico = ET.SubElement(Sede, 'NumeroCivico')
        CAP = ET.SubElement(Sede, 'CAP')
        Comune = ET.SubElement(Sede, 'Comune')
        Provincia = ET.SubElement(Sede, 'Provincia')
        Nazione = ET.SubElement(Sede, 'Nazione')

        CodiceFiscale_T = df.loc[4, df.columns[0]]
        Carica_T = df.loc[4, df.columns[9]]
        IdPaese_T = df.loc[4, df.columns[2]]
        IdCodice_T = df.loc[4, df.columns[0]]
        Denominazione_T = df.loc[4, df.columns[1]]
        Indirizzo_T = df.loc[4, df.columns[3]]
        NumeroCivico_T = df.loc[4, df.columns[4]]
        CAP_T = df.loc[4, df.columns[5]]
        Comune_T = df.loc[4, df.columns[6]]
        Provincia_T = df.loc[4, df.columns[7]]
        Nazione_T = df.loc[4, df.columns[8]]

        CodiceFiscale.text = str(CodiceFiscale_T)
        Carica.text = str(Carica_T)
        IdPaese.text = str(IdPaese_T)
        IdCodice.text = str(IdCodice_T)
        Denominazione.text = str(Denominazione_T)
        Indirizzo.text = str(Indirizzo_T)
        NumeroCivico.text = str(NumeroCivico_T)
        CAP.text = str(CAP_T)
        Comune.text = str(Comune_T)
        Provincia.text = str(Provincia_T)
        Nazione.text = str(Nazione_T)

        for i in range(1, len(df)):
                CedentePrestatoreDTR = ET.SubElement(DTR, 'CedentePrestatoreDTR')
                IdentificativiFiscali2 = ET.SubElement(CedentePrestatoreDTR, 'IdentificativiFiscali')
                IdFiscaleIVA2 = ET.SubElement(IdentificativiFiscali2, 'IdFiscaleIVA')
                IdPaese2 = ET.SubElement(IdFiscaleIVA2, 'IdPaese')
                IdCodice2 = ET.SubElement(IdFiscaleIVA2, 'IdCodice')
                CodiceFiscale2 = ET.SubElement(IdentificativiFiscali2, 'CodiceFiscale')
                AltriDatiIdentificativi2 = ET.SubElement(CedentePrestatoreDTR, 'AltriDatiIdentificativi')
                Denominazione2 = ET.SubElement(AltriDatiIdentificativi2, 'Denominazione')
                Sede2 = ET.SubElement(AltriDatiIdentificativi2, 'Sede')
                Indirizzo2 = ET.SubElement(Sede2, 'Indirizzo')
                NumeroCivico2 = ET.SubElement(Sede2, 'NumeroCivico')
                CAP2 = ET.SubElement(Sede2, 'CAP')
                Comune2 = ET.SubElement(Sede2, 'Comune')
                Provincia2 = ET.SubElement(Sede2, 'Provincia')
                Nazione2 = ET.SubElement(Sede2, 'Nazione')
                DatiFatturaBodyDTR = ET.SubElement(CedentePrestatoreDTR, 'DatiFatturaBodyDTR')
                DatiGenerali = ET.SubElement(DatiFatturaBodyDTR, 'DatiGenerali')
                TipoDocumento = ET.SubElement(DatiGenerali, 'TipoDocumento')
                Data = ET.SubElement(DatiGenerali, 'Data')
                Numero = ET.SubElement(DatiGenerali, 'Numero')
                DataRegistrazione = ET.SubElement(DatiGenerali, 'DataRegistrazione')
                DatiRiepilogo = ET.SubElement(DatiFatturaBodyDTR, 'DatiRiepilogo')
                ImponibileImporto = ET.SubElement(DatiRiepilogo, 'ImponibileImporto')
                DatiIVA = ET.SubElement(DatiRiepilogo, 'DatiIVA')
                Imposta = ET.SubElement(DatiIVA, 'Imposta')
                Aliquota = ET.SubElement(DatiIVA, 'Aliquota')
                Natura = ET.SubElement(DatiRiepilogo, 'Natura')

                IdPaese2_T = df.loc[i, df.columns[21]]
                IdCodice2_T = df.loc[i, df.columns[22]]
                Denominazione2_T = df.loc[i, df.columns[24]]
                Indirizzo2_T = df.loc[i, df.columns[27]]
                NumeroCivico2_T = df.loc[i, df.columns[28]]
                CAP2_T = df.loc[i, df.columns[29]]
                Comune2_T = df.loc[i, df.columns[30]]
                Provincia2_T = df.loc[i, df.columns[31]]
                Nazione2_T = df.loc[i, df.columns[32]]
                TipoDocumento_T = df.loc[i, df.columns[10]]
                Data_T = df.loc[i, df.columns[11]]
                Numero_T = df.loc[i, df.columns[12]]
                DataRegistrazione_T = df.loc[i, df.columns[13]]
                ImponibileImporto_T = df.loc[i, df.columns[14]]
                Imposta_T = df.loc[i, df.columns[15]]
                Aliquota_T = df.loc[i, df.columns[16]] * 100
                Natura_T = df.loc[i, df.columns[17]]

                IdPaese2.text = str(IdPaese2_T)
                IdCodice2.text = str(IdCodice2_T)
                Denominazione2.text = str(Denominazione2_T)
                Indirizzo2.text = str(Indirizzo2_T)
                NumeroCivico2.text = str(NumeroCivico2_T)
                CAP2.text = str(CAP2_T)
                Comune2.text = str(Comune2_T)
                Provincia2.text = str(Provincia2_T)
                Nazione2.text = str(Nazione2_T)
                TipoDocumento.text = str(TipoDocumento_T)
                Data.text = str(datetime.strftime(Data_T, '%Y-%m-%d'))
                Numero.text = str(Numero_T)
                DataRegistrazione.text = str(datetime.strftime(DataRegistrazione_T, '%Y-%m-%d'))
                ImponibileImporto.text = str(format(ImponibileImporto_T, '.2f'))
                Imposta_T = round(Imposta_T, 2)
                Imposta.text = str(format(Imposta_T, '.2f'))
                Aliquota_T = round(Aliquota_T, 2)
                Aliquota.text = str(format(Aliquota_T, '.2f'))
                Natura.text = str(Natura_T)

        DatiFattura.set('xmlns:ds', 'http://www.w3.org/2000/09/xmldsig#')
        DatiFattura.set('xmlns:p', 'http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v2.0')
        DatiFattura.set('versione', 'DAT20')
        #create a new XML file with the results
        mydata = ET.tostring(DatiFattura)
        myfile = open('/tmp/'+ name + ".xml",mode='w'+'b')
        begin='<?xml version="1.0" encoding="UTF-8" standalone="no"?><?xml-stylesheet type=''text/xsl'' href=''datifattura_v2.0.xsl''?>'
        myfile.write(begin.encode())
        myfile.write(mydata)
