import os
import openai

openai.api_key = "[INSIRA A CHAVE DA API OPENAI]"

solicitacao = input("O que deseja buscar?\n")

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "Dadas as tabelas SQL a seguir, seu trabalho é escrever consultas de acordo com a solicitação de um usuário.\n\n"
                 "CREATE TABLE Publicacao (ISSN VARCHAR(50) PRIMARY KEY, TituloP VARCHAR(50) NOT NULL, Editor VARCHAR(50), URL VARCHAR(100));CREATE TABLE Area(AreaID NUMBER PRIMARY KEY, DescricaoA VARCHAR(50) NOT NULL);CREATE TABLE Artigo (ArtigoID NUMBER PRIMARY KEY, TituloA VARCHAR(50) NOT NULL UNIQUE, ISSN VARCHAR(50) NOT NULL, Ano DATE,NumeroDePaginas NUMBER CHECK(NumeroDePaginas > 0),  AreaID NUMBER, CONSTRAINT FK_AreaID_Area FOREIGN KEY(AreaID) REFERENCES Area(AreaID),CONSTRAINT FK_ISSN_Publicacao FOREIGN KEY(ISSN) REFERENCES Publicacao(ISSN));CREATE TABLE PalavraChave (PC NUMBER PRIMARY KEY, DescricaoPC VARCHAR(50));CREATE TABLE ArtigoPC (ArtigoID NUMBER, PC NUMBER,CONSTRAINT PKArtigoPC PRIMARY KEY(ArtigoID, PC),CONSTRAINT FK_ArtigoID_Artigo FOREIGN KEY(ArtigoID) REFERENCES Artigo(ArtigoID),CONSTRAINT FK_PC_PalavraChave FOREIGN KEY(PC) REFERENCES PalavraChave(PC));"
    },
    {
      "role": "user",
      "content": solicitacao
    }
  ],
  temperature=0,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)