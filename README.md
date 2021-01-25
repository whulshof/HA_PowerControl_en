# HA_PowerControl
Il package seguente, unito allo script python "update_entities.py" mira ad evitare il distacco del contatore a causa della troppa potenza assorbita dai vari elettrodomestici (carichi).
Requisito hardware fondamentale è la presenza di switch sui carichi da controllare e di un sensore che misura la potenza dei singoli carichi. 
Personalmente ho utilizzato dispositivi Shelly 1PM e Shelly Plug S, perfetti per lo scopo.
E' consigliato, ma non tassativo, l'utilizzo di un sensore che monitori il consumo complessivo dell'impianto (es. Shelly EM).
La logica prevede che in caso l'utilizzo complessivo superi il valore limite impostato, il pacchetto inizi il distacco dei carichi a minore priorità fino a quelli a maggiore priorità,fino a che l'utilizzo complessivo della potenza rientri nel limite prefissato.
Lo script tiene memoria dell'assorbimento del carico prima del distacco e lo ricollega solo quando la disponibilità di potenza è sufficiente a non causare un nuovo distacco.
La configurazione è interamente tramite interfaccia lovelace, tranne il gruppo di notifica (notify.tutti) che va impostato manualmente.
Il pacchetto è funzionante ma non ottimizzato.

# Installazione
- Copiare il file "pc.yaml" nella directory "packages"
- Copiare il file "update_entities.py" nella directory "python_scripts"
- Abilitare i packages: https://www.home-assistant.io/docs/configuration/packages/
- Abilitare gli script python: https://www.home-assistant.io/integrations/python_script/
- Aggiungere il contenuto del file "pc_lovelace.yaml" all'interfaccia Lovelace.
- Creare un gruppo di notifica "notify.tutti" nel file "configuration.yaml" ed inserirvi i device che riceveranno le notifiche di intervento.

# Configurazione
Impostare i parametri di configurazione dell'interfaccia grafica Lovelace.
