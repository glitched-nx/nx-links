"""
Homebrew-Modul zur Verwaltung und Aktualisierung von Nintendo Switch Homebrew-Anwendungen.

Diese Klasse erbt von BaseModule und sammelt Informationen über verschiedene Homebrew-Anwendungen
und Systemprogramme für die Nintendo Switch. Sie durchsucht GitHub-Releases für die neuesten
Versionen von Anwendungen wie Goldleaf, DBI, EdiZon und andere.

Hauptfunktionen:
- Abrufen der neuesten Releases für Homebrew-Anwendungen
- Unterstützung für Pre-Releases bei bestimmten Anwendungen
- Speichern von Download-Links, Versionen und Homebrew-Status

Attribute:
    config (list): Konfigurationsliste mit Repository-Informationen
    out (dict): Wörterbuch mit Informationen über heruntergeladene Anwendungen
"""
from basemodule import BaseModule

class Homebrew(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "XorTroll",
                "reponame": "Goldleaf",
                "assetPatterns": [".*Goldleaf.*\\.nro"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        a=[]
        # homebrews nro-Files
        a.append([{"username": "rashevskyv","reponame": "dbi", "homebrew": True,"assetPatterns": [".*DBI.*\\.nro"]}])
        a.append([{"username": "WerWolv","reponame": "EdiZon", "homebrew": True,"assetPatterns": [".*EdiZon.*\\.nro"]}])
        a.append([{"username": "mtheall","reponame": "ftpd", "homebrew": True,"assetPatterns": [".*ftpd.*\\.nro"]}])
        a.append([{"username": "XorTroll","reponame": "Goldleaf", "homebrew": True,"assetPatterns": [".*Goldleaf.*\\.nro"]}])
        a.append([{"username": "WerWolv","reponame": "Hekate-Toolbox", "homebrew": True,"assetPatterns": [".*HekateToolbox.*\\.nro"]}])
        a.append([{"username": "J-D-K","reponame": "JKSV", "homebrew": True,"assetPatterns": [".*JKSV.*\\.nro"]}])
        a.append([{"username": "tallbl0nde","reponame": "NX-Activity-Log", "homebrew": True,"assetPatterns": [".*NX-Activity-Log.*\\.nro"]}])
        a.append([{"username": "BernardoGiordano","reponame": "Checkpoint", "homebrew": True,"assetPatterns": [".*Checkpoint.*\\.nro"]}])
        # a.append([{"username": "PoloNX","reponame": "SimpleModDownloader", "homebrew": True,"assetPatterns": [".*SimpleModDownloader.*\\.nro"]}])
        # a.append([{"username": "nadrino","reponame": "SimpleModManager", "homebrew": True,"assetPatterns": [".*SimpleModManager.*\\.nro"]}])
        # overlays - homebrews zip-Files
        # a.append([{"username": "glitched-nx","reponame": "quickReloader", "homebrew": False,"assetPatterns": [".*quickReloader.*\\.zip"]}])
        a.append([{"username": "ndeadly","reponame": "MissionControl", "homebrew": False,"assetPatterns": [".*MissionControl.*\\.zip"]}])
        a.append([{"username": "ppkantorski","reponame": "nx-ovlloader", "homebrew": False,"assetPatterns": [".*nx-ovlloader+.*\\.zip"]}])
        a.append([{"username": "glitched-nx","reponame": "UltraHAND", "homebrew": False,"assetPatterns": [".*ovlmenu.*\\.zip"]}])
        a.append([{"username": "glitched-nx","reponame": "ldn_mitm", "homebrew": False,"assetPatterns": [".*ldn_mitm.*\\.zip"]}])
        a.append([{"username": "o0Zz","reponame": "sys-con", "homebrew": False,"assetPatterns": [".*sys-con.*\\.zip"]}])
        a.append([{"username": "HookedBehemoth","reponame": "sys-tune", "homebrew": False,"assetPatterns": [".*sys-tune.*\\.zip"]}])
        for i in a:
            self.config = i
            if self.config[0]["reponame"] == "Goldleaf" or self.config[0]["reponame"] == "emuiibo":
                release = self.get_latest_pre_release(0)
            else:
                release = self.get_latest_release(0)
            asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
            self.out[self.config[0]["reponame"]] = {"name": i[0]["reponame"] , "link": asset[0].browser_download_url, "version": release.tag_name, "homebrew": i[0]["homebrew"]}
