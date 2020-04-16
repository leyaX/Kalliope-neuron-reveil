import time, string, sys, threading, os, re

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
 
        if re.match(r'(..)h(..)',self.heure_reveil) or re.match(r'(..)h',self.heure_reveil) == None: 
                self.say("Ce n'est pas une heure valide!")
        else:
        	test_heure_reveil = len(self.heure_reveil)
	        print("Longeur de la chaine: " + str(test_heure_reveil))
        	print(self.heure_reveil)
        	if test_heure_reveil == 3:
        	        self.reveil = self.heure_reveil.split('h')
        	        self.reveil= self.reveil[0] + ":00"
        	elif test_heure_reveil == 4:
        	        self.reveil = self.heure_reveil.replace('h',':')
        	        self.reveil= "0" + self.reveil
        	else:
        	        self.reveil = self.heure_reveil.replace('h',':')
        	print(self.reveil)
       		self.say("Le réveil est programmé à " + self.reveil )
        	test = True
        	while(test == True):
        	        heure_courante = time.strftime("%H:%M")
        	        print(heure_courante)
        	        print(self.reveil)
        	        time.sleep(1)
        	        if(self.reveil == heure_courante):
        	                print("OK")
        	                os.system("bash /home/pi/barbara/scripts_ya/franceInter.sh")  
        	                test = False




