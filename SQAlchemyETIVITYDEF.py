##creazione motore di database: è responsabile della connessione al database dell'esecuzione dei comandi SQL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



##connessione al database

mysql_engine=create_engine("mysql://root:$$$$$@localhost:$$$$$$")


##creiamo table direttamente su SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,Date,ForeignKey,DECIMAL,Text

##crea un'istanza MetaData
metadata = MetaData()

#definisci struttura tabella
tabella_utenti = Table(
    'UTENTE', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50)),
    Column('cognome', String(50)),
    Column('email', String(100), unique=True, nullable=False),
    Column('password', String(255), nullable=False),
    Column('telefono1', String(20), nullable=False),
    Column('telefono2', String(20))
)

tabella_provincia = Table(
    'PROVINCIA', metadata,
    Column('idProvincia', Integer, primary_key=True),
    Column('provincia', String(100), nullable=False)
)

tabella_cap = Table(
    'CAP', metadata,
    Column('idCAP', Integer, primary_key=True),
    Column('cap', String(10), nullable=False),
    Column('idProvincia', Integer, ForeignKey('PROVINCIA.idProvincia'))
)

tabella_citta = Table(
    'CITTA', metadata,
    Column('idCittà', Integer, primary_key=True),
    Column('nomeCittà', String(100), nullable=False),
    Column('idCAP', Integer, ForeignKey('CAP.idCAP'))
)

tabella_indirizzi_spedizione = Table(
    'INDIRIZZI_SPEDIZIONE', metadata,
    Column('id', Integer, primary_key=True),
    Column('indirizzo', String(255), nullable=False),
    Column('id_utente', Integer, ForeignKey('UTENTE.id')),
    Column('idCittà', Integer, ForeignKey('CITTA.idCittà'))
)

tabella_condizione_ordine = Table(
    'CONDIZIONE_ORDINE', metadata,
    Column('id', Integer, primary_key=True),
    Column('status_ordine', String(50), nullable=False)
)

tabella_ordine = Table(
    'ORDINE', metadata,
    Column('id', Integer, primary_key=True),
    Column('data_ordine', Date, nullable=False),
    Column('id_utente', Integer, ForeignKey('UTENTE.id')),
    Column('id_status', Integer, ForeignKey('CONDIZIONE_ORDINE.id'))
)

tabella_metodo_pagamento = Table(
    'METODO_PAGAMENTO', metadata,
    Column('id', Integer, primary_key=True),
    Column('tipo_pagamento', String(50), nullable=False)
)

tabella_pagamento = Table(
    'PAGAMENTO', metadata,
    Column('id', Integer, primary_key=True),
    Column('data_pag', Date, nullable=False),
    Column('tot_pag', DECIMAL(10, 2), nullable=False),
    Column('id_ordine', Integer, ForeignKey('ORDINE.id')),
    Column('id_tipopagamento', Integer, ForeignKey('METODO_PAGAMENTO.id'))
)

tabella_metodo_spedizione = Table(
    'METODO_SPEDIZIONE', metadata,
    Column('id', Integer, primary_key=True),
    Column('tipo_spedizione', String(50), nullable=False)
)

tabella_spedizione = Table(
    'SPEDIZIONE', metadata,
    Column('id', Integer, primary_key=True),
    Column('data_spedizione', Date, nullable=False),
    Column('idOrdine', Integer, ForeignKey('ORDINE.id')),
    Column('idTipoSpedizione', Integer, ForeignKey('METODO_SPEDIZIONE.id'))
)

tabella_categoria = Table(
    'CATEGORIA', metadata,
    Column('idCategoria', Integer, primary_key=True),
    Column('nomeCategoria', String(50), nullable=False)
)

tabella_prodotto = Table(
    'PRODOTTO', metadata,
    Column('id', Integer, primary_key=True),
    Column('marca_sella', String(50), nullable=False),
    Column('prezzo', DECIMAL(10, 2), nullable=False),
    Column('idCategoria', Integer, ForeignKey('CATEGORIA.idCategoria'))
)

tabella_linea_ordine = Table(
    'LINEA_ORDINE', metadata,
    Column('NumeroLinea', Integer, primary_key=True),
    Column('idOrdine', Integer, ForeignKey('ORDINE.id')),
    Column('idProdotto', Integer, ForeignKey('PRODOTTO.id')),
    Column('quantità', Integer, nullable=False)
)

