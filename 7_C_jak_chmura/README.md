# Konspekt

## Co to jest chmura

## Chmura Krajowa

## Prosta aplikacja - Monitorujemy dostawę pizzy

Na potrzeby naszego pokazu zakładamy mało optymalną sytuację: jeden dostawca dostarcza na raz jedną pizze.

Statusy dostawcy:
* LOGIN - zalogowanie do systemu
* IDLE - oczekiwanie na podjęcie dostawy
* TAKE - podjęcie dostawy
* MOVING - przemieszczanie się z paczką
* DELIVERED - dostarczono
* PAUSE - przerwa
* LOGOUT - wylogowanie się z systemu
* ERROR - wypadek, zgubiłem pizzę, zaatakował mnie pies

## Google cloud SDK

https://cloud.google.com/sdk

gcloud auth login
gcloud config set project daftacademy-test  

gcloud functions deploy incoming-event --entry-point incoming_event --runtime python37 --trigger-http --allow-unauthenticated
gcloud functions deploy cid-stats --entry-point cid_stats --runtime python37 --trigger-http --allow-unauthenticated
gcloud functions deploy save_event --entry-point save_event --runtime python37 --trigger-topic incoming-events --allow-unauthenticated
gcloud functions deploy error_notification --entry-point error_notification --runtime python37 --trigger-topic incoming-events --allow-unauthenticated
