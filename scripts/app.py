"""
Repräsentiert eine Anwendung zur Aktualisierung des Blue Pack Updaters.

Diese Klasse erbt von BaseModule und ist speziell für das Abrufen der neuesten Version
des Blue Pack Updaters von GitHub konfiguriert. Sie extrahiert die Download-URL
und Versionsinformationen für die neuste Veröffentlichung.

Attribute:
    config (list): Konfigurationsliste mit GitHub-Repository-Details
    out (dict): Speichert die Download-URL und Version des Blue Pack Updaters
"""
from basemodule import BaseModule

class App(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "glitched-nx",
                "reponame": "bluepack-Updater",
                "assetPatterns": [".*bluepack-Updater.*\\.nro"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        release = self.get_latest_release(0)
        asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
        self.out["bluepack-Updater"] = asset[0].browser_download_url
        self.out["version"] = release.tag_name

