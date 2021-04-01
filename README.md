# Expert Data Dashboard



A cool Data Science project which will work with datasets and visualization of them.

Working with DATA URLS or/and file upload the project idea is to easily get the URL parameters which contains a dataset or to upload a file with dataset. After reading the dataset to show a side navbar where user can see the columns name in dropdown format and have visualization for them changed dynamically. 



We tried all the use case files, and all of them are readable to the program.  

We did not clearly understood the context in each those folder-files but we did visualization based on the column the user chooses.  Bellow can see the test case list.



<b>Importat: </b>

<b>Due to lack of time we are submiting the project, but there can be some future modifications like adding Ajax to not reload the files each time we choose a new atribute. Other than that there is easy to add another filter to visualise more than one attribute. For example if the user wants to see how many womans has diabets, or how many males smokes etc, we strongly think that if it was a bit more time we would mange to finish this part as well. </b>

Moto: We care for both, front-end and back-end 



> *****
>
> Keep in mind:  
>
> To run the project you must have python installed in your PC. 
>
> Check the requrments.txt file there is a list of the libraries we used to make the project.
>
>  Need to install the libraries, and then will be able to run the project by:
>
>   - open cmd and go to the project directory
>
>   - execute: python manage.py runserver
>
>   - open the localhost link and will be able to see how the project behaves.
>
>     
>
> ***





<h1>Test Cases:</h1>

<h5>Expert Data Dashboard - Data sets:</h5>

```
*******Kategoria Biznes:*******

- [x] Telecom_Customers - 12 pike bonus
	- [x] ID_KLIENTIT
	- [x] GJINIA
	- [x] QYTETARE_IMOSHUAR
	- [x] FAMILJAR(ANTARE)
	- [x] KOHEZGJATJA_KONTRATES_MUAJ
	- [x] SHERBIMI_TELEFONISE
	- [x] LINJA_TE_SHUMFISHTA_PROVIDER
	- [x] sHERBIM_INTERNET
	- [x] ONLINESECURITY
	- [x] ONLINEBACKUP
	- [x] DEVICEPROTECTION
	- [x] SUPORTI_TEKNIK_PERFSHIER
	- [x] STREAMINGTV
	- [x] STREAMINGMOVIES
	- [x] KONTRATA
	- [x] MENYRA_PAGESES
	- [x] TARIFA_MUJORE
	- [x] TARIFAT_TOTALE
	- [x] LESHUAR_PROVIDERIN
	
	

- [x] Credit_Card_Churn_Analytics - 8 pike bonus
	- [x] ID
	- [x] MOSHA
	- [x] GJINIA
	- [x] FAMILJA
	- [x] NIVELI_EDUKIMIT
	- [x] STATUSI_MARTESOR
	- [x] TE_ARDHURAT_VJETORE
	- [x] LLOJI_CC
	- [x] MUAJT_ME_BANKEN
	- [x] MUAJ_JO_AKTIV_GJATEVITIT
	- [x] SA_HERE_KA_KONTAKTUAR_BANKEN
	- [x] CC_LIMITI
	- [x] CC_SHUMA_PERDORUR
	- [x] CC_SHUMA_PAPERDORUR
	- [x] TRANSAKSIONI_FUNDIT
	- [x] INDIKATORI_LARGIM



- [x] Employee_HR_Analytics - 12 pike bonus
	- [x] ID
	- [x] MOSHA
	- [x] UDHETIME_BIZNESORE
	- [x] DEPARTAMENTI
	- [x] DISTANCA_NGA_SHTEPIA
	- [x] FUSHA_EDUKIMIT
	- [x] AMBIENTI_PUNTORIT
	- [x] GJINIA
	- [x] INVOLVIMI_NE_DETYRA_PERGJITHESI
	- [x] NIVELI_PUNES
	- [x] ROLI
	- [x] STATISFAKCIONI_PUNEDHENESIT
	- [x] STATUSI_MARTESOR
	- [x] ARDHURAT_MUJORE
	- [x] NUMRI_KOMPANIVE_QE_KAPUNUAR
	- [x] OVERTIME
	- [x] NGRITJA_RROGES_PERQINDJE
	- [x] VITE_PERVOJE_PUNE
	- [x] NUMRI_TRAJNIMEVE_VITIN_KALUAR
	- [x] BILANCI_PUNE_JETE



- [x] CC_Analytics - 12 pike bonus 
	- [x] CUST_ID
	- [x] BILANCI_AKTUAL
	- [x] FREKUENCA_NDRYSHIMIT_BILANCIT
	- [x] SHUMA_BLERJEVE_NGA_LLOGARIA
	- [x] SHUMA_TRANSACIONIT_METEMADH
	- [x] SHUMA_SI_KEST
	- [x] FREKUENCA_PERDORIMIT_CC
	- [x] NUMRI_BLERJEVE_CC
	- [] CREDIT_LIMIT
	- [x] PJESA_PAGUAR_LIMITIT
	- [] PAGECA_MINIMALE_CDO_MUAJ
	- [X] KOHEZGJATJA_CC

- [X] ATM_Analytics - 15 pike bonus
	- [X] ATMDID
	- [X] ATMEMRI
	- [X] QYTETI
	- [X] ATMADRESA
	- [x] BILANCI_TOTAL
	- [x] NUMRI_INCOMING_TRANSACTIONS
	- [x] NUMRI_OUTGOING_TRANSACTIONS
	- [x] INCOME_TOTAL
	- [x] OUTCOME_TOTAL
	- [x] NUMRI_TOTAL_TRANSACTIONS
	- [x] DATA
	- [x] KOHA_TRANSAKCIONIT



*******Kategoria Shendet:*******

- [x] Stroke_Analytics - 8 pike bonus 
	- [X] ID
	- [X] GJINIA
	- [X] MOXHA
	- [X] HIPERTENSIONI
	- [X] SEMUNDJET_ZEMRES
	- [X] MARTUAR_NDONJEHER
	- [X] LLOJI PUNESIMIT
	- [X] ZONA JETES
	- [X] MESATARJA_GLUKOZES_NIVELI
	- [x] BMI
	- [X] DUHANPIRJA
	- [X] INFRAKT
	

- [x] Suicide_Analytics - 12 pike bonus
	- [X] COUNTRY
	- [X] YEAR
	- [X] SEX
	- [X] AGE
	- [X] SUICIDES_NO
	- [X] POPUPLLATION
	- [X] SUICES/100K POP
	- [X] COUNTRY-YEAR
	- [x] HDI FOR YEAR
	- [X] GDP_FOR_YEAR($)
	- [X] GDP_PER_CAPTA($)
	- [X] GENERATION



*******Kategoria Art/Entertainment:*******
- [] Movie_Analytics - 20 pike bonus
	- [X] ID
	- [X] TIPI
	- [x] TITULLI
	- [] REGJISORI
	- [] AKTORET
	- [X] SHTETI
	- [x] KOHA_E_SHTUAR_PLATFORME
	- [x] VITI_LESHIMIT
	- [x] RITING
	- [x] KOHEZGJATJA
	- [x] LISTUAR_NE_KATEGORINE
	- [] PERSHRKIMI



*******Kategoria Edukim:*******
- [] PISA_Analytics - 20 pike bonus
- [x] Exam_Analytics  0 pike bonus


```

