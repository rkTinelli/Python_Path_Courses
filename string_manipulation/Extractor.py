class ExtractorArgUrl():
    def __init__(self, url):
        if self.valid_url(url):        
            self.url = url.lower()
        else:
            raise LookupError("Invalid URL provided")

    @staticmethod
    def valid_url(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    def get_arguments(self):

        tag_orin_currency = "moedaorigem"
        tag_dest_currency = "moedadestino"

        init_index_orin_currency = self.find_start_index_substring(tag_orin_currency)
        end_index_orin_currency = self.url.find("&")
        original_currency = self.url[init_index_orin_currency:end_index_orin_currency]

        if original_currency == "moedadestino":
            original_currency = self.replaceOriginCurrency(tag_orin_currency)

        init_index_dest_currency = self.find_start_index_substring(tag_dest_currency)
        end_index_dest_currency = self.url.find("&",init_index_dest_currency)
        future_currency = self.url[init_index_dest_currency:end_index_dest_currency]

        return original_currency, future_currency

    def find_start_index_substring(self, currency):
        return self.url.find(currency) + len(currency) + 1

    def replaceOriginCurrency(self, originCurrency):
        self.url = self.url.replace("moedadestino", "real", 1)  # primeiro vou fazer sem o 1 e depois vou usa-lo
        init_index_orin_currency = self.find_start_index_substring(originCurrency)
        end_index_orin_currency = self.url.find("&")
        return self.url[init_index_orin_currency:end_index_orin_currency]

    def get_value(self):
        value_tag = "Valor".lower()
        init_index_valeu = self.find_start_index_substring(value_tag)
        value = self.url[init_index_valeu:]
        return value

    def __eq__(self,anotherInstance):
      return self.url == anotherInstance.url

    def __len__(self):
      return len(self.url)

    def __str__(self):
        moedaOrigem,moedaDestino = self.get_arguments()
        representacaoString2 = "Valor:" + self.get_value() + " " + moedaOrigem + " " + moedaDestino
        representacaoString  = "Valor: {}\n Moeda Origem: {} \n Moeda Destino: {} \n".format(self.get_value(),moedaOrigem,moedaDestino)
        return representacaoString

if __name__ == "__main__":
    
    url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
    arg = ExtractorArgUrl(url)
    original_currency, future_currency = arg.get_arguments()
    currency_amount = arg.get_value()
    print(future_currency +"\t"+ original_currency +"\t"+ currency_amount)
    print(arg)
    print(len(arg))
    