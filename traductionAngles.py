from enum import Enum


class listAngle(Enum):
    #Rotation en Z de la tête
    MINTETEYAW = -119.5
    MAXTETEYAW = 119.5
    #Rotation en Y de la tête
    MINTETEPITCH = -36.5
    MAXTETEPITCH = 27.5
    #Valeur la plus faible possible pour la hauteur (avant / arrière)
    MINEPAULEPITCH = 117.5
    MAXEPAULEPITCH = -117.5
    #Ecartement épaule
    #( #*-1 dans la fonction pour bras gauche)
    MINEPAULEROLL = -13.00
    MAXEPAULEROLL = 71.00
    #Rotation du coude 
    MINCOUDEYAW = -117.5
    MAXCOUDEYAW = 117.5
    #Flexion du coude 
    #(*-1 dans la fonction pour bras gauche)
    MINCOUDEROLL = 0
    MAXCOUDEROLL = -86.5 
    #Rotation du poignet
    MINPOIGNETROTA = -102.5
    MINPOIGNETROTA = 102.5
    #Rotation inclinaison de la hanche
    MINHANCHEROTATIONINC = -63.60
    MAXHANCHEROTATIONINC = 42.42
    #Ecartement hanche
    #(*-1 dans la fonction pour hanche gauche)
    MINHANCHEECART = -45.27 
    MINHANCHEECART = 21.74  
    #Avant / Arrière hanche
    MINHANCHEPITCH = -86.00
    MAXHANCHEPITCH = 25.73
    #Genou flexion
    MINGENOUFLEX = -5.29
    MAXGENOUFLEX = 121.04
    #Cheville avant/arrière 
    MINCHEVILLEAR = -68.15
    MAXCHEVILLEAR = 52.86
    #Cheville inclinaison 
    #(*-1 dans la fonction pour cheville gauche)
    MINCHEVILLEINC = -44.06
    MAXCHEVILLEINC = 22.79
