
import time, string, sys, threading, os

from kalliope.core.NeuronModule import NeuronModule, InvalidParameterException

class Reveil (NeuronModule):
    def __init__(self, **kwargs):
        # we don't need the TTS cache for this neuron
        cache = kwargs.get('cache', None)
        if cache is None:
            cache = False
            kwargs["cache"] = cache

        super(Reveil, self).__init__(**kwargs)
        # get parameters form the neuron
        self.heure_reveil = kwargs.get('heure_reveil', None)

        """Donne l'heure courante au format hh:mm """
        self.temps = time.strftime("%H:%M")
#       self.say("Il est " + self.temps)
        
        """ 
                Ordre: "Réveille-moi à 11 heures"
                Kalliope renvoie 11h
                je doit reformater la chaine pour avoir 11:00
                Je verifie la longueur de la chaine "len()" et j'utilise "str.split('h')"
                Ordre: "Réveille-moi à dix heures 30"
                Kalliope renvoie 10h30
                je doit reformater la chaine pour avoir 10:30
                J'utilise "str.replace('h',':')"
        """

        test_heure_reveil = len(self.heure_reveil)
#       print("Longeur de la chaine: " + str(test_heure_reveil))
        if test_heure_reveil == 3:
                self.reveil = self.heure_reveil.split('h')
                self.reveil= self.reveil[0] + ":00"
#               print(self.reveil)
        else:
                self.reveil = self.heure_reveil.replace('h',':')
#               print(self.reveil)

        self.say("Réveil programmé à " + self.reveil )
        test = True
        while(test == True):
                heure_courante = time.strftime("%H:%M")
#               print(heure_courante)
                time.sleep(1)
                if(self.reveil == heure_courante):
#                       print("OK")
#                        os.system("/usr/bin/mplayer -slave -quiet http://direct.franceinter.fr/live/franceinter-midfi.mp3 &")
                        os.system("bash /home/pi/barbara/scripts_ya/franceInter.sh")  
                        test = False
