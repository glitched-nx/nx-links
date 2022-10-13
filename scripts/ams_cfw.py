from basemodule import BaseModule

class Ams_cfw(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "THZoria",
                "reponame": "AtmoPack-Vanilla",
                "assetPatterns": [".*AtmoPack-Vanilla_Latest.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        for i in range(len(self.config)): 
            release = self.get_latest_release(i)
            assets = self.get_asset_links(release, i)
            for asset in assets:
                self.out[release.title] = asset.browser_download_url
            self.out["version"] = release.tag_name

            pre_release = self.get_latest_pre_release(i)
            pre_assets = self.get_asset_links(release, i)
            for asset in pre_assets:
                self.out[pre_release.title] = asset.browser_download_url
            self.out["version-beta"] = pre_release.tag_name

