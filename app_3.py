from fastapi import FastAPI, HTTPException
import uvicorn
import requests

app = FastAPI()

@app.get('/')
def index():
    try:
        deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()
        response_cards = requests.get(f"https://deckofcardsapi.com/api/deck/{deck["deck_id"]}/draw/?count=1").json()
        return f"{response_cards['cards'][0]['value']} of {response_cards['cards'][0]['suit']}"
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Erro ao acessar o servidor")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5002)