tabella_recensione = Table(
    'RECENSIONE', metadata,
    Column('idProdotto', Integer, ForeignKey('PRODOTTO.id'), primary_key=True),
    Column('idUtente', Integer, ForeignKey('UTENTE.id'), primary_key=True),
    Column('commento', Text)
)

tabella_magazzino = Table(
    'MAGAZZINO', metadata,
    Column('id', Integer, primary_key=True),
    Column('nomeMagazzino', String(100), nullable=False)
)

tabella_locazione = Table(
    'LOCAZIONE', metadata,
    Column('idProdotto', Integer, ForeignKey('PRODOTTO.id'), primary_key=True),
    Column('idMagazzino', Integer, ForeignKey('MAGAZZINO.id'), primary_key=True),
    Column('disponibilità', Integer, nullable=False)
)

tabella_vetrina = Table(
    'VETRINA', metadata,
    Column('id', Integer, primary_key=True),
    Column('descrizione', Text, nullable=False)
)

tabella_visualizzabile_in = Table(
    'VISUALIZZABILE_IN', metadata,
    Column('idProdotto', Integer, ForeignKey('PRODOTTO.id'), primary_key=True),
    Column('idVetrina', Integer, ForeignKey('VETRINA.id'), primary_key=True),
    Column('immagine_evidenza', Text)
)

# Effettua la migrazione per creare le tabelle nel database
metadata.create_all(mysql_engine)

#crea una sessione 
Session = sessionmaker(bind=mysql_engine)
sessione=Session()

##inserisci valori per la tabella (esempio inserisco solo per tabella utente)
ins = tabella_utenti.insert().values({
    {'nome': 'Cl', 'cognome':'Rrg','email':'clRrg..in.com','password':'09ibn98ijnbuijo93&&','telefono1':'33132465780000999490'},
    {'nome':'wi','cognome':'wiggle','email':'fnchywiggle.poli.com','password':'8u8hhbui4i9jn','telefono1':'3344531999999908765','telefono2':'009867650000938790'}

})
##esegui la query di inserimento a cui è stata assegnata una sessione
session.execute(ins)
ins_provincia = tabella_provincia.insert().values([
    {'idProvincia': 1, 'provincia': 'Roma'},
    {'idProvincia': 2, 'provincia': 'Milano'}
])
session.execute(ins_provincia)

ins_cap = tabella_cap.insert().values([
    {'idCAP': 1, 'cap': '00100', 'idProvincia': 1},
    {'idCAP': 2, 'cap': '20100', 'idProvincia': 2}
])
session.execute(ins_cap)

ins_citta = tabella_citta.insert().values([
    {'idCittà': 1, 'nomeCittà': 'Roma', 'idCAP': 1},
    {'idCittà': 2, 'nomeCittà': 'Milano', 'idCAP': 2}
])
session.execute(ins_citta)

ins_indirizzi_spedizione = tabella_indirizzi_spedizione.insert().values([
    {'id': 1, 'indirizzo': 'Via Roma 1', 'id_utente': 1, 'idCittà': 1},
    {'id': 2, 'indirizzo': 'Via Milano 1', 'id_utente': 2, 'idCittà': 2}
])
session.execute(ins_indirizzi_spedizione)

ins_condizione_ordine = tabella_condizione_ordine.insert().values([
    {'id': 1, 'status_ordine': 'Confermato'},
    {'id': 2, 'status_ordine': 'Spedito'}
])
session.execute(ins_condizione_ordine)

ins_ordine = tabella_ordine.insert().values([
    {'id': 1, 'data_ordine': '2023-01-01', 'id_utente': 1, 'id_status': 1},
    {'id': 2, 'data_ordine': '2023-02-01', 'id_utente': 2, 'id_status': 2}
])
session.execute(ins_ordine)

ins_metodo_pagamento = tabella_metodo_pagamento.insert().values([
    {'id': 1, 'tipo_pagamento': 'Carta di credito'},
    {'id': 2, 'tipo_pagamento': 'PayPal'}
])
session.execute(ins_metodo_pagamento)

ins_pagamento = tabella_pagamento.insert().values([
    {'id': 1, 'data_pag': '2023-01-02', 'tot_pag': 100.00, 'id_ordine': 1, 'id_tipopagamento': 1},
    {'id': 2, 'data_pag': '2023-02-02', 'tot_pag': 200.00, 'id_ordine': 2, 'id_tipopagamento': 2}
])
session.execute(ins_pagamento)

