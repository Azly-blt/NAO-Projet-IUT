# Test 1 — MJPEG / HTTP 
### (echec du test du aux restrictions administratives)

## Objectif

L'objectif de ce test est d'évaluer une première méthode simple pour transmettre un flux vidéo d'un PC vers un smartphone.

Cette méthode repose sur :

- OpenCV pour récupérer les images de la caméra ;
- une compression JPEG image par image ;
- Flask pour créer un serveur HTTP ;
- un navigateur web sur smartphone pour afficher le flux.

L'idée est de vérifier si cette solution peut être utilisée plus tard pour transmettre la caméra du robot NAO vers le téléphone du joueur.

---

## Architecture testée

```text
Webcam PC
   ↓
OpenCV
   ↓
Compression JPEG
   ↓
Serveur Flask / HTTP
   ↓
Navigateur smartphone
```

Dans le projet final, la webcam du PC serait remplacée par le flux provenant de la caméra du NAO :

```text
Caméra NAO
   ↓
PC
   ↓
MJPEG / HTTP
   ↓
Smartphone
```

---

## Mise en place

Dépendances utilisées :

```bash
pip install flask opencv-python
```

Lancement du serveur :

```bash
python mjpeg_server.py
```

Le serveur écoute sur le port `5000`.

Exemple d'accès depuis un autre appareil du même réseau :

```text
http://IP_DU_PC:5000
```

---

## Test sur machine personnelle

Le premier test a été réalisé sur un PC personnel.

Le PC était connecté au partage de connexion du smartphone afin que les deux appareils soient présents sur le même réseau local.

Résultat :

- le smartphone arrive à accéder au serveur Flask ;
- le flux vidéo de la webcam est correctement affiché dans le navigateur ;
- la fluidité est correcte ;
- la qualité est correcte malgré une webcam de qualité moyenne ;
- la latence observée est suffisamment faible pour rendre la solution intéressante pour un premier prototype.

Le test valide donc le fonctionnement de la chaîne :

```text
PC → serveur HTTP → smartphone
```

---

## Test sur les machines de l'IUT

Le même programme a ensuite été testé sur un PC de l'IUT.

Configuration réseau du PC :

```text
Ethernet IUT
Adresse IPv4 : 172.16.0.145
```

Le serveur Flask fonctionne correctement localement :

```text
http://127.0.0.1:5000
```

Le flux vidéo est bien affiché sur le PC.

En revanche, l'accès depuis un autre appareil ne fonctionne pas :

```text
http://172.16.0.145:5000
```

Tests effectués depuis :

- un smartphone connecté à eduroam ;
- un smartphone utilisant les données mobiles ;
- un autre PC de l'IUT.

Dans tous les cas, la connexion au serveur n'aboutit pas.

---

## Limitation rencontrée

Le problème ne semble pas provenir du programme Flask lui-même puisque le serveur fonctionne correctement en local.

La limitation semble liée à l'environnement réseau des machines de l'IUT.

Les postes sont configurés et protégés par l'infrastructure de l'IUT et nous ne disposons pas des droits nécessaires pour modifier les règles réseau ou le pare-feu.

Une connexion entrante directe vers le serveur HTTP du PC semble donc être bloquée.

L'architecture suivante n'est actuellement pas utilisable sur les machines de l'IUT :

```text
Téléphone
    ↓
connexion entrante HTTP
    ↓
PC IUT
```

---

## Avantages de MJPEG / HTTP

Cette solution présente plusieurs avantages :

- très simple à développer ;
- peu de dépendances ;
- fonctionne directement dans un navigateur ;
- aucun logiciel spécifique nécessaire sur le smartphone ;
- facile à intégrer avec OpenCV ;
- suffisante pour créer rapidement un MVP.

---

## Inconvénients

Plusieurs limites ont également été identifiées :

- chaque image est compressée indépendamment en JPEG ;
- consommation réseau potentiellement importante ;
- moins adapté qu'un véritable protocole vidéo temps réel ;
- la latence peut augmenter en fonction de la qualité du réseau ;
- nécessite que le smartphone puisse se connecter directement au serveur du PC ;
- cette dernière condition n'est actuellement pas satisfaite sur le réseau de l'IUT.

---

## Conclusion

MJPEG / HTTP constitue une solution simple et fonctionnelle pour transmettre une caméra d'un PC vers un smartphone sur un réseau local classique.

Le test effectué avec un PC personnel et un partage de connexion smartphone est concluant : le flux est accessible, relativement fluide et la qualité est correcte.

Cependant, cette solution rencontre une limitation importante dans l'environnement de l'IUT : les connexions entrantes vers les machines semblent être bloquées.

MJPEG / HTTP reste donc intéressant comme solution de référence et comme MVP, mais il est nécessaire d'étudier d'autres méthodes de transmission capables de mieux fonctionner avec les contraintes réseau de l'IUT.

Les prochaines solutions étudiées seront :

1. RTSP / RTP
2. WebRTC
