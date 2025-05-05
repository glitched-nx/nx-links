"""
Repräsentiert ein Tab-Modul, das verschiedene Installationsoptionen für Systemkomponenten verwaltet.

Diese Klasse erbt von BaseModule und initialisiert eine Konfiguration für verschiedene 
Installationskategorien wie Pack, App, Homebrew, Firmware und sigpatches.

Attribute:
    out (dict): Ein Wörterbuch, das den Installationsstatus verschiedener Komponenten angibt.
        - "Pack": True
        - "App": True
        - "Homebrew": True
        - "Firmware": True
        - "sigpatches": False
"""
from basemodule import BaseModule


class Tab(BaseModule):
    def __init__(self):
        BaseModule.__init__(self)

    def handle_module(self):
        self.out = {
            "Pack" : True,
            "App" : True,
            "Homebrew" : True,
            "Firmware" : True,
            "sigpatches" : False
        }