ins_metodo_spedizione = tabella_metodo_spedizione.insert().values([
    {'id': 1, 'tipo_spedizione': 'corriere espresso'},
    {'id': 2, 'tipo_spedizione': 'corriere tradizionale'}
])
session.execute(ins_metodo_spedizione)

ins_spedizione = tabella_spedizione.insert().values([
    {'id': 1, 'data_spedizione': '2023-01-03', 'idOrdine': 1, 'idTipoSpedizione': 1},
    {'id': 2, 'data_spedizione': '2023-02-03', 'idOrdine': 2, 'idTipoSpedizione': 2}
])
session.execute(ins_spedizione)
ins_categoria = tabella_categoria.insert().values([
    {'idCategoria': 1, 'nomeCategoria': 'sella inglese'},
    {'idCategoria': 2, 'nomeCategoria': 'sella western'}
])
session.execute(ins_categoria)

ins_prodotto = tabella_prodotto.insert().values([
    {'id': 1, 'marca_sella': 'ACAVALLO', 'prezzo': 599.99, 'idCategoria': 1},
    {'id': 2, 'marca_sella': 'EEQUESTRO', 'prezzo': 79.99, 'idCategoria': 2}
])
session.execute(ins_prodotto)

ins_linea_ordine = tabella_linea_ordine.insert().values([
    {'NumeroLinea': 1, 'idOrdine': 1, 'idProdotto': 1, 'quantità': 1},
    {'NumeroLinea': 2, 'idOrdine': 2, 'idProdotto': 2, 'quantità': 2}
])
session.execute(ins_linea_ordine)

ins_recensione = tabella_recensione.insert().values([
    {'idProdotto': 1, 'idUtente': 1, 'commento': 'Ottimo prodotto!'},
    {'idProdotto': 2, 'idUtente': 2, 'commento': 'Molto comodo.'}
])
session.execute(ins_recensione)

ins_magazzino = tabella_magazzino.insert().values([
    {'id': 1, 'nomeMagazzino': 'Magazzino Centrale'},
    {'id': 2, 'nomeMagazzino': 'Magazzino Nord'}
])
session.execute(ins_magazzino)

ins_locazione = tabella_locazione.insert().values([
    {'idProdotto': 1, 'idMagazzino': 1, 'disponibilità': 50},
    {'idProdotto': 2, 'idMagazzino': 2, 'disponibilità': 100}
])
session.execute(ins_locazione)

ins_vetrina = tabella_vetrina.insert().values([
    {'id': 1, 'descrizione': 'Vetrina Principale'},
    {'id': 2, 'descrizione': 'Vetrina Sconti'}
])
session.execute(ins_vetrina)

ins_visualizzabile_in = tabella_visualizzabile_in.insert().values([
    {'idProdotto': 1, 'idVetrina': 1, 'immagine_evidenza': 'img/ACAVALLO.jpg'},
    {'idProdotto': 2, 'idVetrina': 2, 'immagine_evidenza': 'img/EQUESTRO.jpg'}
])
session.execute(ins_visualizzabile_in)

session.commit()

session.close()

#operazione di aggiornamento
upd = tabella_utenti.update().where(tabella_utenti.c.cognome=='wiggle').values(cognome='worry')


#esegui query di aggiornamento
session.execute(upd)

upd2 = tabella_magazzino.update().where(tabella_magazzino.c.nomeMagazzino=='Magazzino centrale').values(nomeMagazzino='Magazzino Sud')

session.execute(upd2)

#conferma le operazioni
session.commit()

#chiudi la sessione
session.close()


##cancellazione
rem = tabella_utenti.delete().where(tabella_utenti.c.cognome=='wiggle')
session.execute(rem)

rem2 = tabella_prodotto.delete().where(tabella_prodotto.c.marca_sella == 'ACAVALLO')
session.execute(rem2)



session.commit()
session.close()

##eseguire query select 
s = tabella_utenti.select().where(tabella_utenti.c.nome=='Cl')
##esegui la query e ottieni i risultati
result=session.execute(s)
row = result.fetchone()

session.commit()
session.close()

while row is not None:
    print(row)
    row = result.fetchone()
