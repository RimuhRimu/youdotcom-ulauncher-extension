import webbrowser

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction 


class YouExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event: KeywordQueryEvent, _):
        url = "https://you.com/search?q=" + event.get_argument() or ""
        items = [
                ExtensionResultItem(
                                    icon='images/icon.svg',
                                    name=url,
                                    on_enter=ExtensionCustomAction(url,keep_app_open=False)
                                    )
                ]
        return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):

    def on_event(self, event:ItemEnterEvent, _):

        url = event.get_data()

        webbrowser.open(url)

        return RenderResultListAction([ExtensionResultItem(icon='images/icon.svg',
                                                           name=url,
                                                           on_enter=HideWindowAction())])
if __name__ == '__main__':
    YouExtension().run()

