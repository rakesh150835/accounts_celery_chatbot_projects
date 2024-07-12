from openai import OpenAI



client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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"
)



def get_response_from_model(user_message):
    prompt = f"""

      You are an AI chatbot specialized in cricket. Your task is to respond only to queries related to cricket topics. 

      Ensure that all responses are relevant and detailed within the context of cricket.

      If the user query is not related to cricket, please inform the user that you can only answer cricket-related questions.


      Recognize and respond to queries related to cricket topics such as 'matches', 'scores', 'players', 'teams', 'tournaments', 'statistics', 'news', 'results', 'records', 'leagues', 'training', 'coaches', 'playoffs', 'injuries', 'events', 'analysis', 'commentary', 'highlights', 'team standings', 'seasons', 'World Cup', 'IPL', 'T20', 'ODI', 'Test matches', WPL, Big Bash, Hundred, batting, bowling, world test championship, wickets, pitch.
        
      User: {user_message}
      Bot:
    """
    
    completion = client.chat.completions.create(
            model="google/gemma-7b-it:free",
            messages=[
                {
                "role": "system",
                "content": prompt,
                },
                {
                "role": "user",
                "content": user_message,
                },
                
            ],
    )

    return completion.choices[0].message.content

    
    



