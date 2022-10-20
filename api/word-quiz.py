import requests

url = "https://twinword-word-association-quiz.p.rapidapi.com/type1/"

querystring = {"level":"3","area":"sat"}

headers = {
	"X-RapidAPI-Key": "cd7cc895ddmshf60d83e19ae6edep1e28a3jsn7c5ab84381c7",
	"X-RapidAPI-Host": "twinword-word-association-quiz.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)