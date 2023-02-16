import traceback
import emoji
import unicodedata


class TraceHelper:
    def __init__(self):
        self.message = ""
        self.trace = ""
        self.image = ""

    @staticmethod
    def get_trace_str(e):
        traceback_str = ''.join(traceback.format_tb(e.__traceback__))
        return traceback_str

    @staticmethod
    def xml_escape(chars, data_dict):
        return chars.encode('ascii', 'xmlcharrefreplace').decode()

    def contains_emoji(self, text):
        emojis = emoji.emoji_list(text)
        for e in emojis:
            # print(e.emoji)
            # print(emoji.demojize(e))
            # hexcode = hex(ord(e.emoji))
            text = emoji.replace_emoji(text, replace=self.xml_escape)
        print(text)
        return text


TraceHelper().contains_emoji("Juega toda clase de tragamonedas online en Casino Atlantic City  ✅ los mejores premios y bonus los encontrarás aquí 🥇 No te quedes sin jugar.")