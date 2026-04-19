#Movie Agent
This is an improvement on my origional movie reccomendation agent that used rasa. That was a rule based agent and now I'm making a more free flowing agent with the use of LLMs.

Similarly to my origional version, this agent will use TMDB API to access information about movies and reccomend a movie to the user. The big difference is that a Pydantic AI agent with an OpenAI LLM will be the decision maker instead of the Rasa framework. This will allow for a longer conversation with more freedom to change your mind and switch directions. 