class ExtractorArgUrl():
    def __init__(self, url):
        if self.valid_url(url):        
            self.url = url
        else:
            raise LookupError("Invalid URL provided")

    @staticmethod
    def valid_url(url):
        if url == None:
            return False
        else:
            return True

    def get_arguments(self):

        tag_orin_currency = "moedaorigem"
        tag_dest_currency = "moedadestino"

        init_index_orin_currency = self.find_start_index_substring(tag_orin_currency)
        end_index_orin_currency = self.url.find("&")
        original_currency = self.url[init_index_orin_currency:end_index_orin_currency]

        init_index_dest_currency = self.find_start_index_substring(tag_dest_currency)
        future_currency = self.url[init_index_dest_currency:]

        return original_currency, future_currency

    def find_start_index_substring(self, currency):
        return self.url.find(currency) + len(currency) + 1


if __name__ == "__main__":

    url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dólar"
    arg = ExtractorArgUrl(url)
    original_currency, future_currency = arg.get_arguments()
    print(future_currency +"\t"+ original_currency)