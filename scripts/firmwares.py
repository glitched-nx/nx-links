"""
Firmware-Modul zur Verwaltung und Extraktion von Firmware-Releases aus GitHub-Repositories.

Diese Klasse erbt von BaseModule und ermöglicht das Abrufen von Firmware-Assets
aus konfigurierten GitHub-Repositories. Sie durchsucht Releases nach Firmware-Zip-Dateien
und speichert deren Download-URLs.

Attribute:
    config (list): Liste von Konfigurationen mit Repository-Details
        - username (str): GitHub-Benutzername
        - reponame (str): Name des GitHub-Repositories
        - assetPatterns (list): Regex-Muster zur Identifikation relevanter Assets

Methoden:
    handle_module(): Durchsucht konfigurierte Repositories nach Firmware-Releases
"""
import re
from basemodule import BaseModule

class Firmwares(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "THZoria",
                "reponame": "NX_Firmware",
                "assetPatterns": [".*Firmware.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        for i in range(len(self.config)):
            release = self.get_releases(i)
            for j in range(release.totalCount):
                assets = self.get_asset_links(release[j], i)
                for asset in assets:
                    self.out[release[j].title] = asset.browser_download_url
