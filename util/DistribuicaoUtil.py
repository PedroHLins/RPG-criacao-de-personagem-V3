class Distribuicao:

    @staticmethod
    def distribuir_valores_selecionados(personagem, dados_formulario):
        personagem.atributos["Forca"] = int(dados_formulario.get("Forca"))
        personagem.atributos["Destreza"] = int(dados_formulario.get("Destreza"))
        personagem.atributos["Constituicao"] = int(dados_formulario.get("Constituicao"))
        personagem.atributos["Inteligencia"] = int(dados_formulario.get("Inteligencia"))
        personagem.atributos["Sabedoria"] = int(dados_formulario.get("Sabedoria"))
        personagem.atributos["Carisma"] = int(dados_formulario.get("Carisma"))

    @staticmethod
    def classico(personagem, valores):
        i = 0
        for key in personagem.atributos.keys():
            resultado = valores[i]
            personagem.atributos[key] = resultado
            i = i.__add__(1)

    @staticmethod
    def aventureiro_heroico(personagem, dados_formulario):
        Distribuicao.distribuir_valores_selecionados(personagem, dados_formulario)