"""
Sigpatches-Modul zur Verwaltung von Signatur-Patches für Retro-Gaming-Repositories.

Dieses Modul erbt von BaseModule und konfiguriert eine Liste von Repositories 
für Signatur-Patches, mit einem Standardkonfigurationseintrag für PHRetroGamers.

Die handle_module()-Methode setzt Standard-Signaturen und Versionen für Patches.

Attribute:
    config (list): Liste von Repository-Konfigurationen mit Benutzername, 
                   Repository-Namen und Asset-Suchmustern.
"""
from basemodule import BaseModule


class Sigpatches(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "PHRetroGamers",
                "reponame": "signature_gpd",
                "assetPatterns": [".*signature_gpd.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        for i in range(len(self.config)):
            self.out["sigpatches"] = "sigmapatches.coomer.party/sigpatches.zip?latest"
            self.out["version"] = "latest"
